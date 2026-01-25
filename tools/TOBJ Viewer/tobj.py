import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import struct
import os

class TOBJViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("TOBJ Viewer")
        
        # Fixed window size that fits all information perfectly
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.center_window(600, 400)
        
        self.current_file = None
        self.file_data = None
        self.original_data = None
        
        self.create_menu()
        self.create_widgets()
        
    def center_window(self, width, height):
        """Center the window on the screen"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # About menu
        about_menu = tk.Menu(menubar, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="About", menu=about_menu)
        
        self.root.config(menu=menubar)
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label for file path
        self.path_label = ttk.Label(main_frame, text="File path: not selected")
        self.path_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Text entry for editing path
        self.path_entry = ttk.Entry(main_frame, width=70)
        self.path_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Cancel button
        self.cancel_button = ttk.Button(button_frame, text="Cancel", command=self.cancel_edits)
        self.cancel_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Save button
        self.save_button = ttk.Button(button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT)
        self.save_button.state(['disabled'])
        
        # File information frame
        info_frame = ttk.LabelFrame(main_frame, text="File Information", padding="5")
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text widget with fixed size to fit all information
        self.info_text = tk.Text(info_frame, wrap=tk.WORD, width=70, height=18, font=("Courier New", 9))
        self.info_text.pack(fill=tk.BOTH, expand=True)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Open TOBJ File",
            filetypes=[("TOBJ files", "*.tobj"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.current_file = file_path
                self.load_tobj_file(file_path)
                self.save_button.state(['!disabled'])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")
    
    def load_tobj_file(self, file_path):
        """Load and parse TOBJ file"""
        with open(file_path, 'rb') as file:
            self.original_data = file.read()
            self.file_data = bytearray(self.original_data)
        
        # Parse TOBJ structure
        parsed_info = self.parse_tobj_structure(self.file_data)
        
        # Update interface
        self.path_label.config(text=f"File path: {os.path.basename(file_path)}")
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, parsed_info['path'])
        
        # Display file information
        self.display_file_info(parsed_info)
    
    def parse_tobj_structure(self, data):
        """Parse TOBJ structure according to 010 Editor template"""
        result = {}
        
        try:
            offset = 0
            
            # Read unknown 40 bytes
            result['unknown_bytes'] = data[offset:offset + 40]
            offset += 40
            
            # Read path length (uint)
            if offset + 4 <= len(data):
                result['path_length'] = struct.unpack('<I', data[offset:offset + 4])[0]
                offset += 4
            else:
                raise ValueError("Not enough data to read path length")
            
            # Read null terminator (uint)
            if offset + 4 <= len(data):
                result['null_terminator'] = struct.unpack('<I', data[offset:offset + 4])[0]
                offset += 4
            else:
                raise ValueError("Not enough data to read null terminator")
            
            # Read path
            if offset + result['path_length'] <= len(data):
                result['path'] = data[offset:offset + result['path_length']].decode('utf-8', errors='replace')
                offset += result['path_length']
            else:
                raise ValueError("Not enough data to read path")
            
            # Remaining data (if any)
            if offset < len(data):
                result['remaining_data'] = data[offset:]
            else:
                result['remaining_data'] = b''
                
            result['total_size'] = len(data)
            result['parsed_size'] = offset
            
        except Exception as e:
            raise ValueError(f"Error parsing TOBJ structure: {str(e)}")
        
        return result
    
    def display_file_info(self, file_info):
        """Display file information"""
        info_text = f"""TOBJ File Information

File size: {file_info['total_size']} bytes
Parsed structure size: {file_info['parsed_size']} bytes

File structure:
- Unknown data: 40 bytes
- Path length: {file_info['path_length']}
- Null terminator: {file_info['null_terminator']:08X}
- File path: {file_info['path']}"""

        if file_info['remaining_data']:
            info_text += f"\nAdditional data: {len(file_info['remaining_data'])} bytes"
        
        # Hex dump of unknown bytes
        info_text += "\n\nHex dump of unknown bytes:\n"
        info_text += self.hex_dump(file_info['unknown_bytes'])
        
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, info_text)
    
    def hex_dump(self, data, width=16):
        """Create hex dump of data"""
        result = ""
        for i in range(0, len(data), width):
            hex_part = ' '.join(f'{b:02x}' for b in data[i:i+width])
            ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data[i:i+width])
            result += f'{i:04x}: {hex_part:<48} {ascii_part}\n'
        return result
    
    def save_file(self):
        if not self.current_file:
            messagebox.showwarning("Warning", "No file open for saving")
            return
        
        try:
            # Get new path from text entry
            new_path = self.path_entry.get().encode('utf-8')
            new_path_length = len(new_path)
            
            # Update file data
            updated_data = self.update_tobj_data(new_path, new_path_length)
            
            # Save file
            with open(self.current_file, 'wb') as file:
                file.write(updated_data)
            
            # Update original data
            self.original_data = updated_data
            self.file_data = bytearray(updated_data)
            
            messagebox.showinfo("Success", "File saved successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def update_tobj_data(self, new_path, new_path_length):
        """Update TOBJ data with new path"""
        # Create copy of original data
        updated_data = bytearray(self.original_data)
        
        # Update path length (position 40)
        updated_data[40:44] = struct.pack('<I', new_path_length)
        
        # Update path (position 48)
        path_offset = 48
        if path_offset + new_path_length <= len(updated_data):
            updated_data[path_offset:path_offset + new_path_length] = new_path
        else:
            # If new path is longer, rebuild the file
            updated_data = self.rebuild_tobj_file(new_path, new_path_length)
        
        return bytes(updated_data)
    
    def rebuild_tobj_file(self, new_path, new_path_length):
        """Rebuild TOBJ file with new path"""
        # Base data (first 48 bytes)
        base_data = self.original_data[:48]
        
        # Update path length
        base_data = base_data[:40] + struct.pack('<I', new_path_length) + base_data[44:48]
        
        # Build new file
        new_data = base_data + new_path
        
        # Add remaining data if any exists
        old_path_length = struct.unpack('<I', self.original_data[40:44])[0]
        remaining_offset = 48 + old_path_length
        if remaining_offset < len(self.original_data):
            new_data += self.original_data[remaining_offset:]
        
        return new_data
    
    def cancel_edits(self):
        """Cancel changes and restore original data"""
        if self.current_file and self.original_data:
            try:
                self.load_tobj_file(self.current_file)
                messagebox.showinfo("Cancel", "Changes cancelled")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to cancel changes: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No file open")
    
    def show_about(self):
        about_text = """TOBJ Viewer v1.0

Author: Adyusha
Version: 1.0
Created: 2025

Program for viewing and editing TOBJ files."""
        
        messagebox.showinfo("About", about_text)

def main():
    root = tk.Tk()
    app = TOBJViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
