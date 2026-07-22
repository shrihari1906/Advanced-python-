import tkinter as tk

class InteractiveDrawer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()
        
        self.start_x = None
        self.start_y = None
        self.rect = None

        # Bind mouse events to trackpad movement
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Create a rectangle object
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='black')

    def on_move_press(self, event):
        cur_x, cur_y = (event.x, event.y)
        
        # Calculate dynamic shading based on position (0-255 range)
        # R changes with X, B changes with Y
        r = int((cur_x / 800) * 255)
        b = int((cur_y / 600) * 255)
        color = f'#{r:02x}80{b:02x}' # Hex color format #RRGGBB
        
        # Update the rectangle coordinates and color
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)
        self.canvas.itemconfig(self.rect, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveDrawer(root)
    root.mainloop()