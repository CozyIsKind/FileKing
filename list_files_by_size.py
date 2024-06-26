import os

def get_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append((file_path, os.path.getsize(file_path)))
    return file_list

def list_files_by_size(directory):
    file_list = get_files_in_directory(directory)
    sorted_files = sorted(file_list, key=lambda x: x[1])
    for file_path, size in sorted_files:
        print(f"{file_path} - Size: {size} bytes")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    list_files_by_size(directory)
get_files_in_directory(directory)
list_files_by_size(directory)

