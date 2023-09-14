# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /flaskapp
WORKDIR /flaskapp

# Copy flaskapp directory contents into the container at /flaskapp
COPY flaskapp /flaskapp

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Run main.py when the container launches
CMD["main.py"]

ENTRYPOINT["python"]