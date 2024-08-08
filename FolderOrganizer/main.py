import os
import shutil
import argparse

def organize_folder(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_ext = file.split('.')[-1]
            dest_dir = os.path.join(path, file_ext)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.move(file_path, os.path.join(dest_dir, file))

def main(directories):
    for directory in directories:
        organize_folder(directory)

parser = argparse.ArgumentParser(description='c files in directories by extension.')
parser.add_argument('directories', nargs='+', help='List of directories to organize')
args = parser.parse_args()

main(args.directories)
