import datetime
import os
from typing import Union
from datetime import date

from dateFromName import FILE_PATTERNS, DIR_PATTERNS


"""
Each key has a tuple of (name, priority). Priority is used to determine the order of the extract types.
test is used to determine if the extract type is relevant for the given file path - not implemented yet.
handler is the function to be used for extracting the date.
Failed attempts (resulted in None) are followed by the next extract type.
"""
EXTRACT_TYPES = {
    ("file_name", 0): {
        "test": None,
        "handler": "get_date_from_file_name"
    },
    ("directory_name", 1): {
        "test": None,
        "handler": "get_date_from_directory_name"
    },
    # "metadata": {
    #     "test": "metadata_test",
    #     "handler": "get_date_from_metadata"
    # },
}


"""
Replacing the handlers with the actual functions.
"""
for key, value in EXTRACT_TYPES.items():
    value["handler"] = locals()[value["handler"]]


"""
Sorts the extract types by priority.
"""
EXTRACT_TYPES = dict(sorted(EXTRACT_TYPES.items(), key=lambda item: item[0][1]))


class DateExtractor:
    def __init__(self):
        self._extract_types = EXTRACT_TYPES

    def extract(self, file_path) -> Union[date, None]:
        """
        Extracts the date from the given file path. Using extract types as defined in EXTRACT_TYPES (order matters).
        :param file_path: The file path
        :return: The date
        """

        for _, conf in self._extract_types.items():
            file_date = conf["handler"](file_path)
            if file_date:
                return file_date

        return None


def get_date_from_file_name(file_path) -> Union[date, None]:
    for _, conf in FILE_PATTERNS.items():
        filename = os.path.basename(file_path)
        match = conf["compiled"].match(filename)
        if match:
            return conf["handler"](match)
    return None


def get_date_from_directory_name(file_path) -> Union[date, None]:
    for _, conf in DIR_PATTERNS.items():
        match = conf["compiled"].match(file_path)
        if match:
            return conf["handler"](match)
    return None


# Metadata option is not fully implemented yet
'''
def is_all_files_in_time_interval(directory, epsilon):
    """
    Checks if all files in the given directory are in the same time interval.
    :param directory: The directory to check
    :param epsilon: Maximum time difference in seconds
    :return: True if all files in the given directory are in the same time interval, False otherwise
    """

    dates = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            dates.append(file_date)

    if len(dates) == 0:
        return True

    min_date = min(dates)

    for file_date in dates:
        if abs((file_date - min_date).total_seconds()) > epsilon:
            return False

    return True


def metadata_test(directory) -> bool:
    """
    Checks if the given directory's files have valid metadata (i.e. all files are not in the same time interval).
    :param directory: The directory to check
    :return: True if the given directory's files have valid metadata, False otherwise
    """

    interval_check = is_all_files_in_time_interval(directory, epsilon=60*60)
    if interval_check:
        print("Metadata test failed: all files are in the same time interval")
        return False

    return True


def get_date_from_metadata(file_path) -> Union[date, None]:
    """
    Extracts the date from the given file path using the file metadata.
    :param file_path: The file path
    :return: The date
    """
    return datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
'''
