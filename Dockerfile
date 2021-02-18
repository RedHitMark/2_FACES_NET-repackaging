FROM python:3.8.5

# Install JDK
RUN apt update -y && apt install -y default-jdk
RUN java --version

# Upgrade pip
RUN python -m pip install --upgrade pip

# Move in app folder
WORKDIR /server

# Copy requirements.txt and install all dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files in server directory
COPY . .

# Expose Flask server port
EXPOSE 5000

# Run flask application
CMD ["python", "-m", "app"]