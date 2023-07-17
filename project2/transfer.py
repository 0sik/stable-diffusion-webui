import imageio

# Path to the input .mp4 file
mp4_path = "000000.mp4"

# Path to save the output .gif file
gif_path = "000000.gif"

# Read the .mp4 file
video = imageio.get_reader(mp4_path)

# Initialize the frames list
frames = []

# Iterate over each frame in the video
for frame in video:
    frames.append(frame)

# Save the frames as a .gif file
imageio.mimsave(gif_path, frames, format="gif")

print("Conversion complete!")
