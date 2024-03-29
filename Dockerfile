FROM python:3.11.3-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ["requirements.txt", "run.sh", "./"]
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt && chmod +x ./run.sh

# copy project
COPY . .

# Set entrypoint
ENTRYPOINT bash ./run.sh
