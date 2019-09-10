class MyFile(object):
    def __init__(self, namafile):
        print("Membuka file %s... \n" % namafile)
        self.file = open(namafile)
    def __del__(self):
        print("\Menutup file...")
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris, end="")

def main():
    f = MyFile ("D:/Cora/semester 3/pemrograman lanjut/paragraf.txt")
    f.bacadata()
if __name__=="__main__":
    main()
