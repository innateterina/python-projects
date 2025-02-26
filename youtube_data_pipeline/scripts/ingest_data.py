import json
import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# ✅ Ensure correct path to JSON file
json_file_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "dataset", "raw_data.json"))

print(f"📌 JSON file path: {json_file_path}")

# Check if the file exists
if not os.path.exists(json_file_path):
    raise FileNotFoundError(f"❌ JSON file not found at: {json_file_path}")

# Load JSON data
with open(json_file_path, "r") as file:
    raw_data = json.load(file)

print("✅ JSON file loaded successfully!")

# ✅ Detect if running inside Docker
DOCKERIZED = os.getenv("DOCKERIZED", "false").lower() == "true"
DB_HOST = "youtube_postgres" if DOCKERIZED else "localhost"

# ✅ Database connection settings
DB_NAME = "youtube_data"
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_PORT = "5432"

# ✅ Create database connection using SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f"🔗 Connecting to DB: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# ✅ Define the database model
Base = declarative_base()


class VideoCategory(Base):
    __tablename__ = "video_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, unique=True, nullable=False)
    title = Column(String, nullable=False)
    assignable = Column(Boolean, nullable=False)


# ✅ Create the table if it doesn't exist
Base.metadata.create_all(engine)

# ✅ Create a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# ✅ Insert data into PostgreSQL
for item in raw_data["items"]:
    category = VideoCategory(
        category_id=int(item["id"]),
        title=item["snippet"]["title"],
        assignable=item["snippet"]["assignable"]
    )
    session.merge(category)  # Insert or update if exists

session.commit()
session.close()

print("✅ Data successfully inserted into PostgreSQL using SQLAlchemy!")
