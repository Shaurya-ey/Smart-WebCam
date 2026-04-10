import RPi.GPIO as GPIO
import speech_recognition as sr

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RELAY_PIN = 27
GPIO.setup(RELAY PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)

recognizer = sr.Recognizer()

mic = sr.Microphone(device_index=None)

def listen_command():
    with mic as source:
        print("\n Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        print("Could not understand")
        return ""


def relay_on():
    print("Relay ON")
    GPIO.output(RELAY_PIN, GPIO.HIGH)

def relay_off():
    print("Relay OFF")
    GPIO.output(RELAY_PIN, GPIO.LOW)

try:
    print("Jarvis Started (Voice Relay Control)")
    print("Say: 'relay on', 'relay off', or 'exit'")

    while True:
        cmd = listen_command()

        if "relay on" in cmd:
            relay_on()

        elif "relay off" in cmd:
            relay_off()

        elif "exit" in cmd or "stop" in cmd:
            print("Exiting...")
            break

        elif cmd != "":
            print("Unknown command")

except KeyboardInterrupt:
    print("\n Stopped manually")

finally:
    GPIO.cleanup()
