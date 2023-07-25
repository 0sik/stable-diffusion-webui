import codecs

# 파일 경로 지정
file_path = "after2.txt"

# 파일 읽기
with codecs.open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 문자열 수정
modified_lines = [line.replace("완료로#완료로", "완료로") for line in lines]

# 수정된 내용을 파일에 저장
with codecs.open(file_path, "w", encoding="utf-8") as file:
    file.writelines(modified_lines)

print("파일이 수정되었습니다.")
