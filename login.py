username = "admin"
password =  "12345"

print("Selamat datang di sistem login sederhana!")

input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username == username and input_password == password:
    print("\nLogin berhasil!!!")
    print(f"Selamat datang, {input_username}!")

else:
    print("\nLogin gagal. Username atau password salah.")