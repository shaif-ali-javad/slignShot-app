import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

class PhotoCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Capture App")
        
        # Set the window to fullscreen
        self.root.attributes('-fullscreen', True)
        
        self.filename = "captured_image.jpg"

        # Create the button to capture photo
        self.capture_button = tk.Button(root, text="Capture Photo", command=self.capture_photo)
        self.capture_button.pack(pady=20)

        # Bind the escape key to exit fullscreen
        self.root.bind("<Escape>", self.exit_fullscreen)

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

    def capture_photo(self):
        # Attempt to open the first available camera (commonly index 0)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror("Error", "Could not open any camera.")
            return

        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            messagebox.showerror("Error", "Could not read frame.")
        else:
            # Save the captured frame to a file
            cv2.imwrite(self.filename, frame)
            messagebox.showinfo("Success", f"Photo saved as {self.filename}")
            self.enable_click()

        # Release the camera
        cap.release()

    def enable_click(self):
        self.root.bind("<Button-1>", self.place_image)

    def place_image(self, event):
        try:
            # Open the image file
            img = Image.open(self.filename)
            
            # Resize the image to 300px while maintaining aspect ratio
            target_size = 300
            img.thumbnail((target_size, target_size), Image.LANCZOS)
            
            # Create a mask to make the image round
            mask = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + img.size, fill=255)
            
            # Apply the mask to the image
            img = img.convert('RGBA')
            img.putalpha(mask)
            
            # Convert the image to a PhotoImage
            img_tk = ImageTk.PhotoImage(img)
            
            # Calculate the coordinates to place the image at the click location
            x = event.x - img.size[0] // 2
            y = event.y - img.size[1] // 2
            
            # Create a new label to hold the image and place it at the calculated coordinates
            image_label = tk.Label(self.root, image=img_tk, bg='white')
            image_label.image = img_tk
            image_label.place(x=x, y=y)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoCaptureApp(root)
    root.mainloop()
