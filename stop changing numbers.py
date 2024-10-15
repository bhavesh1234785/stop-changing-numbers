import tkinter as tk
import random

class RandomNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number App")

        self.number_label = tk.Label(root, text="0", font=("Arial", 40))
        self.number_label.pack(pady=20)

        self.click_count = 0
        self.is_generating = False

        self.button = tk.Button(root, text="Click Me", command=self.on_click, font=("Arial", 20))
        self.button.pack(pady=20)

        self.update_number()

    def update_number(self):
        if self.is_generating:
            random_number = random.randint(0, 100)
            self.number_label.config(text=str(random_number))
        self.root.after(500, self.update_number)

    def on_click(self):
        self.click_count += 1
        if self.click_count % 2 == 0:
            # Even click: start generating numbers
            self.is_generating = True
        else:
            # Odd click: stop generating numbers
            self.is_generating = False

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberApp(root)
    root.mainloop()
