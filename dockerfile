# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables for database connection
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DATABASE_URL=${DATABASE_URL}
ENV DB_PORT=${DB_PORT}
ENV DB_NAME=${DB_NAME}

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
