#!/bin/bash

# Launch of Celery worker
celery -A  tasks worker -l info --concurrency=2 &

# Launching Celery Flower (interface for monitoring Celery)
celery -A tasks flower -l info &

# Launch Celery Beat (for scheduling tasks)
celery -A tasks beat -l INFO &

# Launching FastAPI with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --reload --workers 2
