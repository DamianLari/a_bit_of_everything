import os
import random
import argparse

def create_random_files(directories, num_files=10, num_subfolders=3, num_files_in_subfolder=5, extensions=None):
    default_extensions = ['txt', 'png', 'jpeg', 'js', 'py', 'mp4', 'csv', 'json', 'html', 'css']
    if extensions is None:
        extensions = default_extensions
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
        for i in range(num_files):
            ext = random.choice(extensions)
            file_path = os.path.join(directory, f'file{i}.{ext}')
            with open(file_path, 'w') as f:
                f.write(f'// Example content for {ext} file\n')
        
        for i in range(num_subfolders):
            sub_dir = os.path.join(directory, f'subfolder{i}')
            os.makedirs(sub_dir, exist_ok=True)
            for j in range(num_files_in_subfolder):
                ext = random.choice(extensions)
                file_path = os.path.join(sub_dir, f'subfile{j}.{ext}')
                with open(file_path, 'w') as f:
                    f.write(f'// Example content for {ext} file in subfolder\n')

parser = argparse.ArgumentParser(description='Create random files and folders.')
parser.add_argument('directory', nargs='+', help='Base directories to create files and subfolders')
parser.add_argument('--num_files', type=int, default=10, help='Number of files to create in the base directory')
parser.add_argument('--num_subfolders', type=int, default=3, help='Number of subfolders to create')
parser.add_argument('--num_files_in_subfolder', type=int, default=5, help='Number of files in each subfolder')
parser.add_argument('--extensions', nargs='*', default=None, help='List of file extensions to use, e.g., txt png jpeg')
args = parser.parse_args()

create_random_files(args.directory, args.num_files, args.num_subfolders, args.num_files_in_subfolder, args.extensions)
