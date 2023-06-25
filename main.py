import os
import shutil

from configs import (
    KEEP_ORIGINAL_DIRECTORY,
    DEST_BASE_DIR,
    GROUP_TO_YEARS,
    SEPERATOR,
    FLIPPED,
    MOVE_FILES,
    FILE_EXTENSIONS,
)
from dateExtractor import DateExtractor


def year_month_dir(month, year) -> str:
    """
    Returns the year and month directory name.
    :param month:
    :param year:
    :return:
    """

    return f"{year}{SEPERATOR}{month}" if FLIPPED else f"{month}{SEPERATOR}{year}"


def get_destination_path(source_base_dir, source_path, month, year) -> str:
    """
    Returns the destination path for the given source path.
    :param source_base_dir: The source base directory to be removed from the source path
    :param source_path: The source path
    :param month: The month
    :param year: The year
    :return: The destination path
    """

    destination_path = DEST_BASE_DIR

    if GROUP_TO_YEARS:
        destination_path = os.path.join(destination_path, year)
        destination_path = os.path.join(destination_path, month)
    else:
        destination_path = os.path.join(destination_path, year_month_dir(month, year))

    rel_path = os.path.relpath(source_path, source_base_dir)

    if KEEP_ORIGINAL_DIRECTORY:
        return os.path.join(destination_path, rel_path)
    else:
        return os.path.join(destination_path, os.path.basename(rel_path))


def process_file(source_base_dir, file_path, extractor) -> None:
    """
    Processes the given file.
    :param source_base_dir: The source base directory to be removed from the source path
    :param file_path: The file path
    :param extractor: The extractor to be used for extracting the date
    :param functions_list: A list of functions to be used for extracting the date
    """

    date = extractor.extract(file_path)

    if date is None:
        month, year = None, None
    else:
        month, year = date.month, date.year

    if month is None or year is None:
        print(f"Could not extract date from file: {file_path}")
        return

    destination_path = get_destination_path(
        source_base_dir=source_base_dir,
        source_path=file_path,
        month=month,
        year=year
    )

    print(f"Moving file: {file_path} to: {destination_path}")

    if MOVE_FILES:
        os.rename(file_path, destination_path)
    else:
        shutil.copy(file_path, destination_path)


def process_directory(directory) -> None:
    """
    Processes the given directory.
    :param directory: The directory
    :param functions_list: A list of functions to be used for extracting the date
    """

    extractor = DateExtractor()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1][1:]  # Get the file extension without the dot

            if file_extension.lower() in [x.lower() for x in FILE_EXTENSIONS]:
                process_file(
                    source_base_dir=directory,
                    file_path=file_path,
                    extractor=extractor
                )


def main(directory, configs=None):
    """
    The main function.
    :param directory: The directory
    :param configs: The configurations to be used
    :param functions_list: A list of functions to be used for extracting the date
    """

    if configs is not None:
        global KEEP_ORIGINAL_DIRECTORY
        global DEST_BASE_DIR
        global GROUP_TO_YEARS
        global SEPERATOR
        global FLIPPED
        global MOVE_FILES
        global FILE_EXTENSIONS

        KEEP_ORIGINAL_DIRECTORY = configs.KEEP_ORIGINAL_DIRECTORY or KEEP_ORIGINAL_DIRECTORY
        DEST_BASE_DIR = configs.DEST_BASE_DIR or DEST_BASE_DIR
        GROUP_TO_YEARS = configs.GROUP_TO_YEARS or GROUP_TO_YEARS
        SEPERATOR = configs.SEPERATOR or SEPERATOR
        FLIPPED = configs.FLIPPED or FLIPPED
        MOVE_FILES = configs.MOVE_FILES or MOVE_FILES
        FILE_EXTENSIONS = configs.FILE_EXTENSIONS or FILE_EXTENSIONS

    process_directory(directory)


if __name__ == '__main__':
    directory = r""
    main(
        directory=directory
    )

