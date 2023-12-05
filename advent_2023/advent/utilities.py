import re


def get_digit_from_string(x):
    return [int(x) for x in re.findall(r'(\d+)', x)]


def get_keywords_from_string(x, keywords: list):
    return re.findall(rf'\b({"|".join(keywords)})\b', x)