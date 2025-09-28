#!/bin/bash
echo "Installing EIICS with icons..."
pip3 install dist/eiics-1.0.0-py3-none-any.whl

# Install desktop entry and icon (optional)
echo "Installing desktop entry..."
sudo mkdir -p /usr/share/icons/eiics/
sudo cp assets/icon.png /usr/share/icons/eiics/
sudo cp eiics.desktop /usr/share/applications/

echo "Installation complete!"