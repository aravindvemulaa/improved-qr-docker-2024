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
docker build -t my-qr-app .
```

also run all the commands in the terminal  below for 
Setting Environment Variables for QR Code Customization
- 1. Setting Environment Variables for QR Code Customization
- 2. Sharing a Volume for QR Code Output
- 3. Setting Arguments for the URL from the Terminal
  using commands
for windows powershell
```powershell 
    docker run -d --name qr-generator `
  -e QR_DATA_URL="https://example.com" `
  -e QR_CODE_DIR="qr_codes" `
  -e QR_CODE_FILENAME="exampleQR.png" `
  -e FILL_COLOR="blue" `
  -e BACK_COLOR="yellow" `
  -v "C:\host\path\for\qr_codes:/app/qr_codes" `
  my-qr-app
```
for mac or linux
```bash
    docker run -d --name qr-generator \
  -e QR_DATA_URL="https://example.com" \
  -e QR_CODE_DIR="qr_codes" \
  -e QR_CODE_FILENAME="exampleQR.png" \
  -e FILL_COLOR="blue" \
  -e BACK_COLOR="yellow" \
  -v /host/path/for/qr_codes:/app/qr_codes \
  my-qr-app

```

### Running the Application

Once the image is built successfully, you can run the application using the following command:
 for mac and linux below command can be used
```bash
docker run -v .:/app my-qr-app --url your_git_hub_profile_link_or_any_link_
```
for windows powershell, you can use the following command:
```powershell
docker run -v ${PWD}:/app qr_codes --url your_git_hub_profile_link_or_any_link
```
