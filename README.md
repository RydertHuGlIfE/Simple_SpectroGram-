# Simple_SpectroGram-
This is a simple spectrogram made in python

Full Spectrogram Viewer
This Python script utilizes the Tkinter, Librosa, and Matplotlib libraries to create a GUI application that allows users to select an MP3 file and display its full spectrogram. Here’s a breakdown of its features:

Graphical User Interface (GUI): Utilizes Tkinter to create a window with a 'Browse' button. Users can click this button to select an MP3 file from their file system.

File Dialog: The filedialog.askopenfilename() method lets users browse their files and choose an MP3 file.

Audio Processing: Uses Librosa to load the selected audio file, compute its Mel spectrogram, and convert the amplitude to a decibel scale for better visualization.

Spectrogram Display: Plots the spectrogram using Matplotlib, showing the time on the x-axis, frequency on the y-axis, and color representing the amplitude in decibels.

How to Use:
Run the Script: Execute the Python script to launch the GUI.

Browse File: Click the 'Browse' button to open a file dialog and select an MP3 file.

View Spectrogram: The script will load the audio file, compute its spectrogram, and display it in a new window.

Dependencies:
tkinter

librosa

matplotlib

numpy

