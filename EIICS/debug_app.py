
"""
debug_app.py - Debug version to find where the segmentation fault occurs
"""

import tkinter as tk
from tkinter import messagebox
import os
import glob
import sys
import traceback

print("=== STARTING DEBUG ===")
print(f"Python: {sys.version}")
print(f"Working dir: {os.getcwd()}")

def test_pillow():
    """Test Pillow functionality"""
    print("Testing Pillow...")
    try:
        from PIL import Image
        print("✓ PIL import successful")
        
        # Test creating a simple image
        img = Image.new('RGB', (100, 100), color='red')
        print("✓ Image creation successful")
        return True
    except Exception as e:
        print(f"✗ Pillow test failed: {e}")
        return False

def test_crypto():
    """Test Crypto functionality"""
    print("Testing Crypto...")
    try:
        from Crypto.Cipher import AES
        from Crypto.Random import get_random_bytes
        print("✓ Crypto imports successful")
        
        # Test simple crypto operation
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_ECB)
        print("Crypto operations successful")
        return True
    except Exception as e:
        print(f"Crypto test failed: {e}")
        return False

def test_tkinter():
    """Test Tkinter functionality"""
    print("Testing Tkinter...")
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the window
        print("✓ Tkinter initialization successful")
        
        # Test message box
        messagebox.showinfo("Test", "Tkinter works!")
        print("✓ Message box test successful")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ Tkinter test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("\n1. Testing libraries...")
    
    tests = [
        ("Pillow", test_pillow),
        ("Crypto", test_crypto),
        ("Tkinter", test_tkinter),
    ]
    
    all_passed = True
    for name, test_func in tests:
        try:
            if not test_func():
                all_passed = False
        except Exception as e:
            print(f"✗ {name} test crashed: {e}")
            all_passed = False
        print()
    
    if all_passed:
        print("✓ All basic tests passed!")
        print("Now testing main application...")
        test_main_app()
    else:
        print("Some tests failed. The main app will likely fail too.")
        input("Press Enter to exit...")

def test_main_app():
    """Test the main application step by step"""
    print("2. Testing main application")
    
    try:
        # Test imports
        print("Testing main app imports...")
        from main_app import EIICSApp
        print("✓ Main app import successful")
        
        # Test initialization
        print("Testing app initialization...")
        root = tk.Tk()
        root.withdraw()  # Hide during testing
        
        app = EIICSApp(root)
        print("✓ App initialization successful")
        
        # Test welcome screen
        print("Testing welcome screen...")
        app.show_welcome_screen()
        print("Welcome screen successful")
        
        root.destroy()
        print("All tests completed successfully!")
        
    except Exception as e:
        print(f"Main app test failed: {e}")
        traceback.print_exc()
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()