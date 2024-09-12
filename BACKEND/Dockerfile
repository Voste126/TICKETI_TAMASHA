# Use the Python 3 slim image
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install pip requirements
COPY BACKEND/requirements.txt /app/
RUN python -m pip install -r requirements.txt

# Copy the entire project into the container
COPY BACKEND /app

# Create a non-root user with an explicit UID and add permissions to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Run Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Tamasha.wsgi:application"]
