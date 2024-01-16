# Use the official Python image as a base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt
RUN pip install tensorflow==2.10.0

# Copy the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000
# Command to run the application
CMD ["flask", "run"]