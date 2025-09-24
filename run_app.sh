#!/bin/bash

# TCGPlayer Inventory Updater Launcher Script

echo "Starting TCGPlayer Inventory Updater..."

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if pandas is installed
$PYTHON_CMD -c "import pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required dependencies..."
    $PYTHON_CMD -m pip install pandas --user
fi

# Run the application
echo "Launching application..."
$PYTHON_CMD tcg_inventory_updater.py

echo "Application closed."
