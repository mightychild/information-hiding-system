"""
help_content.py
Central repository for help and about content for EIICS
"""

class HelpContent:
    """Static content for help and about dialogs"""
    
    ABOUT_TITLE = "About EIICS"
    
    ABOUT_TEXT = """
Encryption Image Information Concealing System (EIICS)
Version 1.0
© 2024 EIICS

A secure application for hiding encrypted data within images using the Least Significant Bit (LSB) technique combined with AES-256 encryption.

This tool allows you to:
• Embed secret text messages into images
• Hide entire files within images
• Extract hidden data with the correct key

Built with Python, PyCryptodome, and PIL/Pillow.
"""

    HELP_TITLE = "EIICS Help"
    
    HELP_TEXT = """
Getting Started

1. Embedding Data:
   • Choose 'Embed Text' to hide a text message or 'Embed File' to hide a document.
   • Select a cover image (PNG format is recommended).
   • Provide your data and a strong encryption key.
   • Save the resulting stego image.

2. Extracting Data:
   • Choose 'Extract Data'.
   • Select the stego image containing hidden data.
   • Enter the encryption key used during embedding.
   • View extracted text or save the extracted file.

Important Notes

• SECURITY: Your encryption key is essential for extraction. It cannot be recovered if lost.
• FORMATS: For reliable results, always use PNG images as your cover files. JPEG compression can destroy hidden data.
• CAPACITY: The amount of data you can hide depends on the resolution of your cover image.
• LIMITATIONS: This tool is for legitimate use only. Always respect copyright and privacy laws.
"""

    TIPS_TITLE = "Pro Tips"
    
    TIPS_TEXT = """
• Use high-resolution images for hiding larger files.
• Choose a strong, complex encryption key for maximum security.
• The application works best with PNG and BMP images. Avoid JPEG.
• Always test extraction immediately after embedding to verify it works.
• Keep your original cover image without hidden data as a backup.
"""