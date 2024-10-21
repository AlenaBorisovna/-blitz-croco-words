# Создать в репозиторие файл main.py
# Вывести на экран путь к директории, где лежит файл main.py
# Закоммитить, приложить скрин и коммит.

import os

current_file = os.path.relpath(__file__)
current_directory = os.path.dirname(current_file)

print(current_file)
