nilai = input("Masukkan nilai: ")
nilai = int(nilai)

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid. Nilai harus antara 0 dan 100.")

elif nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 60:
    print("Nilai D")
else:
    print("Nilai E")