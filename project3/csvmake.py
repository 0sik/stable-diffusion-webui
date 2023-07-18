import csv
from PIL import Image

def get_gif_info(file_path):
    with Image.open(file_path) as im:
        frame_count = im.n_frames
        duration = 0
        for i in range(frame_count):
            im.seek(i)
            duration += im.info.get("duration", 100)  # Use 100 milliseconds as default if duration is not available
        time_per_frame = duration / 1000  # Convert duration from milliseconds to seconds
        return frame_count, time_per_frame

gif_files = ["./animation/000000.gif", "./animation/000001.gif"]  # Replace with the paths to your actual GIF files
output_file = "gif_info.csv"  # Specify the output CSV file name

# Open the CSV file in write mode and create a CSV writer
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "frame", "time"])  # Write the header row
    
    for gif_file in gif_files:
        gif_name = gif_file.split("/")[-1].split(".")[0]  # Extract the name from the file path
        frame_count, time_per_frame = get_gif_info(gif_file)
        time_format = f"{int(time_per_frame // 60):02d}:{int(time_per_frame % 60):02d}"  # Format time as "mm:ss"
        writer.writerow([gif_name, frame_count, time_format])  # Write the row for the current GIF file

print("CSV file created successfully.")
