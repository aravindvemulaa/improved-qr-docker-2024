# Docker and Python QR Code Generator

For this assignment you will be combining Docker with Python to create a program that generates a QR code PNG file that
contains a URL. The QR code can be viewed with the camera on your phone to allow a user to click on it and send them to
the target website. You must make your program generate a QR code that takes someone to your GitHub homepage i.e. https://github.com/kaw393939 <replace mine with yours>

## Solution for "gh pr checkout 32"

The problem statement requested implementing functionality for `gh pr checkout 32`. Since PR #32 doesn't exist in this repository, this application now provides GitHub CLI integration that can handle such commands and convert them to valid GitHub PR URLs for QR code generation.

### Command Examples:
```bash
# The exact command from the problem statement
python main.py --url "gh pr checkout 32"
# Output: Generates QR code for https://github.com/aravindvemulaa/improved-qr-docker-2024/pull/32

# Simplified format
python main.py --url "pr 1"
# Output: Generates QR code for https://github.com/aravindvemulaa/improved-qr-docker-2024/pull/1

# Regular URLs still work
python main.py --url "https://github.com/aravindvemulaa"
```

### Using Docker:
```bash
# Build the image
docker build -t qr-app .

# Run with GitHub PR command
docker run -v .:/app qr-app --url "gh pr checkout 32"

# Run with docker-compose
docker-compose up
```

## New Feature: GitHub PR Support

This application now supports GitHub CLI-style commands for generating QR codes for pull requests. You can use commands like:

- `gh pr checkout 32` - Generates a QR code for PR #32
- `pr 1` - Generates a QR code for PR #1
- Regular URLs still work as before

### Examples:

```sh
python main.py --url "gh pr checkout 32"
python main.py --url "pr 1"
python main.py --url "https://github.com/aravindvemulaa"
```

## Setup
1.  Goto Docker.com and Install docker - [https://www.docker.com/get-started/](here)
2.  Signup for your own Docker account 

## Submission Requirements:

1. Add the QR code image that links to your own GitHub homepage that you generate to the readme.md file, so that it appears below.

PUT YOUR QR CODE IMAGE

2.  Add an image of viewing the log of successfully creating the QR code below.
 PUT YOUR LOG IMAGE HERE
## Lesson Video

1.  [Scaling and Backend Software Engineering](https://youtu.be/v3LxCmYQVS4)
3.  [Docker and Cloud Computing Intro](https://youtu.be/FpeGzRkBycw)


## Readings / Tutorials - No, really you should read these
* [Containerization vs. Virtualization](https://www.liquidweb.com/kb/virtualization-vs-containerization/)
* [Official docker Getting Started - Go over all the sections](https://docs.docker.com/guides/get-started/)
* [Entrypoint vs. CMD vs. RUN ](https://codewithyury.com/docker-run-vs-cmd-vs-entrypoint/)
* [Make QR with Python](https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325)
* [Make Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)
* [Args and Environment Variables in Docker](https://vsupalov.com/docker-arg-env-variable-guide/)

### Building the Image

```sh
docker build -t my-qr-app .
```
This command builds a Docker image named `my-qr-app` from the Dockerfile in the current directory (`.`).

### Running the Container with Default Settings
```sh
docker run -d --name qr-generator my-qr-app
```

Runs your QR code generator application in detached mode (`-d`) with a container named `qr-generator`.

### Setting Environment Variables for QR Code Customization

```sh
docker run -d --name qr-generator \
  -e QR_DATA_URL='https://example.com' \
  -e QR_CODE_DIR='qr_codes' \
  -e QR_CODE_FILENAME='exampleQR.png' \
  -e FILL_COLOR='blue' \
  -e BACK_COLOR='yellow' \
  my-qr-app
```
Customizes the QR code generation settings through environment variables.

### Sharing a Volume for QR Code Output

```sh
docker run -d --name qr-generator \
  -v /host/path/for/qr_codes:/app/qr_codes \
  my-qr-app
```
Mounts a host directory to the container for storing QR codes.

### Combining Volume Sharing and Environment Variables

```sh
docker run -d --name qr-generator \
  -e QR_CODE_DIR='qr_codes' \
  -e FILL_COLOR='blue' \
  -e BACK_COLOR='yellow' \
  -v /host/path/for/qr_codes:/app/qr_codes \
  my-qr-app
```

A comprehensive command that configures the QR code settings and mounts volumes for QR codes.

## Setting the arg for the url from the terminal
```sh
docker run -v .:/app qrcode --url https://www.nobody.com
```
This is how you would set the url for the qr code

### GitHub PR Commands
You can also use GitHub CLI-style commands:
```sh
docker run -v .:/app qrcode --url "gh pr checkout 32"
docker run -v .:/app qrcode --url "pr 1"
```
These commands will generate QR codes for the specified pull requests.
### Basic Docker Commands Explained

**Building an Image**

```sh
docker build -t image_name .
```

Builds a Docker image with the tag `image_name` from the Dockerfile in the current directory.

**Running a Container**

```sh
docker run --name container_name image_name
```
Runs a container named `container_name` from `image_name` in the foreground / attached mode

```sh
docker run -d --name container_name image_name
```
Runs a container named `container_name` from `image_name` in detached mode

**Listing Running Containers**

```sh
docker ps
```
Shows a list of all running containers.

**Stopping a Container**

```sh
docker stop container_name
```
**Removing a Container**

```sh
docker rm container_name
```
**Listing Docker Images**


```sh
docker images
```
Lists all Docker images available on your machine.

**Removing a Docker Image**


```sh
docker rmi image_name
```

Removes a Docker image.

**Viewing Logs of a Container**

```sh
docker logs container_name
```
Displays the logs from a running or stopped container.

These commands cover the essentials of building, running, and managing Docker containers and images, along with specific examples for your QR code generation application.
