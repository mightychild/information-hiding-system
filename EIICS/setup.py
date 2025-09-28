"""
setup.py
Setup script for Encryption Image Information Concealing System (EIICS)
"""

from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="eiics",
    version="1.0.0",
    description="Encryption Image Information Concealing System - A secure steganography application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/eiics",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "eiics": [
            "default_images/*.png",
            "default_images/*.jpg",
            "default_images/*.jpeg"
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "gui_scripts": [
            "eiics=eiics.main_app:main",
        ],
        "console_scripts": [
            "eiics-console=eiics.main_app:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.8",
    keywords="steganography, encryption, security, image-processing",
    # Add platform-specific icons
    options={
        'build_exe': {
            'include_files': [
                ('assets/icon.ico', 'icon.ico'),
                ('assets/icon.png', 'icon.png'),
            ],
        },
    },
)