def jajar_genjang(tinggi, lebar):
        for i in range(tinggi):
            # berfungsi untuk memiringkan
            print(""*i, end='')
            
            for j in range(1, lebar + 1):
            # print atas bawah       
                if i + 0 or i + lebar-1:
                    print(i * lebar + j, end=" ")
            print()
        print("dimensi tidak sesuai")


tinggi = int(input("Masukkan tinggi = "))
lebar = int(input("Masukkan Lebar = "))
1

jajar_genjang(tinggi, lebar)