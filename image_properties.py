import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the Tkinter root window
Tk().withdraw()

# Open file dialog to select an image
file_path = askopenfilename(
    title="Open an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif")]
)

# Check if an image was selected
if file_path:
    # Read the image
    image = cv2.imread(file_path)

    if image is not None:
        print('Shape:', image.shape)  # (height, width, channels)
        print('Size:', image.size)  # total number of values
        print('Data type:', image.dtype)  # usually uint8

    # Display the image
    cv2.imshow("Selected Image", image)

    print("Press any key to close the image window...")

    # Wait indefinitely until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
else:
    print("No image selected.")





