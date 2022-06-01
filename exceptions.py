class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates"""

class ApiServiceError(Exception):
    """Program can't parse weather info"""

class HistoryStorageError(Exception):
    """Program can't write weather history"""
