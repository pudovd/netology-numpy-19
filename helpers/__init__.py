import requests
from zipfile import ZipFile
import os, os.path


class MovieLensDatasets:
    def __init__(self):
        self.base_url = "https://files.grouplens.org/datasets/movielens/"
        self.verify_ssl = False

    def download(self, file):
        url = self.base_url + file
        r = requests.get(url, verify=self.verify_ssl)
        open(file, "wb").write(r.content)

    def decompress(self, file):
        with ZipFile(file, "r") as zipObj:
            zipObj.extractall()

    def list_files(self, file):
        with ZipFile(file, "r") as zipObj:
            for filename in zipObj.namelist():
                print(filename)

    def is_already_download(self, file):
        return os.path.exists(file)

    def prepare_datasets(self, small=True):
        file = "ml-latest-small.zip" if small else "ml-latest.zip"

        if not self.is_already_download(file):
            print(f"Starting download file '{file}'...")
            self.download(file)
            self.decompress(file)
            self.list_files(file)
        else:
            print(f"File '{file}' is already downloaded.")
            self.list_files(file)
