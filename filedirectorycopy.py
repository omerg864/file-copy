import shutil
import os


def copy_items(fromDirectory, toDirectory, skip_directories):
    skip = False
    corupted_files_to_skip = ["P1010102.JPG", "P1010065.JPG"]
    types_to_copy = [".jpg", ".mp4", ".doc"]
    try:
        if not os.path.exists(toDirectory):
            os.makedirs(toDirectory)
        if not skip:
            for item in os.listdir(fromDirectory):
                print(item)
                s = os.path.join(fromDirectory, item)
                d = os.path.join(toDirectory, item)
                if os.path.isdir(s):
                    if item not in skip_directories:
                        copy_items(s, d, skip_directories)
                else:
                    if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        if need_to_copy(item, types_to_copy) and item not in corupted_files_to_skip:
                            if not os.path.exists(d):
                                shutil.copy2(s, d)
                skip_directories.add(fromDirectory)
    except PermissionError:
        print("Access Denied!!")


def need_to_copy(item, types_to_copy):
    for i in types_to_copy:
        if item.endswith(i) or item.endswith(i.upper()):
            return True
    return False


if __name__ == '__main__':
    fromDirectory = "F:\\"
    toDirectory = "D:\\"
    skip_directories = set()

    copy_items(fromDirectory, toDirectory, skip_directories)
    print(skip_directories)
    print("Done")
