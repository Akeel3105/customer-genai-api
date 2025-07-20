# Use a small Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt


# Copy your app code into the container
COPY ./app ./app

# Expose FastAPI port
EXPOSE 8000

# Run the API using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
