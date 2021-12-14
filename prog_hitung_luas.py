class Luas:
    def luasPersegiPanjang(panjang, lebar):
        luas = panjang * lebar
        print ("Luas persegi panjang: %s" % luas)
        return luas
    def luasPersegi(sisi):
        luas = sisi * sisi
        print ("Luas persegi: %s" % luas)
        return luas
    def luasSegitiga(alas, tinggi):
        luas = 1/2 * alas * tinggi
        print ("Luas segitiga: %s" % luas)
        return luas
    def luasLingkaran(jari):
        luas = 22/7 * (jari*jari)
        print("Luas lingkaran: %s" % luas)
        return luas
    def luasTrapesium(atas,bawah,tinggi):
        luas = 1/2 * (atas+bawah) * tinggi
        print("Luas trapesium: %s" % luas)
        return luas
    def luasJajarG(alas,tinggi):
        luas = alas * tinggi
        print("Luas jajar genjang: %s" % luas)
        return luas

class Main:
    def main():
            print("Pilih Menu:\n1. Hitung luas persegi panjang\n2. Hitung luas persegi\n3. Hitung luas segitiga")
            print("4. Hitung luas lingkaran\n5. Hitung luas trapesium\n6. Hitung luas jajar genjang\n7. Exit")
            var = int(input("Pilihan: "))
            if (var == 1):
                p = int(input('Masukkan panjang: '))
                l = int(input('Masukkan lebar: '))
                Luas.luasPersegiPanjang(p,l)
            elif (var == 2):
                s = int(input('Masukkan panjang sisi: '))
                Luas.luasPersegi(s)
            elif (var == 3):
                a = int(input('Masukkan panjang alas: '))
                t = int(input('Masukkan tingginya: '))
                Luas.luasSegitiga(a,t)
            elif (var == 4):
                j = int(input('Masukkan jari-jari: '))
                Luas.luasLingkaran(j)
            elif (var == 5):
                a = int(input('Masukkan panjang atap: '))
                b = int(input('Masukkan panjang alas bawah: '))
                t = int(input('Masukkan panjang tinggi: '))
                Luas.luasTrapesium(a,b,t)
            elif (var == 6):
                a = int(input('Masukkan panjang alas: '))
                t = int(input('Masukkan tingginya: '))
                Luas.luasJajarG(a,t)
            elif (var == 7):
                exit()
            else:
                print("Menu tidak ditemukan")

Main.main()
