import re
import os
def FindSentence(text):
    text = text.split(".")
    for x in text:
        print(x)
        print("______-------______")
def main():
    f = open("test.txt","r",encoding = "UTF-8").read()
    print(re.findall(r"[А-Я]. [А-Я][а-я]+",f))
    print(re.findall(r"[А-Я]. [А-Я]. [А-Я][а-я]+",f))
    print(re.findall(r"[А-Я][а-я]+ [А-Я][а-я]+",f))
    a1 = re.findall(r"[А-Я]. [А-Я]. [А-Я][а-я]+",f)
    a2 = re.findall(r"[А-Я][а-я]+ [А-Я][а-я]+",f)
    """a1 = [x.split(" ") for x in a1]
    a2 = [x.split(" ") for x in a2]
    for x in a1:
        os.mkdir(x[2])
        f = open(x[2]+"//f.txt","w")
        f.write()
        f.close()
    a2 = [x.split(" ") for x in a2]
    for x in a2:
        os.mkdir(x[1])
        f = open(x[2]+"//f.txt","w")
        f.write()
        f.close()"""
if __name__ == "__main__":
    main()
