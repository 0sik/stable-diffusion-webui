import imageio

def convert_gif_to_mp4(input_path, output_path, fps=10):
    gif_reader = imageio.get_reader(input_path)
    
    gif_meta = gif_reader.get_meta_data()
    
    mp4_writer = imageio.get_writer(output_path, format='FFMPEG', fps=fps)
    
    for frame in gif_reader:
        mp4_writer.append_data(frame)
    
    mp4_writer.close()

input_gif_path = 'input.gif'
output_mp4_path = 'output.mp4'

convert_gif_to_mp4(input_gif_path, output_mp4_path)
