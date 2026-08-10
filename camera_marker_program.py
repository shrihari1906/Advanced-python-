import cv2
import numpy as np

camera = cv2.VideoCapture(0)

# Canvas will hold the drawing (same size as frame)
canvas = None
drawing = False
prev_point = None

# Drawing settings
color = (0, 0, 255)  # Red (BGR)
thickness = 4

colors = {
    ord('1'): (0, 0, 255),    # Red
    ord('2'): (0, 255, 0),    # Green
    ord('3'): (255, 0, 0),    # Blue
    ord('4'): (0, 255, 255),  # Yellow
    ord('5'): (255, 255, 255) # White
}

def draw(event, x, y, flags, param):
    global drawing, prev_point, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and prev_point is not None:
            cv2.line(canvas, prev_point, (x, y), color, thickness)
            prev_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        prev_point = None

cv2.namedWindow("Web Camera")
cv2.setMouseCallback("Web Camera", draw)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)  # mirror view, feels natural to draw on

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Merge drawing canvas onto the live frame
    combined = cv2.addWeighted(frame, 1, canvas, 1, 0)

    cv2.putText(combined, "Draw: click+drag | 1-5: colors | c: clear | q: quit",
                (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Web Camera", combined)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)  # clear the drawing
    elif key in colors:
        color = colors[key]

camera.release()
cv2.destroyAllWindows()