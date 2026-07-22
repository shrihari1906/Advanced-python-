import tkinter as tk

def create_gradient(canvas, x1, y1, x2, y2, color1, color2):
    # This function creates a vertical gradient
    width = x2 - x1
    height = y2 - y1
    
    # We draw thin lines to simulate the gradient
    for i in range(height):
        # Calculate intermediate color
        r = int(color1[0] + (color2[0] - color1[0]) * (i / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / height))
        
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(x1, y1 + i, x2, y1 + i, fill=hex_color)

# Usage
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# Shading from Blue to Red
create_gradient(canvas, 50, 50, 350, 350, (0, 0, 255), (255, 0, 0))
root.mainloop()