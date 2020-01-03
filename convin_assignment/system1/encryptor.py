from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and save it into a file
    """

    key = Fernet.generate_key()
    with open("media/key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the media directory
    """

    return open("media/key", "rb").read()


def encrypt(filename, key):
    """
    Given a filename(str) and key(bytes), it encrypts the file and write it
    """

    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    return encrypted_data