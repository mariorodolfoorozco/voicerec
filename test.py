from sense_hat import SenseHat
from time import sleep
import picamera

camera = picamera.PiCamera()

# Adjust camera settings if needed
# camera.resolution = (1280, 720)  # Set resolution
# camera.rotation = 180           # Set rotation

# Wait for the camera to initialize
sleep(2)

# Capture an image and save it to a file
camera.capture("image.jpg")

# Release the camera resources
camera.close()
