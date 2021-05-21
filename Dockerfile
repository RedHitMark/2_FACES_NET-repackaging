FROM python:3.8.5

# Install JDK
RUN apt update -y && apt install -y default-jdk
RUN java --version
RUN keytool -help

# Move in server folder
WORKDIR /server/javalib

# Generate key
RUN keytool -genkey -noprompt -dname "CN=mqttserver.ibm.com, OU=ID, O=IBM, L=Hursley, S=Hants, C=GB" -v -keystore "/server/javalib/debug.keystore" -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000

# Move in server folder
WORKDIR /server

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy requirements.txt and install all dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files in server directory
COPY . .

# Expose server port
EXPOSE 5000

# Run FastAPI application
CMD ["python", "-m", "app"]