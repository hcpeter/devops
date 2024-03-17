# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask is running on
EXPOSE 3000

# Define environment variable
ENV FLASK_APP=app.py

# Run flask app
#CMD ["flask", "run", "--host", "0.0.0.0"]
CMD python ./app.py
