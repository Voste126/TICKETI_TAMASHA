# Use the official Python image as a base image
FROM python@sha256:3c5e2b2e8b3d5b9b8c2e8e8d5b6b3c5e2b2e8b3d5b9b8c2e8e8d5b6b3c5e2b2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "TAMASHA.wsgi:application", "--bind", "0.0.0.0:8000"]