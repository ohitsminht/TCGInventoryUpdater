#!/usr/bin/env python3
"""
Simple launcher script for macOS users
This bypasses the PyInstaller issues and runs the app directly
"""

import sys
import os
import subprocess

def main():
    print("TCGPlayer Inventory Updater - macOS Launcher")
    print("=" * 50)
    
    # Check if Python 3 is available
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        print("Please install Python 3 from https://python.org")
        input("Press Enter to exit...")
        return
    
    # Check if required packages are installed
    try:
        import tkinter
        import pandas
    except ImportError as e:
        print(f"Missing required package: {e}")
        print("\nInstalling required packages...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
            print("✓ pandas installed successfully")
        except subprocess.CalledProcessError:
            print("✗ Failed to install pandas")
            print("Please run: pip install pandas")
            input("Press Enter to exit...")
            return
    
    # Run the main application
    try:
        print("Starting TCGPlayer Inventory Updater...")
        from tcg_inventory_updater import main as run_app
        run_app()
    except ImportError:
        print("Error: Could not find tcg_inventory_updater.py")
        print("Please make sure all files are in the same directory")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"Error starting application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
