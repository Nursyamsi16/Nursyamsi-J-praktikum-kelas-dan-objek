class lingkaran (object):
    def __init__(self, p, a ):
        self.phi = p
        self.jarijari = a
    def hitungluas(self):
        return self.phi * self.jarijari * self.jarijari
    def cetakData(self):
        print("phi\t:", self.phi)
        print("jarijari\t:", self.jarijari)


    def cetakluas(self):
        print("luas\t:", self.hitungluas())

def main():
    lingkaran1 = lingkaran(3.14, 5)
    print("Objek lingkaran1")
    lingkaran1.cetakData()
    lingkaran1.cetakluas()


    lingkaran2 = lingkaran(3.14, 7)
    print("\nObjek lingkaran2")
    lingkaran2.cetakData()
    lingkaran2.cetakluas()

if __name__=="__main__":
    main()


class lingkaran(object):
    def __init__(self, p, r):
        self.phi = p
        self.jarijari = r

    def hitungkeliling(self):
        return 2 *self.phi * self.jarijari
    def cetakData(self):
        print("phi\t:", self.phi)
        print("jarijari\t:", self.jarijari)

    def cetakkeliling(self):
        print("keliling\t=", self.hitungkeliling())

def main():

    lingkaran1 = lingkaran(3.14, 8)
    print("Objek lingkaran1")
    lingkaran1.cetakData()
    lingkaran1.cetakkeliling()

    lingkaran2 = lingkaran(3.14, 11)
    print("\nObjek lingkaran2")
    lingkaran2.cetakData()
    lingkaran2.cetakkeliling()

if __name__ == "__main__":
    main()
