# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables (can be overridden at runtime)
ENV MAILER_API_URL=http://mailer:8001
ENV AI_ROUTER_API_URL=http://ai-router:8002
ENV POLLING_INTERVAL=30
ENV TARGET_SENDER=""

# Disable Python output buffering for real-time logs
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]