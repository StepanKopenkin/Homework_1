import Stemmer
import pymorphy2
import QuickSort as q
import time
import gzip
import csv
from transliterate import translit


class BigramWorker:
    __stemmer = Stemmer.Stemmer()

    __morph = pymorphy2.MorphAnalyzer()

    __tags = ["adj", "adp", "adv", "conj", "det", "noun", "pron", "verb", "num", "prt", "_", ";", ".", "!", ",", ":",
              "?", "--", "'", "«", "»", ")", "(", '"', "*", ">", "<", "/"]

    __dct = {"stem": "", "normal_form": [], "frequency": ([], [])}

    def __init__(self, verb):
        print("Program start working")
        CurrentTime = time.time()

        self.__dct["stem"] = self.__stemmer.stem(verb)

        fle = self.__GetFile()

        for line in fle:
            line = line.lower()
            if (line[:len(self.__dct["stem"])] == self.__dct["stem"]):
                line = line.replace("\t", " ").replace("\n", "").split(" ")
                for y in self.__tags:
                    if (y in line[0]):
                        line[0] = line[0].replace(y, "")
                    if (y in line[1]):
                        line[1] = line[1].replace(y, "")
                if (line[1] != "" and line[1] != "-" and self.__stemmer.stem(line[0]) == self.__dct[
                    "stem"]):
                    self.__dct["normal_form"].append(self.__morph.parse(line[1])[0].normal_form)
                    self.__dct["frequency"][1].append(int(line[3]))

        fle.close()

        print(str(self.GetLen()) + " strings with stem " + self.__dct["stem"])
        print("Start Transforming...")
        self.__Transformation()

        print("Transforming is finished.Sorting...")
        self.__FinalTransformation()

        CurrentTime2 = time.time()
        print("Programm has been working %f seconds" % (CurrentTime2 - CurrentTime))

    def GetLen(self):
        return len(self.__dct["normal_form"])

    # Данную функцию я взял у Марка, немного изменил ее, чтобы она скачивала файлы для любого глагола
    def __GetFile(self):
        """
        :return: Возвращает файл, который нужен для работы с данным глаголом
        """
        npart = translit(self.__dct["stem"][:2], reversed=True)
        url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-rus-all-2gram-20120701-"
        url += npart
        url += ".gz"
        file_name = url.split('/')[-1]
        try:
            return gzip.open(file_name, 'rt', encoding='utf-8')
        except IOError:
            import urllib.request
            import urllib.error
        try:
            urllib.request.urlretrieve(url, file_name)
            return gzip.open(file_name, 'rt', encoding='utf-8')
        except urllib.error.URLError:
            print("Internet connection is down, try later")
            exit()

    def ToFile(self, name):
        """
        Функция преобразовывает соварь в вайл формата csv
        :param name: Имя файла
        :return: None
        """
        with open(name + ".csv", 'w', newline='') as csvfile:
            wrtr = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for x in range(self.GetLen()):
                wrtr.writerow([self.__dct["stem"], self.__dct["normal_form"][self.__dct["frequency"][0][x]],
                               self.__dct["frequency"][1][x]])

    def __Transformation(self):
        """
        Функция соединяет поля с одинаковыми значениями
        :return:
        """
        x = 0
        while (x < self.GetLen()):
            y = x
            while (y < self.GetLen() - 1):
                if (self.__dct["normal_form"][x] == self.__dct["normal_form"][y + 1]):
                    self.__dct["frequency"][1][x] += self.__dct["frequency"][1][y + 1]
                    del self.__dct["frequency"][1][y + 1]
                    del self.__dct["normal_form"][y + 1]
                else:
                    y += 1
            x += 1

        [self.__dct["frequency"][0].append(x) for x in range(self.GetLen())]

    def __FinalTransformation(self):
        """
        Сортировка словаря
        :return:
        """
        q.quickSort(self.__dct["frequency"], 1, True)
