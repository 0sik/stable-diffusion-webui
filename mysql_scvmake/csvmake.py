import csv
from PIL import Image

def get_gif_info(file_path):
    with Image.open(file_path) as im:
        frame_count = im.n_frames
        duration = 0
        for i in range(frame_count):
            im.seek(i)
            duration += im.info.get("duration", 100) 
        time_per_frame = duration / 1000 
        return frame_count, time_per_frame

output_file = "gif_info.csv" 
# Open the CSV file in write mode and create a CSV writer
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["idx", "frame", "time"])  
    
    for i in range(14616): 
        gif_file = f"./animation/{str(i).zfill(6)}.gif" 
        gif_name = gif_file.split("/")[-1].split(".")[0] 
        frame_count, time_per_frame = get_gif_info(gif_file)
        time_format = f"{int(time_per_frame // 60):02d}:{int(time_per_frame % 60):02d}" 
        writer.writerow([gif_name, frame_count, time_format])  

print("CSV file created successfully.")
