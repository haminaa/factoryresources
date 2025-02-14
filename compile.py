import os
import zipfile

def zip_directory(source_dir, out_folder, zip_name):
    resourcepack_dir = os.path.join(source_dir, 'resourcepack')
    out_folder_path = os.path.join(source_dir, out_folder)
    
    if not os.path.exists(out_folder_path):
        os.makedirs(out_folder_path)
    
    zip_path = os.path.join(out_folder_path, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(resourcepack_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, resourcepack_dir)
                zipf.write(file_path, arcname)

if __name__ == "__main__":
    source_directory = "./"
    out_folder_name = "out"
    zip_file_name = "resourcepack.zip"
    zip_directory(source_directory, out_folder_name, zip_file_name)
    print(f"All files from 'resourcepack' zipped to '{out_folder_name}/{zip_file_name}'.")