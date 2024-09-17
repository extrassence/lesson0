class WordsFinder:

    def __init__(self, *filenames):
        self.file_names = []
        self.file_names += filenames

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                listwords = []
                for line in file:
                    line_for_split = line.lower()
                    for p in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        is_here = line_for_split.find(p)
                        while is_here > 0:
                            line_for_split = line_for_split.replace(p, '')
                            is_here = line_for_split.find(p)
                    listwords = listwords + line_for_split.split()
            all_words[i] = listwords
        return all_words

    def find(self, word):
        all_found = {}
        words = self.get_all_words()
        for i in words.items():
            counter = 0
            for j in i[1]:
                counter += 1
                if j == word.lower():
                    all_found[i[0]] = counter
                    break
        return all_found

    def count(self, word):
        all_found = {}
        words = self.get_all_words()
        for i in words.items():
            counter = 0
            for j in i[1]:
                if j == word.lower():
                    counter += 1
            all_found[i[0]] = counter
        return all_found


finder2 = WordsFinder('test_file.txt', 'test.txt', 'products.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
