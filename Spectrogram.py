import tkinter as tk
from tkinter import filedialog
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_full_spectrogram(file_path)

def display_full_spectrogram(mp3_file):
    # Load the audio file
    y, sr = librosa.load(mp3_file)
    
    # Compute the spectrogram
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    log_spectrogram = librosa.amplitude_to_db(spectrogram, ref=np.max)
    
    # Calculate time axis
    duration = librosa.get_duration(y=y, sr=sr)
    time_axis = np.linspace(0, duration, num=log_spectrogram.shape[1])
    
    # Plot the full spectrogram in a separate window
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(log_spectrogram, sr=sr, x_axis='time', y_axis='mel', cmap='viridis')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Full Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.tight_layout()
    plt.show()

# Create a Tkinter window
root = tk.Tk()
root.title("Full Spectrogram Viewer")

# Create a button to browse for the file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
