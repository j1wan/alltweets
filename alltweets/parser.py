from datetime import datetime


def as_datetime(s: str) -> datetime:
    """
    convert Twitter datetime string into Python datetime object
    :param s: Twitter datetime string
    :return: datetime object
    """
    return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")


