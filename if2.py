username = "admin"
password = "123"

username_input = input('masukan username: ')
password_input = input('masukan password: ')

if username_input == username and password_input == password:
    print('login berhasil')
else:    
    print('login gagal')