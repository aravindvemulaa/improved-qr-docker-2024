# improved-qr-docker-2024

# QR Codes Project

This project is designed to generate QR codes based on provided URLs. It utilizes Docker for containerization, making it easy to run the application in a consistent environment.

## Getting Started

### Prerequisites

- Docker installed on your machine.
- Basic knowledge of Docker commands.

### Building the Docker Image

Before running the application, you need to build the Docker image. Navigate to the project directory where the `Dockerfile` is located and run the following command:

```bash or windows
docker build -t qr_codes .
```

also run all the commands in the terminal  below for 
Setting Environment Variables for QR Code Customization
- 1. Setting Environment Variables for QR Code Customization
- 2. Sharing a Volume for QR Code Output
- 3. Setting Arguments for the URL from the Terminal

### Running the Application

Once the image is built successfully, you can run the application using the following command:

```bash
docker run -v .:/app qr_codes --url http://www.nobody.com
```
if your system os is windows, you can use the following command:
```bash
docker run -v ${PWD}:/app qr_codes --url http://www.nobody.com
```
