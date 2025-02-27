YouTube Data Pipeline

This project sets up a YouTube Data Pipeline that extracts, transforms, and loads (ETL) video category data from a JSON file into a PostgreSQL database using Docker and SQLAlchemy.

🚀 Project Overview

Extract: Reads raw_data.json from the dataset/ directory.

Transform: Parses and structures the data.

Load: Inserts the data into a PostgreSQL database running in Docker.

📂 Project Structure

├── dataset/
│ ├── raw_data.json # YouTube video category data
│
├── database/
│ ├── init.sql # SQL script to initialize the database (optional)
│
├── scripts/
│ ├── ingest_data.py # ETL script using SQLAlchemy
│ ├── query_data.py # Query script using SQLAlchemy
│
├── Dockerfile # Defines the app container
├── docker-compose.yml # Defines the PostgreSQL and app services
├── requirements.txt # Python dependencies
├── README.md # Documentation

🛠 Setup & Installation

1️⃣ Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose

- Python 3.11+ (for running scripts locally)

2️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/youtube-data-pipeline.git
cd youtube-data-pipeline
```

3️⃣ Start the Docker Containers

```sh
docker-compose up -d
```

This will:
✅ Start a PostgreSQL database inside Docker.
✅ Start the Python ingestion script, which loads data into PostgreSQL.

4️⃣ Verify the Data in PostgreSQL

Run the following command to check if data was inserted:

```sh
docker exec -it youtube_postgres psql -U admin -d youtube_data -c "SELECT \* FROM video_categories;"
```

If everything is correct, you should see the YouTube categories.

5️⃣ Query the Data

Run the query script to fetch and display data:

```sh
python scripts/query_data.py
```

🛠 Development & Testing

Run the ETL Script Locally

If you want to run the ingest_data.py script locally, first install dependencies:

```sh
pip install -r requirements.txt
```

Then, run:

```sh
python scripts/ingest_data.py
```

Stop & Clean Up Containers

To stop and remove all Docker containers and volumes:

```sh
docker-compose down -v
```
