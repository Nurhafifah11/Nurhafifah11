kata = input("Masukkan Kalimatmu : ") 

daftar = {}
for karakter in kata: 
    if karakter in daftar: 
        daftar[karakter] += 1  
    else:
        daftar[karakter] = 1  

print(len(daftar))   