import customtkinter as ctk
from gemini_notes import get_song_notes
from arduino_sender import send_song
from PIL import Image
import customtkinter as ctk

#----------------------------
#setting of background imagae
#----------------------------
bg_image = ctk.CTkImage(
    light_image=Image.open("background.png"),
    dark_image=Image.open("background.png"),
    size=(712, 447)
)
# ----------------------------
# App Settings
# ----------------------------
ctk.set_appearance_mode("Light")       # Dark, Light, System
ctk.set_default_color_theme("blue")   # blue, green, dark-blue
# ----------------------------
# Window
# ----------------------------
app = ctk.CTk()
app.title("My baby Piano Player")
app.geometry("712x447")
app.resizable(False, False)
bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# ----------------------------
# Title
# ----------------------------
title = ctk.CTkLabel(
    app,
    text="My baby Piano Player",
    text_color="yellow",
    font=("Arial", 28, "bold"),
    fg_color="#ffffff"
)
title.pack(pady=(40, 10))

subtitle = ctk.CTkLabel(
    app,
    text="Enter a song name please",
    font=("Arial", 14),
    fg_color="#ffffff",
    text_color="pink"
)
subtitle.pack()

# ----------------------------
# Song Entry
# ----------------------------
song_entry = ctk.CTkEntry(
    app,
    width=400,
    height=40,
    placeholder_text="Enter song name..."
)
song_entry.pack(pady=25)

# ----------------------------
# Status
# ----------------------------
status = ctk.CTkLabel(
    app,
    text="Status: Ready",
    text_color="lightgreen",
    font=("Arial", 14),
    fg_color="#ffffff"
)
status.pack(pady=10)

# ----------------------------
# Functions
# ----------------------------
def play_song():
    song = song_entry.get().strip()

    if song == "":
        status.configure(
            text="Please enter a song.",
            text_color="red"
        )
        return

    try:

        status.configure(
            text="Getting notes..."
        )


        result = get_song_notes(song)
        notes=result["notes"]
        print(type(notes))
        print(notes)
        status.configure(
            text=f"Playing {len(notes)} notes"
        )


        send_song(notes)


        status.configure(
            text="Finished"


        )


    except Exception as e:

        status.configure(
            text="Error"
        )

        print(e)

def clear():
    song_entry.delete(0, "end")
    status.configure(
        text="Status: Ready",
        text_color="lightgreen"
    )

# ----------------------------
# Buttons
# ----------------------------
button_frame = ctk.CTkFrame(app, fg_color="#FAE29c")
button_frame.pack(pady=20)

play_btn = ctk.CTkButton(
    button_frame,
    text="▶ Play",
    width=140,
    height=40,
    fg_color="#FEBE00",
    hover_color="#CC7722",
    command=play_song
)
play_btn.grid(row=0, column=0, padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=140,
    height=40,
    fg_color="#e47200",
    hover_color="#AA4C0A",
    command=clear
)
clear_btn.grid(row=0, column=1, padx=10)

# ----------------------------
# Progress Bar
# ----------------------------
progress = ctk.CTkProgressBar(app, width=400)
progress.pack(pady=15)
progress.set(0)

# ----------------------------
# Run
# ----------------------------
app.mainloop()
