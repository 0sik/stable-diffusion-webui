import os

file_path = 'after2.txt'
output_directory = 'output'
count = 13786
# 카운트가 1로 시작하여 before.txt파일에 가서 000000.txt는 자기가 스스로 만들어줘야함
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = None

    for line in lines:
        line = line.strip()
        if line == '완료로':
            if output_file:
                output_file.close()
                count += 1
            output_file_path = os.path.join(output_directory, f'{str(count).zfill(6)}.txt')
            output_file = open(output_file_path, 'a', encoding='utf-8')
        elif output_file:
            output_file.write(line + '\n')

    if output_file:
        output_file.close()

    print('Files have been successfully created.')
except UnicodeDecodeError:
    print('Error: Unable to decode the file with the specified encoding.')
