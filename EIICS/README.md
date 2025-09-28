# Encryption Image Information Concealing System (EIICS)

A professional steganography application that allows you to hide encrypted data within images using AES-256 encryption and LSB steganography.

## Features

- **Text Embedding**: Hide secret text messages in images
- **File Embedding**: Conceal any type of file within images
- **Military-Grade Encryption**: AES-256 CBC with HMAC authentication
- **User-Friendly Interface**: Modern GUI with intuitive workflow
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Installation

### Method 1: PIP Installation
```bash
pip install eiics


### Method 2: FROM SOURCE
```bash
git clone https://github.com/yourusername/eiics.git
cd eiics
pip install .

## Method 3: Standalone Executable
Download the latest release for your operating system from the Releases page.


## Usage
### 1. Launch the application:
```bash
eiics

### 2. Embed Data:

Choose "Embed Text" or "Embed File"

Select a cover image (or use default images)

Enter your secret data and encryption key

Save the stego image

### 3. Extract Data:

Choose "Extract Data"

Select the stego image

Enter the decryption key

View or save the extracted content

## System Requirements
Python: 3.8 or higher

Operating Systems: Windows 10+, Ubuntu 18.04+, macOS 10.15+

RAM: 4GB minimum, 8GB recommended

Storage: 100MB free space

## Building from Source
### Prerequisites
Python 3.8+

pip

build tools

### Build Steps
```bash
# Clone the repository
git clone https://github.com/yourusername/eiics.git
cd eiics

# Install build dependencies
pip install build wheel

# Build the package
python -m build

# The built packages will be in the dist/ directory

## Creating Standalone Executables
### Using PyInstaller
```bash
pip install pyinstaller
pyinstaller eiics.spec

### Using cx_Freeze
```bash
pip install cx-freeze
python setup.py build_exe


## Security Features
AES-256 CBC encryption with PBKDF2 key derivation

HMAC authentication for data integrity

Secure memory management

No data leakage or logging

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For support, bug reports, or feature requests:

Create an issue on GitHub

Email: support@example.com