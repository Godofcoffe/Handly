import requests
from os.path import basename, isdir
from sys import argv, exit

VERSION = "0.1.0"


def download(url, path):
    """
    :param url: url for file.
    :param path: directory_name with file_name.
    """
    resposta = requests.get(url, stream=True)

    if path is None:
        path = basename(url.split("?")[0])
    else:
        if resposta.status_code == requests.codes.OK:
            with open(path, 'wb') as new_file:
                for parte in resposta.iter_content(chunk_size=256):
                    new_file.write(parte)
            print(f"Download complete. File save in: {path}")
        else:
            resposta.raise_for_status()


if __name__ == "__main__":
    if len(argv) <= 1:
        print("main.py <url> <path>")
        exit(0)
    elif "http" not in argv[1]:
        print("Url not valid!")
        exit(0)
    else:
        download(argv[1], argv[2])
