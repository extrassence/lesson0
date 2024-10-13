import time
from threading import Thread

def write_words(word_count, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range (1, word_count+1):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
        print('Завершилась запись в ',filename)

time1 = time.time()
num = 0
for wds in [10, 30, 200, 100]:
    num += 1
    write_words(wds, f'example{num}.txt')
print('Работа без потоков', time.time() - time1)
time1 = time.time()

thr_1st = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2nd = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3rd = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4th = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1st.start()
thr_2nd.start()
thr_3rd.start()
thr_4th.start()

thr_1st.join()
thr_2nd.join()
thr_3rd.join()
thr_4th.join()

print('Работа потоков', time.time() - time1)

