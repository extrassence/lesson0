import time
from multiprocessing import Pool


def read_info(filename):
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line.strip():
                break


filenames = [f'file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__': #Знаю, что это обязательно только при мультипроцессорной обработке, но почему бы и нет
# Линейная обработка файлов
    start_time_linear = time.time()
    for filename in filenames:
        data = read_info(filename)
    end_time_linear = time.time()
    print(f'Время выполнения линейной обработки: {end_time_linear - start_time_linear} секунд')

# Мультипроцессорная обработка файлов

    start_time_multiproc = time.time()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    end_time_multiproc = time.time()
    print(f'Время выполнения мультипроцессорной обработки: {end_time_multiproc - start_time_multiproc} секунд')