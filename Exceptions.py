
class InteractorException(Exception):
    """Base exception thrown by the interactor"""


class PathDoesNotExistException(InteractorException):
    """The path to the binaries does not seem to exist"""


class BinaryNotPresentException(InteractorException):
    """One or more of the binaries are not present in the given path"""


class WrongTypeException(InteractorException):
    """The passed argument is not of the correct type"""


class FormatNotCorrectException(InteractorException):
    """The format of the passed argument does not sem to match the requirements"""


class YoutubeDLException(InteractorException):
    """Youtube-dl itself gave an error"""


class BadOutputException(InteractorException):
    """Youtube-dl gave some output that we can't seem to parse to a string"""
