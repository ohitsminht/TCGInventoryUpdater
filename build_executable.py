#!/usr/bin/env python3
"""
Build script for creating executable files using PyInstaller
"""

import os
import sys
import subprocess
import platform

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """Build the executable using PyInstaller"""
    install_pyinstaller()
    
    # Get the current platform
    current_platform = platform.system().lower()
    
    # Basic PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=TCGInventoryUpdater",
        "--add-data=sample_main_inventory.csv:.",
        "--add-data=sample_addition1.csv:.",
        "--add-data=sample_addition2.csv:.",
        "--add-data=README.md:.",
        "tcg_inventory_updater.py"
    ]
    
    # Add platform-specific options
    if current_platform == "darwin":  # macOS
        # Create a proper macOS app bundle
        cmd = [
            "pyinstaller",
            "--onedir",
            "--windowed",
            "--name=TCGInventoryUpdater",
            "--add-data=sample_main_inventory.csv:.",
            "--add-data=sample_addition1.csv:.",
            "--add-data=sample_addition2.csv:.",
            "--add-data=README.md:.",
            "--osx-bundle-identifier=com.tcginventoryupdater.app",
            "tcg_inventory_updater.py"
        ]
    elif current_platform == "windows":
        # Remove version file requirement for Windows
        pass
    
    print(f"Building executable for {current_platform}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print("Build completed successfully!")
        
        # Move the executable to a more accessible location
        if current_platform == "darwin":
            # For onedir builds, we get a .app bundle
            source = "dist/TCGInventoryUpdater.app"
            dest = "TCGInventoryUpdater-macOS.app"
        elif current_platform == "windows":
            source = "dist/TCGInventoryUpdater.exe"
            dest = "TCGInventoryUpdater-Windows.exe"
        else:
            source = "dist/TCGInventoryUpdater"
            dest = f"TCGInventoryUpdater-{current_platform}"
            
        if os.path.exists(source):
            os.rename(source, dest)
            # Make the file executable on Unix-like systems (macOS/Linux)
            if current_platform in ["darwin", "linux"]:
                os.chmod(dest, 0o755)  # rwxr-xr-x permissions
            print(f"Executable saved as: {dest}")
        
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = build_executable()
    if success:
        print("\nBuild completed successfully!")
        print("The executable is ready for distribution.")
    else:
        print("\nBuild failed!")
        sys.exit(1)