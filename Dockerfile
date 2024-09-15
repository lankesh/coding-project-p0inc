# Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY src ./src

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
# This flag makes sure to output logs directly to console
ENV PYTHONUNBUFFERED=1

# Run the FastAPI app with Uvicorn server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
