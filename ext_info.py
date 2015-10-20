import sys
from pathlib import Path
from collections import defaultdict

def create_file_extension():
    return {
        'size': 0,
        'numbers': 0,
    }


# Main Program
if __name__ == '__main__':
    try:
        path = sys.argv[1]
        folder = Path(path)
        files = defaultdict(create_file_extension)
    except IndexError:
        print("Please enter a valid path.")
        exit()


# iterate through the files in folder's path
for p in folder.iterdir():
    if(p.is_file()):
        if(p.suffix[-1:] == '~'):
            continue
        extension_name = p.suffix[1:]
        files[extension_name]['size'] += p.stat().st_size
        files[extension_name]['numbers'] += 1


# Print the information.
for exten, item in files.items():
    print exten, item['numbers'], item['size']
