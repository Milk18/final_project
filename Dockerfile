# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /flaskapp

# Copy the current directory contents into the container at /app
COPY . /flaskapp

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 9000
# Run app.py when the container launches
ENTRYPOINT ["python", "main.py"]
