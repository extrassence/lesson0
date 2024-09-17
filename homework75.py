import os
import time

maindir = 'Z:\\PycharmProjects\\xtras\\.venv'
os.chdir(maindir)
for root, dirs, files in os.walk(maindir):
    os.chdir(root)
    for file in files:
        filepath = os.path.realpath(file)
        filetime = os.stat(filepath).st_ctime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.getcwd()
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
