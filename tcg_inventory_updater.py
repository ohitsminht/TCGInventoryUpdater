#!/usr/bin/env python3
"""
TCGPlayer Inventory Updater
Automates the process of updating TCGPlayer inventory quantities from secondary files.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext, simpledialog
import pandas as pd
import os
from typing import List, Dict, Tuple, Optional
import logging

class TCGInventoryUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("TCGPlayer Inventory Updater")
        self.root.geometry("800x600")
        
        # Ensure window is properly initialized
        self.root.update_idletasks()
        
        # Set initial window position (let Tkinter handle centering)
        self.root.geometry("800x600+100+100")
        
        # Data storage
        self.main_file_path = None
        self.secondary_files = []
        self.main_data = None
        self.secondary_data = []
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self.setup_ui()
        
        # Ensure proper focus after UI is set up
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="TCGPlayer Inventory Updater", 
                               font=('Arial', 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 30))
        
        # Main file selection
        ttk.Label(main_frame, text="Main Inventory File:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=10)
        self.main_file_var = tk.StringVar()
        main_file_entry = ttk.Entry(main_frame, textvariable=self.main_file_var, width=60, font=('Arial', 10))
        main_file_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 5))
        ttk.Button(main_frame, text="Browse", command=self.select_main_file, width=12).grid(row=1, column=2, padx=5)
        
        # Secondary files selection
        ttk.Label(main_frame, text="Secondary Files:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=(20, 10))
        
        # Secondary files listbox with scrollbar
        files_frame = ttk.Frame(main_frame)
        files_frame.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 10), padx=(10, 0))
        files_frame.columnconfigure(0, weight=1)
        
        self.secondary_files_listbox = tk.Listbox(files_frame, height=5, font=('Arial', 10))
        self.secondary_files_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        files_scrollbar = ttk.Scrollbar(files_frame, orient=tk.VERTICAL, command=self.secondary_files_listbox.yview)
        files_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.secondary_files_listbox.configure(yscrollcommand=files_scrollbar.set)
        
        files_frame.rowconfigure(0, weight=1)
        
        # Secondary files buttons
        files_buttons_frame = ttk.Frame(main_frame)
        files_buttons_frame.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=(0, 20), padx=(10, 0))
        
        ttk.Button(files_buttons_frame, text="Add Files", command=self.add_secondary_files, width=12).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(files_buttons_frame, text="Remove Selected", command=self.remove_secondary_file, width=15).grid(row=0, column=1, padx=5)
        ttk.Button(files_buttons_frame, text="Clear All", command=self.clear_secondary_files, width=12).grid(row=0, column=2, padx=5)
        
        
        # Action buttons
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=3, pady=30)
        
        self.preview_button = ttk.Button(buttons_frame, text="Preview Changes", command=self.preview_changes, width=20)
        self.preview_button.grid(row=0, column=0, padx=10)
        
        self.save_button = ttk.Button(buttons_frame, text="Save", command=self.save_inventory, width=20)
        self.save_button.grid(row=0, column=1, padx=10)
        
        ttk.Button(buttons_frame, text="Clear All", command=self.clear_all, width=20).grid(row=0, column=2, padx=10)
        
        # Log output
        log_frame = ttk.LabelFrame(main_frame, text="Log Output", padding="10")
        log_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=20)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=6, width=80, font=('Consolas', 9))
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure main frame row weights
        main_frame.rowconfigure(5, weight=1)
        
        
    def log_message(self, message):
        """Add a message to the log output"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        
    def select_main_file(self):
        """Select the main inventory file"""
        filename = filedialog.askopenfilename(
            title="Select Main Inventory File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            self.main_file_path = filename
            self.main_file_var.set(filename)
            self.log_message(f"Main file selected: {os.path.basename(filename)}")
            
    def add_secondary_files(self):
        """Add secondary files for inventory updates"""
        filenames = filedialog.askopenfilenames(
            title="Select Secondary Files",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        for filename in filenames:
            if filename not in self.secondary_files:
                self.secondary_files.append(filename)
                self.secondary_files_listbox.insert(tk.END, os.path.basename(filename))
                self.log_message(f"Secondary file added: {os.path.basename(filename)}")
                
    def remove_secondary_file(self):
        """Remove selected secondary file"""
        selection = self.secondary_files_listbox.curselection()
        if selection:
            index = selection[0]
            filename = self.secondary_files.pop(index)
            self.secondary_files_listbox.delete(index)
            self.log_message(f"Secondary file removed: {os.path.basename(filename)}")
            
    def clear_secondary_files(self):
        """Clear all secondary files"""
        self.secondary_files.clear()
        self.secondary_files_listbox.delete(0, tk.END)
        self.log_message("All secondary files cleared")
        
            
    def validate_inputs(self) -> bool:
        """Validate user inputs"""
        if not self.main_file_path or not os.path.exists(self.main_file_path):
            messagebox.showerror("Error", "Please select a valid main inventory file.")
            return False
            
        if not self.secondary_files:
            messagebox.showerror("Error", "Please add at least one secondary file.")
            return False
            
        for file_path in self.secondary_files:
            if not os.path.exists(file_path):
                messagebox.showerror("Error", f"Secondary file not found: {os.path.basename(file_path)}")
                return False
                
        return True
        
    def load_csv_data(self, file_path: str) -> Optional[pd.DataFrame]:
        """Load CSV data with error handling"""
        try:
            # Try different encodings
            encodings = ['utf-8', 'latin-1', 'cp1252']
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    return df
                except UnicodeDecodeError:
                    continue
                    
            # If all encodings fail, try with error handling
            df = pd.read_csv(file_path, encoding='utf-8', errors='ignore')
            return df
            
        except Exception as e:
            self.log_message(f"Error loading {os.path.basename(file_path)}: {str(e)}")
            return None
            
    def preview_changes(self):
        """Preview the changes that will be made"""
        if not self.validate_inputs():
            return
            
        try:
            self.log_message("Starting preview...")
            
            # Load main data
            self.main_data = self.load_csv_data(self.main_file_path)
            if self.main_data is None:
                messagebox.showerror("Error", "Failed to load main inventory file.")
                return
                
            # Load secondary data
            self.secondary_data = []
            for file_path in self.secondary_files:
                data = self.load_csv_data(file_path)
                if data is not None:
                    self.secondary_data.append(data)
                        
            if not self.secondary_data:
                messagebox.showerror("Error", "No secondary files could be loaded.")
                return
                    
            # Process changes
            changes = self.process_inventory_changes()
            
            if changes:
                self.log_message(f"Preview: {len(changes)} cards will be updated")
                for change in changes:  # Show all changes
                    self.log_message(f"  {change['product_name']} ({change['set_name']}, {change['condition']}) → {change['new_add_quantity']}")
            else:
                self.log_message("No changes found to apply.")
                
        except Exception as e:
            self.log_message(f"Error during preview: {str(e)}")
            messagebox.showerror("Error", f"Preview failed: {str(e)}")
            
    def process_inventory_changes(self) -> List[Dict]:
        """Process inventory changes and return list of changes"""
        changes = []
        
        # Fixed column names
        main_product_line = "Product Line"
        main_set_name = "Set Name"
        main_product_name = "Product Name"
        main_number = "Number"
        main_condition = "Condition"
        main_add_quantity = "Add to Quantity"
        
        secondary_product_line = "Product Line"
        secondary_set_name = "Set"
        secondary_product_name = "Product Name"
        secondary_number = "Number"
        secondary_condition = "Condition"
        secondary_quantity = "Quantity"
        
        # Aggregate quantities from secondary files
        aggregated_quantities = {}
        
        for secondary_df in self.secondary_data:
            try:
                for _, row in secondary_df.iterrows():
                    # Create a key for matching
                    card_key = (
                        str(row.get(secondary_product_line, '')).strip().lower(),
                        str(row.get(secondary_set_name, '')).strip().lower(),
                        str(row.get(secondary_product_name, '')).strip().lower(),
                        str(row.get(secondary_number, '')).strip().lower(),
                        str(row.get(secondary_condition, '')).strip().lower()
                    )
                    
                    # Get quantity
                    quantity = row.get(secondary_quantity, 0)
                    try:
                        quantity = int(float(quantity)) if pd.notna(quantity) else 0
                    except (ValueError, TypeError):
                        quantity = 0
                        
                    if quantity > 0 and card_key[0] and card_key[1] and card_key[2]:
                        if card_key not in aggregated_quantities:
                            aggregated_quantities[card_key] = 0
                        aggregated_quantities[card_key] += quantity
                        
            except Exception as e:
                self.log_message(f"Error processing secondary file: {str(e)}")
                continue
                    
        # Find matching rows in main data and calculate changes
        for _, main_row in self.main_data.iterrows():
            try:
                main_key = (
                    str(main_row.get(main_product_line, '')).strip().lower(),
                    str(main_row.get(main_set_name, '')).strip().lower(),
                    str(main_row.get(main_product_name, '')).strip().lower(),
                    str(main_row.get(main_number, '')).strip().lower(),
                    str(main_row.get(main_condition, '')).strip().lower()
                )
                
                if main_key in aggregated_quantities:
                    current_add_quantity = main_row.get(main_add_quantity, 0)
                    try:
                        current_add_quantity = int(float(current_add_quantity)) if pd.notna(current_add_quantity) else 0
                    except (ValueError, TypeError):
                        current_add_quantity = 0
                        
                    new_quantity = aggregated_quantities[main_key]
                    
                    changes.append({
                        'index': main_row.name,
                        'product_line': main_row.get(main_product_line, ''),
                        'set_name': main_row.get(main_set_name, ''),
                        'product_name': main_row.get(main_product_name, ''),
                        'number': main_row.get(main_number, ''),
                        'condition': main_row.get(main_condition, ''),
                        'current_add_quantity': current_add_quantity,
                        'new_add_quantity': new_quantity,
                        'change': new_quantity - current_add_quantity
                    })
                        
            except Exception as e:
                self.log_message(f"Error processing main row: {str(e)}")
                continue
                
        return changes
        
    def save_inventory(self):
        """Save the updated inventory"""
        if not self.validate_inputs():
            return
            
        try:
            # Load data if not already loaded
            if self.main_data is None:
                self.main_data = self.load_csv_data(self.main_file_path)
                if self.main_data is None:
                    messagebox.showerror("Error", "Failed to load main inventory file.")
                    return
                    
            if not self.secondary_data:
                for file_path in self.secondary_files:
                    data = self.load_csv_data(file_path)
                    if data is not None:
                        self.secondary_data.append(data)
                            
            if not self.secondary_data:
                messagebox.showerror("Error", "No secondary files could be loaded.")
                return
                    
            # Process changes
            changes = self.process_inventory_changes()
            
            if not changes:
                self.log_message("No changes to apply.")
                return
                    
            # Apply changes
            updated_count = 0
            for change in changes:
                self.main_data.at[change['index'], "Add to Quantity"] = change['new_add_quantity']
                updated_count += 1
                    
            # Get output filename using file dialog
            default_name = os.path.basename(self.main_file_path)
            output_path = filedialog.asksaveasfilename(
                title="Save Updated Inventory As",
                defaultextension=".csv",
                initialfile=default_name,
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
            )
            
            if not output_path:
                return
                
            # Save file
            self.main_data.to_csv(output_path, index=False)
            
            self.log_message(f"Saved: {updated_count} cards updated to {output_path}")
            messagebox.showinfo("Success", f"Inventory updated successfully!\n{updated_count} cards updated.")
            
                
        except Exception as e:
            self.log_message(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Save failed: {str(e)}")
            
    def clear_all(self):
        """Clear all data and reset the interface"""
        self.main_file_path = None
        self.secondary_files = []
        self.main_data = None
        self.secondary_data = []
        
        self.main_file_var.set("")
        self.secondary_files_listbox.delete(0, tk.END)
        self.log_text.delete(1.0, tk.END)
        
        self.log_message("Application reset. Ready for new files.")

def main():
    root = tk.Tk()
    app = TCGInventoryUpdater(root)
    root.mainloop()

if __name__ == "__main__":
    main()
