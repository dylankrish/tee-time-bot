# Base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the repository to the working directory in the container
COPY . .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure chrome for testing is downloaded
RUN python -c "from selenium import webdriver; driver = webdriver.Chrome(); driver.quit()"

# Set the entry point for the container
ENTRYPOINT ["python", "book.py"]