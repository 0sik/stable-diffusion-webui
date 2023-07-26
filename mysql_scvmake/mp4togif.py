import os
import shutil
from moviepy.editor import VideoFileClip

mp4_folder = "mp4folder" 
animation_folder = "animation"  


if not os.path.exists(animation_folder):
    os.makedirs(animation_folder)


for filename in os.listdir(mp4_folder):
    if filename.endswith(".mp4"):
        file_number = filename.split(".")[0]  # Extract the file number
        
        mp4_filepath = os.path.join(mp4_folder, filename)
        gif_filename = file_number + ".gif"
        gif_filepath = os.path.join(animation_folder, gif_filename)
        
       
        video_clip = VideoFileClip(mp4_filepath)
        video_clip.write_gif(gif_filepath)
        

print("File conversion completed.")
