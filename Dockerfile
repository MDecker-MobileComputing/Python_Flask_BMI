# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY bmi_app.py .

# Expose the port the app runs on
EXPOSE 8080

# Set environment variables for Flask
ENV FLASK_APP=bmi_app.py
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "bmi_app.py"]
