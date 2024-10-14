import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def convert_to_sketch(image_path):
    # Read the image
    image = cv2.imread(image_path)
   
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
   
    # Blur the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)
   
    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
   
    # Sketch: Combine the original image with the inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
   
    return sketch

class ImageToSketchConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Sketch Converter")
       
        # Create widgets
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)
       
        self.button = tk.Button(root, text="Choose Image", command=self.load_image)
        self.button.pack(pady=10)
       
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(pady=10)
       
        self.convert_button = tk.Button(root, text="Convert to Sketch", command=self.convert_to_sketch)
        self.convert_button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.image = self.image.resize((400, 400))  # Resize the image to fit the canvas
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.canvas.image = self.photo  # Keep a reference to avoid garbage collection

    def convert_to_sketch(self):
        if hasattr(self, 'image_path'):
            sketch = convert_to_sketch(self.image_path)
            
            # Convert the sketch (numpy array) to PIL Image for display in Tkinter
            sketch_pil = Image.fromarray(sketch)
            sketch_pil = sketch_pil.convert("RGB")  # Convert to RGB mode for Tkinter
            sketch_pil = sketch_pil.resize((400, 400))  # Resize to fit the canvas

            # Convert to ImageTk for Tkinter
            sketch_photo = ImageTk.PhotoImage(sketch_pil)
            
            # Display the sketch on the same canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=sketch_photo)
            self.canvas.image = sketch_photo  # Keep a reference to avoid garbage collection
        else:
            messagebox.showwarning("Warning", "Please choose an image first.")

# Create the main window
root = tk.Tk()
app = ImageToSketchConverter(root)
root.mainloop()