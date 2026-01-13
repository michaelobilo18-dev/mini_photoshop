import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps
import os

class MiniPhotoshop:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Photoshop")
        self.root.geometry("600x700")

        self.original = None
        self.processed = None

        self.label = tk.Label(root)
        self.label.pack()

        tk.Button(root, text="Open Image", command=self.open_image).pack()
        tk.Button(root, text="Grayscale", command=self.grayscale).pack()
        tk.Button(root, text="Blur", command=self.blur).pack()
        tk.Button(root, text="Edges", command=self.edges).pack()
        tk.Button(root, text="Save Image", command=self.save_image).pack()

    def open_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.original = Image.open(path)
            self.processed = self.original.copy()
            self.show_image(self.original)

    def show_image(self, img):
        if img is None:
            messagebox.showerror("Error", "No image to display")
            return
        img_tk = ImageTk.PhotoImage(img)
        self.label.config(image=img_tk)
        self.label.image = img_tk

    def grayscale(self):
        if self.original is None:
            messagebox.showwarning("Warning", "Please open an image first")
            return
        self.processed = ImageOps.grayscale(self.original)
        self.show_image(self.processed)

    def blur(self):
        if self.original is None:
            messagebox.showwarning("Warning", "Please open an image first")
            return
        self.processed = self.original.filter(ImageFilter.GaussianBlur(radius=5))
        self.show_image(self.processed)

    def edges(self):
        if self.original is None:
            messagebox.showwarning("Warning", "Please open an image first")
            return
        self.processed = self.original.filter(ImageFilter.FIND_EDGES)
        self.show_image(self.processed)

    def save_image(self):
        if self.processed is None:
            messagebox.showwarning("Warning", "No image to save")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.processed.save(path)

root = tk.Tk()
app = MiniPhotoshop(root)
root.mainloop()