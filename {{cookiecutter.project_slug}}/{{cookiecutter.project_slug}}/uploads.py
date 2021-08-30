from werkzeug.utils import secure_filename


def save_file(filename: str) -> str:
    """
    Saves the given file to a local directory,
    and returns the generated file name.
    """
    return secure_filename(filename)
