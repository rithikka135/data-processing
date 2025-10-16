# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY ./app /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install pandas numpy scikit-learn kafka-python pyspark

# Set default command
CMD ["bash"]
