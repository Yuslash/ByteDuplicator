import os

def copy_module_files(source_directory, destination_file):
    with open(destination_file, 'w') as dest_file:
        for filename in os.listdir(source_directory):
            if filename.endswith('.py'):
                file_path = os.path.join(source_directory, filename)
                with open(file_path, 'r') as source_file:
                    dest_file.write("# File: {}\n\n".format(filename))
                    dest_file.write(source_file.read())
                    dest_file.write("\n\n# End of file: {}\n\n".format(filename))
    print("Module files copied successfully to", destination_file)

if __name__ == "__main__":
    # Specify the source directory where the module files are located.
    # This directory contains the Python module files (.py files) to be copied.
    # Replace 'YourUserName' with your actual username.
    source_directory = "C:\\Users\\YourUserName\\AppData\\Roaming\\Python\\Python39\\site-packages\\speech_recognition"

    # Specify the destination file where you want to store the copied script
    destination_file = "ModulePack.py"

    # Copy the module files to the destination file
    copy_module_files(source_directory, destination_file)
