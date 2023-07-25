import os
import shutil
from moviepy.editor import VideoFileClip

mp4_folder = "mp4folder"  # Specify the path to the mp4 files directory
animation_folder = "animation"  # Specify the path to the animation folder

# Create the animation folder if it doesn't exist
if not os.path.exists(animation_folder):
    os.makedirs(animation_folder)

# Iterate over the files in the mp4 folder
for filename in os.listdir(mp4_folder):
    if filename.endswith(".mp4"):
        file_number = filename.split(".")[0]  # Extract the file number
        
        mp4_filepath = os.path.join(mp4_folder, filename)
        gif_filename = file_number + ".gif"
        gif_filepath = os.path.join(animation_folder, gif_filename)
        
        # Convert the MP4 file to GIF using moviepy
        video_clip = VideoFileClip(mp4_filepath)
        video_clip.write_gif(gif_filepath)
        
# Print a message when the conversion process is completed
print("File conversion completed.")
