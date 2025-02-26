import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# ✅ Ensure correct database settings
DB_NAME = "youtube_data"
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"

# ✅ Adjust host for Docker compatibility
DOCKERIZED = os.getenv("DOCKERIZED", "false").lower() == "true"
DB_HOST = "youtube_postgres" if DOCKERIZED else "localhost"

# ✅ Create database connection using SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# ✅ Create session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# ✅ Define the table model (Matching ingest_data.py)
Base = declarative_base()


class VideoCategory(Base):
    __tablename__ = "video_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, unique=True, nullable=False)
    title = Column(String, nullable=False)
    assignable = Column(Boolean, nullable=False)


# ✅ Query and display results
try:
    print("✅ Successfully connected to PostgreSQL!")

    # Fetch all categories
    categories = session.query(VideoCategory).all()

    # Display results
    print("\n📌 YouTube Video Categories:")
    for category in categories:
        print(
            f"🔹 {category.category_id} | {category.title} | Assignable: {category.assignable}")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    session.close()
    print("\n✅ Query completed!")
