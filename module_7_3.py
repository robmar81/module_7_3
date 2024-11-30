class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        string = ''
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punctuation:
                        line = line.replace(i, '')
                string = string + line
            all_words.update({self.file_names: string.split()})

        return all_words


    def find(self, txt):
        dict2 = {}
        word2 = self.get_all_words()[self.file_names]
        for j in range(len(word2)):
            if txt.lower() == word2[j]:
                dict2.update({self.file_names: j + 1})
                return dict2


    def count(self, txt):
        dict3 = {}
        word3 = self.get_all_words()[self.file_names]
        dict3.update({self.file_names: word3.count(txt.lower())})
        return dict3


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
