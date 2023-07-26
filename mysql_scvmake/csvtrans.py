import csv
import os

def read_text_file(file_path, encoding="utf-8"):
    with open(file_path, "r", encoding=encoding) as file:
        lines = file.readlines()
        desceng = " ".join([
            line.split("#")[1].strip() + "." if not line.split("#")[1].endswith(".") else line.split("#")[1].strip()
            for line in lines
            if not line.startswith("#")
        ])
        deschan = " ".join([
            line.split("#")[0].strip() + "." if not line.split("#")[0].endswith(".") else line.split("#")[0].strip()
            for line in lines
            if not line.startswith("#")
        ])
        return desceng, deschan

gif_info_file = "gif_info.csv"  
text_folder = "./text/"  

output_file = "edited_gif_info.csv"  


with open(gif_info_file, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = ['idx', 'kind', 'desceng', 'deschan', 'frame', 'time']  
    
    
    rows = []
    
    for row in reader:
        gif_name = row["idx"]
        text_file_path = os.path.join(text_folder, gif_name + ".txt")
        
        if os.path.isfile(text_file_path):
           
            desceng, deschan = read_text_file(text_file_path, encoding="utf-8")
            row["desceng"] = desceng
            row["deschan"] = deschan
        
        
        row["kind"] = "1"
        
        
        rows.append(row)

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
      
        row["desceng"] = '"' + row["desceng"] + '"'
        row["deschan"] = '"' + row["deschan"] + '"'

        writer.writerow(row)
