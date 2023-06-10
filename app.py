import speech_recognition as sr
import cv2
from sense_hat import SenseHat
from time import sleep

# Initialize the recognizer
r = sr.Recognizer()
sense = SenseHat()

def listen_and_recognize():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = r.recognize_google(audio)
        print("You said:", command)
        
        # Process the recognized command
        process_command(command)
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
        
    except sr.RequestError as e:
        print("Sorry, there was an error while processing your request. Please try again later.", str(e))

def process_command(command):
    # Define your own logic to process the recognized command
    if "picture" in command.lower():
        capture_image()
    elif "burst" in command.lower():
        for i in range (3, -1, -1):
            sense.show_letter( str(i) )
            sleep(1)
        capture_burst(3)
    elif "goodbye" in command.lower():
        print("Goodbye!")
        exit()

def capture_image():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite("captured_image.jpg", image)
    camera.release()
    print("Image captured successfully!")

def capture_burst(count):
    camera = cv2.VideoCapture(0)
    for i in range(count):
        return_value, image = camera.read()
        cv2.imwrite(f"captured_image_{i+1}.jpg", image)
        sleep(1)
    camera.release()
    print(f"{count} images captured successfully!")

# Continuously listen for voice commands
while True:
    listen_and_recognize()
