import sys
import qrcode
from dotenv import load_dotenv
import logging.config
from pathlib import Path
import os
import argparse
from datetime import datetime
import validators  # Import the validators package
import re
import urllib.parse

# Load environment variables
load_dotenv()

# Environment Variables for Configuration
QR_DIRECTORY = os.getenv('QR_CODE_DIR', 'qr_codes')  # Directory for saving QR code
FILL_COLOR = os.getenv('FILL_COLOR', 'red')  # Fill color for the QR code
BACK_COLOR = os.getenv('BACK_COLOR', 'white')  # Background color for the QR code

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )

def create_directory(path: Path):
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")
        exit(1)

def is_valid_url(url):
    if validators.url(url):
        return True
    else:
        logging.error(f"Invalid URL provided: {url}")
        return False

def parse_github_pr_command(command):
    """
    Parse GitHub CLI-style PR commands and convert them to GitHub PR URLs.
    Supports commands like 'gh pr checkout 32' or just 'pr 32'
    """
    # Pattern to match 'gh pr checkout <number>' or 'pr <number>'
    pr_pattern = r'(?:gh\s+)?pr\s+(?:checkout\s+)?(\d+)'
    match = re.search(pr_pattern, command.lower())
    
    if match:
        pr_number = match.group(1)
        # For this repository, construct the PR URL
        repo_url = "https://github.com/aravindvemulaa/improved-qr-docker-2024"
        pr_url = f"{repo_url}/pull/{pr_number}"
        logging.info(f"Parsed GitHub PR command '{command}' to URL: {pr_url}")
        return pr_url
    
    return None

def process_input(input_data):
    """
    Process input data which can be:
    1. A regular URL
    2. A GitHub CLI command like 'gh pr checkout 32'
    3. A simplified PR reference like 'pr 32'
    """
    # First check if it's a GitHub CLI command
    pr_url = parse_github_pr_command(input_data)
    if pr_url:
        return pr_url
    
    # If not a GitHub command, treat as regular URL
    return input_data

def generate_qr_code(data, path, fill_color='black', back_color='white'):
    # Process the input data (could be URL or GitHub command)
    processed_url = process_input(data)
    
    if not is_valid_url(processed_url):
        return  # Exit the function if the URL is not valid

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(processed_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        with path.open('wb') as qr_file:
            img.save(qr_file)
        logging.info(f"QR code successfully saved to {path}")
        if processed_url != data:
            logging.info(f"Original input: {data}")
            logging.info(f"Generated QR code for: {processed_url}")

    except Exception as e:
        logging.error(f"An error occurred while generating or saving the QR code: {e}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Generate a QR code for URLs or GitHub PR commands.')
    parser.add_argument('--url', help='The URL to encode in the QR code or GitHub CLI command (e.g., "gh pr checkout 32")', default='https://github.com/aravindvemulaa/improved-qr-docker-2024/blob/main/README.md')
    args = parser.parse_args()

    # Initial logging setup
    setup_logging()
    
    # Generate a timestamped filename for the QR code
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    qr_filename = f"QRCode_{timestamp}.png"

    # Create the full path for the QR code file
    qr_code_full_path = Path.cwd() / QR_DIRECTORY / qr_filename
    
    # Ensure the QR code directory exists
    create_directory(Path.cwd() / QR_DIRECTORY)
    
    # Generate and save the QR code
    generate_qr_code(args.url, qr_code_full_path, FILL_COLOR, BACK_COLOR)

if __name__ == "__main__":
    main()
