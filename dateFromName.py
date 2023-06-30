"""

"""
import re
from datetime import date
from typing import Union

YYYY = r"(20\d{2})"  # Year
mm = r"(0[1-9]|1[0-2])"  # Month
DD = r"(0[1-9]|[12]\d|3[01])"  # Day
HH = r"([0-1][0-9]|2[0-3])"  # Hours
MM = r"([0-5][0-9])"  # Minutes
SS = r"([0-5][0-9])"  # Seconds

YYYYmm = YYYY + mm
YYYYmmDD = YYYY + mm + DD
HHMMSS = HH + MM + SS
YYYYmmDD_HHMMSS = YYYYmmDD + r"_" + HHMMSS

"""
The patterns for the different types of optional files or directories.
"""
FILE_PATTERNS = {
    "iphone": {
        "pattern": r"^IMG_" + YYYYmmDD_HHMMSS,
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
    "iphone_vid": {
        "pattern": r"^VID_" + YYYYmmDD_HHMMSS,
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
    "samsung": {
        "pattern": r"^" + YYYYmmDD_HHMMSS,
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
    "whatsapp": {
        "pattern": r"^(?:IMG|VID)-" + YYYYmmDD + r"-WA\d+",
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
    "date": {
        "pattern": YYYYmmDD,
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
    "date-": {
        "pattern": YYYY + r"-" + mm + r"-" + DD,
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
    "screenshot": {
        "pattern": r"^Screenshot_" + YYYYmmDD + "-" + HHMMSS,
        "compiled": None,
        "handler": "extract_from_yyyymmdd_patterns"
    },
}

DIR_PATTERNS = {
    "date_dir": {
        "pattern": r"^" + YYYYmm + r"_{0,2}$",
        "compiled": None,
        "handler": "extract_from_yyyymm_patterns"
    },
    "date_path": {
        "pattern": r"[/\\]" + YYYY + r"_{0,2}" + r"[/\\]" + mm + r"_{0,2}$",
        "compiled": None,
        "handler": "extract_from_yyyymm_patterns"
    },
}

"""
Compiling the patterns.
"""
for key, value in FILE_PATTERNS.items():
    value["compiled"] = re.compile(value["pattern"])

for key, value in DIR_PATTERNS.items():
    value["compiled"] = re.compile(value["pattern"])


########################################################################################################################
# Utility functions                                                                                                    #
########################################################################################################################


def to_date(date_str):
    return date(int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:8]))


def extract_from_yyyymmdd_patterns(match: re.Match) -> Union[date, None]:
    """
    Extracts the date from a string of the format YYYYmmDD.
    :param match: The match object
    :return: The date
    """
    try:
        return to_date(match.group(1) + match.group(2) + match.group(3))
    except ValueError:
        return None


def extract_from_yyyymm_patterns(match: re.Match) -> Union[date, None]:
    """
    Extracts the date from a string of the format YYYYmm.
    :param match: The match object
    :return: The date
    """
    try:
        return to_date(match.group(1) + match.group(2) + "01")
    except ValueError:
        return None


########################################################################################################################
# End of utility functions                                                                                             #
########################################################################################################################


"""
Replacing the handlers with the actual functions.
"""
for key, value in FILE_PATTERNS.items():
    value["handler"] = locals()[value["handler"]]
for key, value in DIR_PATTERNS.items():
    value["handler"] = locals()[value["handler"]]