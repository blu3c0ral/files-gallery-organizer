

"""
List of file extensions to be processed.
"""
FILE_EXTENSIONS = [
    'jpg',
    'jpeg',
    # 'png',
    # 'gif',
    #  'bmp',
    # 'tif',
    # 'tiff',
    #  'ico',
    # 'webp'
    'mp4',
    'mov',
    'avi',
    'wmv',
    'mpg',
    'mpeg',
    # 'mkv',
    # 'webm',
    # 'flv',
    # 'm4v',
]





"""
Set KEEP_ORIGINAL_DIRECTORY to True if you want to keep the original directory structure.
Otherwise the files will be moved to the destination dates directories without any subdirectories.

For example, if you have a file in the directory /home/user/Downloads/Pictures/DCIM/file.jpg
and KEEP_ORIGINAL_DIRECTORY is set to True, the file will be moved to the directory
/destination_directory/home/user/Downloads/Pictures/DCIM/file.jpg
If KEEP_ORIGINAL_DIRECTORY is set to False, the file will be moved to the directory
/destination_directory/file.jpg

Where /destination_directory is based on the relevant date extracted from the file
"""
KEEP_ORIGINAL_DIRECTORY = False


"""
Set DEST_BASE_DIR to the directory where you want to move or copy files. 
"""
DEST_BASE_DIR = None


"""
Set GROUP_TO_YEARS to True if you want to group files by years.
Otherwise the files will be grouped by years and months.
"""
GROUP_TO_YEARS = True


"""
If you want to move files to a new directory, set MOVE_FILES to True.
If you want to copy files to a new directory, set MOVE_FILES to False.
"""
MOVE_FILES = False


"""
Define a seperator for the year and month directories.
If GROUP_TO_YEARS is set to True, this setting will be ignored.

For example, if you set the seperator to "-", the year and month directories will be named like this:
2020-01
"""
SEPARATOR = "-"


"""
Set FLIPPED to True if you want to have the year before the month in the year and month directories.
If GROUP_TO_YEARS is set to True, this setting will be ignored.

For example, if FLIPPED is set to True, and the SEPERATOR is set to "-",
the year and month directories will be named like this:
2020-01
"""
FLIPPED = True

