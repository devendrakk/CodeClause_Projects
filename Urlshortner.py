import tkinter as tk
from tkinter import messagebox
import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.short_to_long_map = {}
        self.domain = "http://short.url/"

    def generate_short_url(self, long_url):
        # If the URL has already been shortened, return the short version
        if long_url in self.url_map:
            return self.url_map[long_url]
        
        # Generate a random 6-character string
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        # Ensure the short URL is unique
        while short_url in self.short_to_long_map:
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        short_url = self.domain + short_url
        self.url_map[long_url] = short_url
        self.short_to_long_map[short_url] = long_url
        
        return short_url

class URLShortenerApp:
    def __init__(self, root):
        self.shortener = URLShortener()
        
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("400x200")
        self.root.configure(bg='#f0f0f0')
        
        self.label = tk.Label(root, text="Enter the long URL:", bg='#f0f0f0')
        self.label.pack(pady=10)
        
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        
        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url, bg='#4CAF50', fg='white')
        self.shorten_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", bg='#f0f0f0')
        self.result_label.pack(pady=10)

    def shorten_url(self):
        long_url = self.url_entry.get()
        if long_url:
            short_url = self.shortener.generate_short_url(long_url)
            self.result_label.config(text=f"Short URL: {short_url}", fg='#0000FF')
        else:
            messagebox.showerror("Error", "Please enter a valid URL")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
