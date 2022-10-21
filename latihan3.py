# input nilai variabel
a = input("masukkan nilai a: ")
b = input("masukkan nilai b: ")

# cetak nilai variabel
print("Variable a=",a)
print("Variable b=",b)

# cetak hasil operasi kedua variabel dengan String Format
print("Hasil Penggabungan", a, '&', b, '=', "{0}{1}".format (a,b))

# konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan", a,'+',b,"= %d" %(a+b))
print("Hasil penjumlahan", a,'/',b,"= %d" %(a/b))
