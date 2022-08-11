from django.conf import settings
from termcolor import colored

try:
    ERROR_MESSAGE = settings.FILE_VALIDATOR_ERROR_MESSAGE
except AttributeError:
    ERROR_MESSAGE = "File is not valid"

try:
    SHOW_MESSAGE_ONLY = settings.FILE_VALIDATOR_SHOW_MESSAGE_ONLY
except AttributeError:
    SHOW_MESSAGE_ONLY = False

try:
    SHOW_FILE_NAME = settings.FILE_VALIDATOR_SHOW_FILE_NAME
except AttributeError:
    SHOW_FILE_NAME = False

try:
    SHOW_MIME_TYPE = settings.FILE_VALIDATOR_SHOW_MIME_TYPE
except AttributeError:
    SHOW_MIME_TYPE = False

try:
    ERROR_MESSAGE = settings.FILE_VALIDATOR_ERROR_MESSAGE
except AttributeError:
    ERROR_MESSAGE = "File is not valid"


def error_message(
        file,
        mimes,
        message=ERROR_MESSAGE,
        show_file_name=SHOW_FILE_NAME,
        show_mime_type=SHOW_MIME_TYPE,
        show_message_only=SHOW_MESSAGE_ONLY,
):
    if (
            show_file_name
            and show_mime_type
            and show_message_only
            or show_mime_type
            and show_message_only
            or show_file_name
            and show_message_only
    ):
        message = "If you want only the message to be displayed, set the show_file_name and show_mime_type parameters to False"
        raise ValueError(colored(message, "red"))

    file_mimes = ""
    for mime in mimes:
        file_mimes += str(mime)
        file_mimes += ', '
        if mime == mimes[-1]:
            file_mimes += str(mime)

    if show_file_name:
        message = f"{file} {message}"
    elif show_mime_type:
        message = f"{message} {file_mimes}"
    elif show_file_name and show_mime_type:
        message = f"{file} {message} {file_mimes}"
    elif show_message_only:
        message = f"{message}"
    else:
        message = f"{file} {message} {file_mimes}"
    return message
