# Теперь рефакторим код.
# Ракладываем его по уровням и задачам.
# 1 уровень - читаем архив и собираем слова из каждого файла
# 2 уровень (ниже) - читаем файл с презентацией и достаём из него слова.
# Уровни лучше разнести по разным файлам.


import os
from zipfile import ZipFile
from pathlib import Path
from helpers import get_words_presentation, write_txt

FILE_ZIP = 'croco-blitz-source.zip'

current_file = os.path.relpath(__file__)
current_directory = os.path.dirname(current_file)

PATH_FILE_ZIP = "croco-blitz-source.zip"


def zip_f():
    with ZipFile(PATH_FILE_ZIP, mode="r") as archive:
        print("Список файлов в архиве: ")
        for f in archive.namelist():
            print(f)


def unzip_zip_file():
    cur_folder = os.path.dirname(os.path.realpath(__file__))
    words: set[str] = set()

    p = Path(cur_folder) / FILE_ZIP

    with ZipFile(p) as zip_ref:
        for f in zip_ref.namelist():
            words.update(get_words_presentation(zip_ref.open(f)))


if __name__ == '__main__':
    unzip_zip_file()
