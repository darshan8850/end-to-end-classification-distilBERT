FROM python:3.9-slim-buster

WORKDIR /app
COPY . /app

# Install dependencies and clean up
RUN apt-get update && apt-get install -y --no-install-recommends awscli \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Use ENTRYPOINT for better argument handling
ENTRYPOINT ["python3", "app.py"]