# Use a lightweight Python environment
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API code into the container
COPY app.py .

# Tell Docker this container uses port 5000
EXPOSE 5000

# Start the application using Gunicorn for better performance
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
