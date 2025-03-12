FROM python:3.10

# Install system dependencies (Poppler)
RUN apt-get update && apt-get install -y poppler-utils

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Command to run the application
CMD ["python", "app.py"]
