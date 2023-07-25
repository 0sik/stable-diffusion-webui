import os

folder_path = "outputs"
new_folder_path = "new_outputs"
start_number = 3762

def rename_and_move_files(folder_path, new_folder_path, start_number):
    file_names = sorted(os.listdir(folder_path))

    for i, file_name in enumerate(file_names):
        if i < start_number - 1:
            continue

        file_path = os.path.join(folder_path, file_name)
        new_file_name = str(start_number).zfill(6) + ".txt"
        new_file_path = os.path.join(new_folder_path, new_file_name)

        os.rename(file_path, new_file_path)
        print(f"Renamed and moved file: {file_name} -> {new_file_name}")

        start_number += 1

rename_and_move_files(folder_path, new_folder_path, start_number)
