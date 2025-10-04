"""
main_app.py
Main Application Window for Encryption Image Information Concealing System (EIICS)
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import os
import glob

# Import from current directory
from crypto_engine import CryptoEngine
from stego_engine import StegoEngine
from help_content import HelpContent

class EIICSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EIICS - Encryption Image Information Concealing System")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0a1929")
        
        # Create main container
        self.main_frame = tk.Frame(root, bg="#0a1929")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.default_images = self.load_default_images()
        self.create_menu_bar()
        self.show_welcome_screen()
        self.center_window()

    def load_default_images(self):
        """Load default images from default_images folder"""
        default_images = []
        try:
            image_files = glob.glob("default_images/*.png") + glob.glob("default_images/*.jpg") + glob.glob("default_images/*.jpeg")
            for img_path in image_files:
                default_images.append(img_path)
            print(f"Loaded {len(default_images)} default images")
        except Exception as e:
            print(f"Error loading default images: {e}")
        return default_images

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_menu_bar(self):
        """Create professional menu bar"""
        menubar = tk.Menu(self.root, bg="#132f4c", fg="#ffffff", activebackground="#00e5ff")
        
        # Navigation menu
        nav_menu = tk.Menu(menubar, tearoff=0, bg="#132f4c", fg="#ffffff", activebackground="#00e5ff")
        nav_menu.add_command(label="Home", command=self.show_welcome_screen)
        nav_menu.add_separator()
        nav_menu.add_command(label="Embed Text", command=self.show_text_embed)
        nav_menu.add_command(label="Embed File", command=self.show_file_embed)
        nav_menu.add_command(label="Extract Data", command=self.show_extract)
        menubar.add_cascade(label="Navigation", menu=nav_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0, bg="#132f4c", fg="#ffffff", activebackground="#00e5ff")
        help_menu.add_command(label="User Guide", command=self.show_help)
        help_menu.add_command(label="Pro Tips", command=self.show_tips)
        help_menu.add_separator()
        help_menu.add_command(label="About EIICS", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)

    def clear_main_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        """Show welcome screen"""
        self.clear_main_frame()
        self.root.title("EIICS - Encryption Image Information Concealing System")
        
        main_frame = tk.Frame(self.main_frame, bg="#132f4c")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

        # Title
        title_label = tk.Label(main_frame, text="EIICS", 
                               fg="#00e5ff", bg="#132f4c",
                               font=('Arial', 36, 'bold'))
        title_label.pack(pady=(40, 10))

        subtitle_label = tk.Label(main_frame, 
                                  text="Encryption Image Information Concealing System",
                                  fg="#b0bec5", bg="#132f4c",
                                  font=('Arial', 14))
        subtitle_label.pack(pady=(0, 50))

        # Action buttons
        btn_frame = tk.Frame(main_frame, bg="#132f4c")
        btn_frame.pack(pady=30)

        # Text embedding button
        text_btn = tk.Button(btn_frame, text="📝 Embed Text", 
                             command=self.show_text_embed,
                             bg="#00e5ff", fg="#ffffff",
                             font=('Arial', 12, 'bold'),
                             padx=30, pady=15, width=20)
        text_btn.pack(pady=15, padx=20, fill=tk.X)
        self.add_button_hover(text_btn, "#00e5ff", "#00b8d4")

        # File embedding button
        file_btn = tk.Button(btn_frame, text="📁 Embed File", 
                             command=self.show_file_embed,
                             bg="#ff6e40", fg="#ffffff",
                             font=('Arial', 12, 'bold'),
                             padx=30, pady=15, width=20)
        file_btn.pack(pady=15, padx=20, fill=tk.X)
        self.add_button_hover(file_btn, "#ff6e40", "#ff5722")

        # Extraction button
        extract_btn = tk.Button(btn_frame, text="🔍 Extract Data", 
                                command=self.show_extract,
                                bg="#4caf50", fg="#ffffff",
                                font=('Arial', 12, 'bold'),
                                padx=30, pady=15, width=20)
        extract_btn.pack(pady=15, padx=20, fill=tk.X)
        self.add_button_hover(extract_btn, "#4caf50", "#45a049")

        # Footer
        footer_label = tk.Label(main_frame, 
                               text="© 2024 EIICS • Secure Data Hiding",
                               fg="#b0bec5", bg="#132f4c",
                               font=('Arial', 10))
        footer_label.pack(side=tk.BOTTOM, pady=20)

    def show_text_embed(self):
        """Show text embedding screen"""
        self.clear_main_frame()
        self.root.title("EIICS - Embed Text")
        
        # Create a simple form
        main_frame = tk.Frame(self.main_frame, bg="#132f4c")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header with back button
        header_frame = tk.Frame(main_frame, bg="#132f4c")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        back_btn = tk.Button(header_frame, text="← Back to Home", 
                           command=self.show_welcome_screen,
                           bg="#607d8b", fg="#ffffff",
                           font=('Arial', 10))
        back_btn.pack(side=tk.LEFT)
        self.add_button_hover(back_btn, "#607d8b", "#546e7a")

        title_label = tk.Label(header_frame, text="Embed Text Data", 
                               fg="#00e5ff", bg="#132f4c",
                               font=('Arial', 20, 'bold'))
        title_label.pack(side=tk.LEFT, padx=20)

        # Store variables as instance attributes
        self.current_image_path = None
        self.encryption_key = tk.StringVar()

        # Image selection with default images
        tk.Label(main_frame, text="1. Select Cover Image (Optional - defaults available below)", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        # Upload button
        upload_btn = tk.Button(main_frame, text="📁 Upload Custom Image", 
                  command=self.select_image, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 10))
        upload_btn.pack(pady=(0, 10), padx=20)
        self.add_button_hover(upload_btn, "#00e5ff", "#00b8d4")
        
        # Selected image label
        self.selected_image_label = tk.Label(main_frame, text="No image selected", 
                                           fg="#b0bec5", bg="#132f4c",
                                           font=('Arial', 10, 'italic'))
        self.selected_image_label.pack(pady=(0, 10), padx=20)

        # Default images gallery
        tk.Label(main_frame, text="Or choose from default images:", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 11, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        default_frame = tk.Frame(main_frame, bg="#132f4c")
        default_frame.pack(fill=tk.X, pady=(0, 20), padx=20)
        
        if self.default_images:
            for i, img_path in enumerate(self.default_images[:5]):
                img_name = os.path.basename(img_path)
                btn = tk.Button(default_frame, text=f"🖼️ {img_name}", 
                              command=lambda path=img_path: self.use_default_image(path),
                              bg="#4fc3f7", fg="#ffffff",
                              font=('Arial', 9),
                              padx=10, pady=5)
                btn.pack(side=tk.LEFT, padx=5)
                self.add_button_hover(btn, "#4fc3f7", "#29b6f6")
        else:
            tk.Label(default_frame, text="No default images available", 
                   fg="#b0bec5", bg="#132f4c",
                   font=('Arial', 10, 'italic')).pack()

        # Text input
        tk.Label(main_frame, text="2. Enter Secret Text", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        self.text_input = scrolledtext.ScrolledText(main_frame, height=8,
                                                   bg="#132f4c", fg="#ffffff",
                                                   insertbackground="#00e5ff")
        self.text_input.pack(pady=(0, 15), padx=20, fill=tk.BOTH, expand=True)

        # Key input
        tk.Label(main_frame, text="3. Encryption Key", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        key_entry = tk.Entry(main_frame, textvariable=self.encryption_key, 
                             font=('Arial', 12), show="•", bg="#132f4c", fg="#ffffff")
        key_entry.pack(pady=(0, 20), padx=20, fill=tk.X)

        # Buttons
        btn_frame = tk.Frame(main_frame, bg="#132f4c")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="🚀 Embed Text", 
                  command=self.embed_text, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 12, 'bold'), padx=20, pady=10).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="❌ Cancel", 
                  command=self.show_welcome_screen, 
                  bg="#ff6e40", fg="#ffffff",
                  font=('Arial', 12), padx=20, pady=10).pack(side=tk.LEFT, padx=10)

    def use_default_image(self, image_path):
        """Use a default image"""
        self.current_image_path = image_path
        img_name = os.path.basename(image_path)
        self.selected_image_label.config(text=f"Selected: {img_name} (Default)")
        messagebox.showinfo("Success", f"Using default image: {img_name}")

    def select_image(self):
        """Select cover image"""
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if path:
            self.current_image_path = path
            img_name = os.path.basename(path)
            self.selected_image_label.config(text=f"Selected: {img_name}")
            messagebox.showinfo("Success", f"Selected: {img_name}")

    def embed_text(self):
        """Embed text into image"""
        text_data = self.text_input.get("1.0", tk.END).strip()
        if not text_data:
            messagebox.showerror("Error", "Please enter text to hide")
            return
        
        # Use default image if none selected
        if not self.current_image_path and self.default_images:
            self.current_image_path = self.default_images[0]
            img_name = os.path.basename(self.current_image_path)
            messagebox.showinfo("Info", f"Using default image: {img_name}")
        
        if not self.current_image_path:
            messagebox.showerror("Error", "Please select a cover image or use a default image")
            return
        
        if not self.encryption_key.get():
            messagebox.showerror("Error", "Please enter an encryption key")
            return

        try:
            # Encrypt the text
            encrypted_data = CryptoEngine.encrypt_data(text_data.encode('utf-8'), self.encryption_key.get())
            
            # Save output
            output_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            
            if output_path:
                # Embed the data
                StegoEngine.embed_data(
                    self.current_image_path, 
                    encrypted_data.encode('utf-8'), 
                    'text', 
                    output_path
                )
                
                messagebox.showinfo("Success", 
                                  f"Text embedded successfully!\n\n"
                                  f"Saved to: {output_path}\n\n"
                                  "Keep your key safe - it's required for extraction!")
                self.show_welcome_screen()
                
        except Exception as e:
            messagebox.showerror("Error", f"Embedding failed: {str(e)}")

    def show_file_embed(self):
        """Show file embedding screen"""
        self.clear_main_frame()
        self.root.title("EIICS - Embed File")
        
        # Similar simple implementation as text embed
        main_frame = tk.Frame(self.main_frame, bg="#132f4c")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header with back button
        header_frame = tk.Frame(main_frame, bg="#132f4c")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        back_btn = tk.Button(header_frame, text="← Back to Home", 
                           command=self.show_welcome_screen,
                           bg="#607d8b", fg="#ffffff",
                           font=('Arial', 10))
        back_btn.pack(side=tk.LEFT)
        self.add_button_hover(back_btn, "#607d8b", "#546e7a")

        title_label = tk.Label(header_frame, text="Embed File Data", 
                               fg="#00e5ff", bg="#132f4c",
                               font=('Arial', 20, 'bold'))
        title_label.pack(side=tk.LEFT, padx=20)

        # Store variables
        self.current_image_path = None
        self.selected_file_path = None
        self.encryption_key = tk.StringVar()

        # Image selection with default images
        tk.Label(main_frame, text="1. Select Cover Image (Optional - defaults available below)", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        # Upload button
        upload_btn = tk.Button(main_frame, text="📁 Upload Custom Image", 
                  command=self.select_image, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 10))
        upload_btn.pack(pady=(0, 10), padx=20)
        self.add_button_hover(upload_btn, "#00e5ff", "#00b8d4")
        
        # Selected image label
        self.selected_image_label = tk.Label(main_frame, text="No image selected", 
                                           fg="#b0bec5", bg="#132f4c",
                                           font=('Arial', 10, 'italic'))
        self.selected_image_label.pack(pady=(0, 10), padx=20)

        # Default images gallery
        tk.Label(main_frame, text="Or choose from default images:", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 11, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        default_frame = tk.Frame(main_frame, bg="#132f4c")
        default_frame.pack(fill=tk.X, pady=(0, 20), padx=20)
        
        if self.default_images:
            for i, img_path in enumerate(self.default_images[:5]):
                img_name = os.path.basename(img_path)
                btn = tk.Button(default_frame, text=f"🖼️ {img_name}", 
                              command=lambda path=img_path: self.use_default_image(path),
                              bg="#4fc3f7", fg="#ffffff",
                              font=('Arial', 9),
                              padx=10, pady=5)
                btn.pack(side=tk.LEFT, padx=5)
                self.add_button_hover(btn, "#4fc3f7", "#29b6f6")
        else:
            tk.Label(default_frame, text="No default images available", 
                   fg="#b0bec5", bg="#132f4c",
                   font=('Arial', 10, 'italic')).pack()

        # File selection
        tk.Label(main_frame, text="2. Select File to Hide", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        tk.Button(main_frame, text="📂 Choose File", 
                  command=self.select_file, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 10)).pack(pady=(0, 15), padx=20)

        # File selection label
        self.selected_file_label = tk.Label(main_frame, text="No file selected", 
                                          fg="#b0bec5", bg="#132f4c",
                                          font=('Arial', 10, 'italic'))
        self.selected_file_label.pack(pady=(0, 10), padx=20)

        # Key input
        tk.Label(main_frame, text="3. Encryption Key", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        key_entry = tk.Entry(main_frame, textvariable=self.encryption_key, 
                             font=('Arial', 12), show="•", bg="#132f4c", fg="#ffffff")
        key_entry.pack(pady=(0, 20), padx=20, fill=tk.X)

        # Buttons
        btn_frame = tk.Frame(main_frame, bg="#132f4c")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="🚀 Embed File", 
                  command=self.embed_file, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 12, 'bold'), padx=20, pady=10).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="❌ Cancel", 
                  command=self.show_welcome_screen, 
                  bg="#ff6e40", fg="#ffffff",
                  font=('Arial', 12), padx=20, pady=10).pack(side=tk.LEFT, padx=10)

    def select_file(self):
        """Select file to hide"""
        path = filedialog.askopenfilename(title="Select File to Hide")
        if path:
            self.selected_file_path = path
            file_name = os.path.basename(path)
            self.selected_file_label.config(text=f"Selected: {file_name}")
            messagebox.showinfo("Success", f"File selected: {file_name}")

    def embed_file(self):
        """Embed file into image"""
        if not self.selected_file_path:
            messagebox.showerror("Error", "Please select a file to hide")
            return
        
        # Use default image if none selected
        if not self.current_image_path and self.default_images:
            self.current_image_path = self.default_images[0]
            img_name = os.path.basename(self.current_image_path)
            messagebox.showinfo("Info", f"Using default image: {img_name}")
        
        if not self.current_image_path:
            messagebox.showerror("Error", "Please select a cover image or use a default image")
            return
        
        if not self.encryption_key.get():
            messagebox.showerror("Error", "Please enter an encryption key")
            return

        try:
            # Read file content
            with open(self.selected_file_path, 'rb') as f:
                file_data = f.read()
            
            # Encrypt the file data
            encrypted_data = CryptoEngine.encrypt_data(file_data, self.encryption_key.get())
            
            # Save output
            output_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            
            if output_path:
                # Embed the data
                StegoEngine.embed_data(
                    self.current_image_path, 
                    encrypted_data.encode('utf-8'), 
                    'file', 
                    output_path
                )
                
                messagebox.showinfo("Success", 
                                  f"File embedded successfully!\n\n"
                                  f"Saved to: {output_path}\n\n"
                                  "Keep your key safe - it's required for extraction!")
                self.show_welcome_screen()
                
        except Exception as e:
            messagebox.showerror("Error", f"Embedding failed: {str(e)}")

    def show_extract(self):
        """Show extraction screen"""
        self.clear_main_frame()
        self.root.title("EIICS - Extract Data")
        
        main_frame = tk.Frame(self.main_frame, bg="#132f4c")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header with back button
        header_frame = tk.Frame(main_frame, bg="#132f4c")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        back_btn = tk.Button(header_frame, text="← Back to Home", 
                           command=self.show_welcome_screen,
                           bg="#607d8b", fg="#ffffff",
                           font=('Arial', 10))
        back_btn.pack(side=tk.LEFT)
        self.add_button_hover(back_btn, "#607d8b", "#546e7a")

        title_label = tk.Label(header_frame, text="Extract Hidden Data", 
                               fg="#00e5ff", bg="#132f4c",
                               font=('Arial', 20, 'bold'))
        title_label.pack(side=tk.LEFT, padx=20)

        # Store variables
        self.stego_image_path = None
        self.encryption_key = tk.StringVar()
        self.extracted_data = None
        self.data_type = None

        # Image selection
        tk.Label(main_frame, text="1. Select Stego Image", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        tk.Button(main_frame, text="📁 Browse Image", 
                  command=self.select_extract_image, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 10)).pack(pady=(0, 20), padx=20)

        # Selected image label for extraction
        self.selected_extract_image_label = tk.Label(main_frame, text="No image selected", 
                                                   fg="#b0bec5", bg="#132f4c",
                                                   font=('Arial', 10, 'italic'))
        self.selected_extract_image_label.pack(pady=(0, 10), padx=20)

        # Key input
        tk.Label(main_frame, text="2. Decryption Key", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10, 5), padx=20)

        key_entry = tk.Entry(main_frame, textvariable=self.encryption_key, 
                             font=('Arial', 12), show="•", bg="#132f4c", fg="#ffffff")
        key_entry.pack(pady=(0, 20), padx=20, fill=tk.X)

        # Extract button
        tk.Button(main_frame, text="🔓 Extract Data", 
                  command=self.extract_data, bg="#00e5ff", fg="#ffffff",
                  font=('Arial', 12, 'bold'), padx=20, pady=10).pack(pady=20)

        # Result area
        result_frame = tk.Frame(main_frame, bg="#132f4c")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        tk.Label(result_frame, text="3. Extracted Data", 
                 fg="#00e5ff", bg="#132f4c",
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=(0, 5), padx=20)

        self.result_text = scrolledtext.ScrolledText(result_frame, height=10,
                                                   bg="#132f4c", fg="#ffffff",
                                                   insertbackground="#00e5ff")
        self.result_text.pack(pady=(0, 10), padx=20, fill=tk.BOTH, expand=True)
        self.result_text.config(state=tk.DISABLED)

        # Save button
        self.save_button = tk.Button(main_frame, text="💾 Save Extracted File", 
                                    command=self.save_file, bg="#4caf50", fg="#ffffff",
                                    font=('Arial', 12, 'bold'), padx=20, pady=10,
                                    state=tk.DISABLED)
        # Initially hidden
        self.save_button.pack_forget()

    def select_extract_image(self):
        """Select stego image for extraction"""
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if path:
            self.stego_image_path = path
            img_name = os.path.basename(path)
            self.selected_extract_image_label.config(text=f"Selected: {img_name}")
            messagebox.showinfo("Success", f"Selected: {img_name}")

    def extract_data(self):
        """Extract data from stego image"""
        if not self.stego_image_path:
            messagebox.showerror("Error", "Please select a stego image")
            return
        
        if not self.encryption_key.get():
            messagebox.showerror("Error", "Please enter a decryption key")
            return

        try:
            # Extract and decrypt data
            self.data_type, extracted_data = StegoEngine.extract_data(self.stego_image_path)
            self.extracted_data = CryptoEngine.decrypt_data(extracted_data.decode('utf-8'), self.encryption_key.get())
            
            # Display results
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            
            if self.data_type == 'text':
                self.result_text.insert("1.0", self.extracted_data.decode('utf-8'))
                messagebox.showinfo("Success", "Text extracted successfully!")
                # Hide save button for text
                self.save_button.pack_forget()
            else:
                # For files, show info and enable save button
                self.result_text.insert("1.0", 
                    f"File data extracted successfully!\n\n"
                    f"File type: Binary data\n"
                    f"Size: {len(self.extracted_data)} bytes\n\n"
                    f"Click 'Save Extracted File' button to save the file."
                )
                messagebox.showinfo("Success", "File data extracted successfully!")
                
                # Show and enable save button
                self.save_button.pack(pady=(0, 10))
                self.save_button.config(state=tk.NORMAL)
            
            self.result_text.config(state=tk.DISABLED)
                
        except Exception as e:
            messagebox.showerror("Error", f"Extraction failed: {str(e)}")
            self.save_button.pack_forget()

    def save_file(self):
        """Save extracted file to disk"""
        if not self.extracted_data or self.data_type != 'file':
            messagebox.showerror("Error", "No file data to save")
            return

        try:
            # Ask user where to save the file
            file_path = filedialog.asksaveasfilename(
                title="Save Extracted File",
                defaultextension=".*",
                filetypes=[("All files", "*.*")]
            )
            
            if file_path:
                # Write the binary data to file
                with open(file_path, 'wb') as f:
                    f.write(self.extracted_data)
                
                messagebox.showinfo("Success", 
                                  f"File saved successfully!\n\n"
                                  f"Location: {file_path}\n"
                                  f"Size: {len(self.extracted_data)} bytes")
                
                # Disable save button after successful save
                self.save_button.config(state=tk.DISABLED)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def show_help(self):
        """Show help dialog"""
        self.show_scrolled_dialog(HelpContent.HELP_TITLE, HelpContent.HELP_TEXT)

    def show_tips(self):
        """Show tips dialog"""
        self.show_scrolled_dialog(HelpContent.TIPS_TITLE, HelpContent.TIPS_TEXT)

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(HelpContent.ABOUT_TITLE, HelpContent.ABOUT_TEXT)

    def show_scrolled_dialog(self, title, content):
        """Show a dialog with scrolled text for longer content"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("700x500")
        dialog.configure(bg="#0a1929")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (700 // 2)
        y = (dialog.winfo_screenheight() // 2) - (500 // 2)
        dialog.geometry(f"700x500+{x}+{y}")
        
        # Main frame
        main_frame = tk.Frame(dialog, bg="#132f4c")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text=title, 
                             fg="#00e5ff", bg="#132f4c",
                             font=('Arial', 16, 'bold'))
        title_label.pack(pady=(10, 20))
        
        # Scrolled text
        text_widget = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD,
                                                 bg="#132f4c", fg="#ffffff",
                                                 font=('Arial', 11),
                                                 padx=10, pady=10)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        text_widget.insert('1.0', content)
        text_widget.config(state=tk.DISABLED)
        
        # Close button
        close_btn = tk.Button(main_frame, text="Close", 
                            command=dialog.destroy,
                            bg="#00e5ff", fg="#ffffff",
                            font=('Arial', 10, 'bold'),
                            padx=20, pady=5)
        close_btn.pack(pady=10)
        
        self.add_button_hover(close_btn, "#00e5ff", "#00b8d4")

    def add_button_hover(self, button, normal_color, hover_color):
        """Add hover effects to buttons"""
        def on_enter(e):
            button.configure(bg=hover_color)
        def on_leave(e):
            button.configure(bg=normal_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = EIICSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()