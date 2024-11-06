# Задача 2024.11.01.02
#
# В какой контейнер данных нужно собирать слова чтобы исключить дубликаты?
# Поменяйте код так, чтобы это сделать.
# Подумайте на каком уровне лучше это делать и почему.
# Напишите сколько было слов всего из всех файлов, когда вы сохраняли их в список,
# и сколько стало, когда вы исключили дубликаты.


import os
from zipfile import ZipFile
from pathlib import Path
from helpers import get_words_presentation, write_txt

FILE_ZIP = 'src/croco-blitz-source.zip'


def unzip_zip_file():
    cur_folder = os.path.dirname(os.path.realpath(__file__))
    words: list[str] = list()

    p = Path(cur_folder) / FILE_ZIP

    with ZipFile(p) as zip_ref:
        for f in zip_ref.namelist():
            words.extend(get_words_presentation(zip_ref.open(f)))

    words_set: set = set(words)
    write_txt("words.txt", words_set)

    print(f"{len(words)} слова-дубликаты\n и {len(words_set)} без дубликатов")


if __name__ == '__main__':
    unzip_zip_file()

# 2174 слова-дубликаты
#  и 1635 без дубликатов