#import library
import requests

print("Testing API...")

#API endpoint
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

#handling response
if response.status_code == 200:
    data_user = response.json()
    print("Data user berhasil didapatkan:")
    print(f"Nama: {data_user['name']}")
    print(f"Email: {data_user['email']}")
    print(f"Alamat: {data_user['address']['street']}, {data_user['address']['city']}") #maggil banyak
else:
    print(f"Gagal mendapatkan data user. Status code: {response.status_code}")