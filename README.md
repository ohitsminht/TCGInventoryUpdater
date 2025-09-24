# TCGPlayer Inventory Updater

A Python application that automates the process of updating TCGPlayer inventory quantities from secondary files.

## Features

- **GUI Interface**: Easy-to-use Tkinter-based graphical interface with responsive threading
- **CSV Processing**: Handles CSV files with automatic encoding detection and optimized loading
- **Smart Matching**: Matches cards by Product Line, Set Name, Product Name, Number, and Condition
- **Quantity Aggregation**: Automatically sums quantities for duplicate cards across multiple files
- **Flexible Output**: Save as new file or overwrite original
- **Preview Mode**: Preview changes before applying them
- **Performance Optimized**: Multi-threaded processing prevents UI freezing
- **Cancellation Support**: Cancel long-running operations at any time
- **Real-time Progress**: Live progress updates and status messages
- **Error Handling**: Comprehensive error handling and logging

## Installation

1. Install Python 3.7 or higher
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python tcg_inventory_updater.py
   ```

2. **Select Main File**: Choose your main TCGPlayer inventory CSV file
3. **Add Secondary Files**: Add one or more CSV files containing the quantities to add
4. **Preview Changes**: Click "Preview Changes" to see what will be updated
5. **Save**: Click "Save" to apply changes and choose where to save the updated file

## How It Works

1. **File Loading**: The application loads your main inventory file and all secondary files
2. **Card Matching**: For each card in secondary files, it finds the matching card in the main file by comparing:
   - Product Line
   - Set Name
   - Product Name
   - Number
   - Condition
3. **Quantity Aggregation**: If multiple entries exist for the same card, quantities are summed together
4. **Update Process**: The matched cards in the main file have their "Add to Quantity" values updated
5. **File Saving**: The updated inventory is saved to a new file with a name you choose

## CSV File Format

Your CSV files should contain columns for:

**Main File:**
- **Product Line**: The product line (e.g., "Magic")
- **Set Name**: The set the card belongs to
- **Product Name**: The name of the trading card
- **Number**: The card number
- **Condition**: The condition of the card (e.g., "Near Mint", "Lightly Played")
- **Add to Quantity**: The quantity to add (will be updated)

**Secondary Files:**
- **Product Line**: The product line (e.g., "Magic")
- **Set**: The set the card belongs to
- **Product Name**: The name of the trading card
- **Number**: The card number
- **Condition**: The condition of the card
- **Quantity**: The number of cards to add (should be numeric)

Example CSV structure:

**Main Inventory File:**
```csv
Product Line,Set Name,Product Name,Number,Condition,Add to Quantity,Price
Magic,Magic 2011,Lightning Bolt,1,Near Mint,4,0.25
Magic,Magic 2011,Lightning Bolt,1,Lightly Played,2,0.15
Magic,Alpha,Black Lotus,1,Near Mint,1,15000.00
```

**Secondary Files:**
```csv
Product Line,Set,Product Name,Number,Condition,Quantity
Magic,Magic 2011,Lightning Bolt,1,Near Mint,3
Magic,Magic 2011,Lightning Bolt,1,Lightly Played,2
Magic,Alpha,Black Lotus,1,Near Mint,1
```

## Sample Files

The repository includes sample CSV files for testing:
- `sample_main_inventory.csv`: Example main inventory file
- `sample_addition1.csv`: Example secondary file with additions
- `sample_addition2.csv`: Another example secondary file

## Error Handling

The application includes comprehensive error handling for:
- Invalid file paths
- Missing columns
- Encoding issues
- Data type errors
- File permission problems

All errors are logged to the application's log output area.

## Tips

- Use "Preview Changes" before updating to verify the changes look correct
- Make sure your CSV files have consistent column names
- The application is case-insensitive when matching card names and sets
- Empty or invalid quantities are treated as 0
