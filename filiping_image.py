import cv2

# Start camera
camera = cv2.VideoCapture(0)

# Flip mode
flip_mode = 1


# Mouse/trackpad click function
def mouse_click(event, x, y, flags, param):
    global flip_mode

    if event == cv2.EVENT_LBUTTONDOWN:

        # Horizontal button
        if 20 <= x <= 170 and 450 <= y <= 500:
            flip_mode = 1

        # Vertical button
        elif 190 <= x <= 340 and 450 <= y <= 500:
            flip_mode = 0

        # Both button
        elif 360 <= x <= 510 and 450 <= y <= 500:
            flip_mode = -1

        # Normal button
        elif 530 <= x <= 680 and 450 <= y <= 500:
            flip_mode = 2


cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", mouse_click)


while True:

    ret, frame = camera.read()

    if not ret:
        print("Camera not found!")
        break

    # Apply selected flip
    if flip_mode == 1:
        frame = cv2.flip(frame, 1)

    elif flip_mode == 0:
        frame = cv2.flip(frame, 0)

    elif flip_mode == -1:
        frame = cv2.flip(frame, -1)

    # Add buttons
    cv2.rectangle(frame, (20, 450), (170, 500), (255, 255, 255), -1)
    cv2.putText(frame, "Horizontal", (35, 482),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.rectangle(frame, (190, 450), (340, 500), (255, 255, 255), -1)
    cv2.putText(frame, "Vertical", (215, 482),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.rectangle(frame, (360, 450), (510, 500), (255, 255, 255), -1)
    cv2.putText(frame, "Both", (405, 482),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.rectangle(frame, (530, 450), (680, 500), (255, 255, 255), -1)
    cv2.putText(frame, "Normal", (555, 482),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    # Display
    cv2.imshow("Camera", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()