import os.path
import shutil
import requests


def get_cats(folder, name):
    url = "https://cataas.com/cat"
    data = get_data_from_url(url)
    save_images(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_images(folder, name, data):
    file_name = os.path.join(folder, name + ".jpg")
    with open(file_name, "wb") as fout:
        shutil.copyfileobj(data, fout)