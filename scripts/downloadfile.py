import os


def downloadfile():
    os.system("kaggle datasets download --force --unzip -d juzershakir/tmdb-movies-dataset")

downloadfile()