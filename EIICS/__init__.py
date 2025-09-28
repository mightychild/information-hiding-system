"""
EIICS - Encryption Image Information Concealing System
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .main_app import EIICSApp
from .crypto_engine import CryptoEngine
from .stego_engine import StegoEngine
from .help_content import HelpContent

__all__ = ['EIICSApp', 'CryptoEngine', 'StegoEngine', 'HelpContent']