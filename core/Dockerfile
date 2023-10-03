# Dockerfile
FROM python:3.11

# Set the working directory to /app
WORKDIR /core

# Copy the current directory contents into the container at /app
COPY . /core

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME World

# Run server.py when the container launches
CMD ["bash", "-c", "gunicorn app:app -b 0.0.0.0:8000"]