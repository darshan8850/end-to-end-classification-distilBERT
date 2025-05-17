import os
import sys
import pickle

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save an object to a file using pickle serialization.

    Args:
        file_path (str): The path to the file where the object will be saved.
        obj: The object to be saved.

    Raises:
        CustomException: If an error occurs during the saving process.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load an object from a file using pickle deserialization.

    Args:
        file_path (str): The path to the file from which the object will be loaded.

    Returns:
        The object loaded from the file.

    Raises:
        CustomException: If an error occurs during the loading process.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
