import os
import shutil

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def organize_files(file_extensions, source_directory):
    for filename in os.listdir(source_directory):
        if os.path.isfile(os.path.join(source_directory, filename)):
            file_extension = filename.split(".")[-1].lower()
            if file_extension in file_extensions:
                destination_directory = file_extensions[file_extension]
                create_directory(destination_directory)
                source_path = os.path.join(source_directory, filename)
                destination_path = os.path.join(destination_directory, filename)
                shutil.move(source_path, destination_path)
                print(f"Memindahkan {filename} 👉 {destination_directory}/{filename}")

if __name__ == "__main__":
    
    # directory alamat tempat folder yang ingin dirapikan
    source_directory = "C:/Users/asusy/Downloads"
    source_directory = os.getcwd()
    file_extensions = {
        'pdf': 'PDF',
        'png': 'Images',
        'jpg': 'Images',
        'jpeg': 'Images',
        'svg': 'Images',
        'webp':'Images',
        'avif': 'Images',
        'zip': 'Archives',
        'pptx':'Documents',
        'docx': 'Documents',
        'xlsx': 'Documents',
        'csv':'Documents',
        'mp4': 'Videos',
        '3gpp': 'Videos',
        'exe':'Programs',
        'msi':'Programs'
    }
    
    organize_files(file_extensions, source_directory)