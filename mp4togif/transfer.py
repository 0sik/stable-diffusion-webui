import imageio


mp4_path = "000000.mp4"


gif_path = "000000.gif"


video = imageio.get_reader(mp4_path)


frames = []


for frame in video:
    frames.append(frame)

imageio.mimsave(gif_path, frames, format="gif")

print("Conversion complete!")
