from Code.HashMaps import HashMaps
class PoemWordCount:
    def __init__(self):
        self.list = []
    def load_file(self,file_path,HMaps):
        with open(file_path, "r") as f:
            for line in f:
                words = line.split()
                for word in words:
                    cleaned_word = word.rstrip('.,\'\"#:;!?$(){[]}*')
                    leading_chars = "#.,'\"#:;!?$\'()[{]}*"
                    result = cleaned_word
                    while result and result[0] in leading_chars:
                        result = result[1:]
                    if result in HMaps:
                        HMaps[result] += 1
                    else:
                        HMaps[result] = 1
                        self.list.append(result)

    def write_file(self,HMaps):
        f = open("E:\\Python Folders\\pythonProject\\files\\WordCount1.txt", "w")
        self.list.sort()
        f.write("                           Word Count\n")
        for word in self.list:
            f.write(f"{word} :- {HMaps[word]}\n")
        f.close()

if __name__=="__main__":
    HMaps = HashMaps()
    obj = PoemWordCount()
    obj.load_file("E:\\Python Folders\\pythonProject\\files\\test.txt",HMaps)
    obj.write_file(HMaps)
    print(HMaps.arr)
