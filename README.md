# FastAPI for User and Tasks with Categories Management
This project is a server-side component of a web application that provides APIs for managing users and tasks and their categories. It uses the FastAPI framework to create API endpoints and stores data in a PostgreSQL database.
## Technologies Used

*  Backend: FastAPI.
*  Database: Async PostgreSQL.
*  ORM:  SQLAlchemy.
*  Docker for containerization.
*  Celery + Redis for tasks
*  JWT for authentication. 


## Installing / Getting started:
```shell
To get started, you need to clone the repository from GitHub: https://github.com/Morty67/test_kollectiv_fast_api/tree/developer
Python 3.11.3 must be installed

python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)

pip install -r requirements.txt

Your settings for DB in .env file:

DB_HOST=YOUR DB_HOST
DB_PORT=YOUR DB_PORT
DB_NAME=YOUR DB_NAME
DB_USER=YOUR DB_USER
DB_PASS=YOUR DB_PASS

SMTP_USER=YOUR SMTP_USER
SMTP_PASSWORD=YOUR SMTP_PASSWORD

JWT_SECRET_KEY=YOUR JWT_SECRET_KEY

alembic upgrade head
uvicorn app.main:app --reload

```

## How to get access
Domain:
*  localhost:8000 or 127.0.0.1:8000 (127.0.0.1:8000/docs)

## Run Docker 🐳
Docker must be installed :
* docker-compose up --build
* FastAPi server in Docker http://localhost:8001/docs
* Celery flower http://localhost:5556/
```shell


## Features:
*  Optimization of image quality in jpec format at the endpoint /images/optimize-image/, the result can be sent to your email. Powered by Celery + Redis
*  Save Tasks: Create or update an Tasks in the database.
*  Save User: Create or update a user in the database.
*  Save Category: Create or update a category in the database.
*  This project implements JWT-based authentication for securing API endpoints. To access protected endpoints, users must obtain a valid JWT token by following the authentication process.
*  API documentation is available at http://localhost:8000/docs when the application is running. You can explore and test the endpoints using the Swagger UI.

