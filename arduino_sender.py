import serial
import time

# Change COM port to your Arduino port
arduino = serial.Serial(
    "COM3",
    9600,
    timeout=1
)

time.sleep(2)  # wait for Arduino reset

NOTE_FREQ = {
    "C4": 262,
    "C#4": 277,
    "D4": 294,
    "D#4": 311,
    "E4": 330,
    "F4": 349,
    "F#4": 370,
    "G4": 392,
    "G#4": 415,
    "A4": 440,
    "A#4": 466,
    "B4": 494,

    "C5": 523,
    "D5": 587,
    "E5": 659,
}


def send_song(notes):

    for item in notes:

        note = item["note"]
        duration = item["duration"]

        frequency = NOTE_FREQ.get(note, 0)

        message = f"{frequency},{duration}\n"

        arduino.write(message.encode())

        print("Sent:", message.strip())

        time.sleep(duration / 1000)
