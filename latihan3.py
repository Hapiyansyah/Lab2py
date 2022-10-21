# input nilai variabel
a = input("masukkan nilai a")
b = input("masukkan nilai b")

# cetak nilai variabel
print("Variable a=",a)
print("Variable b=",b)

# cetak hasil operasi kedua variabel dengan String Format
print("Hasil Penggabungan (1)&(0)=%".format(a,b)%(a+b))

# konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b)%(a,b))
print("Hasil penjumlahan {1}/{0}=%d".format(a,b)%(a/b))
