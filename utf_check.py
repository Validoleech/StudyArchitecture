import os

def check_encoding(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError as e:
                print(f"Encoding error in file: {file_path} - {e}")

check_encoding('D:/Dev/StudyArchitecture/app')