import requests

def cari_github_profile():
    print("Mencari profil GitHub...")

    username = input("Masukkan username GitHub: ")

    #user ux menghapus spasi di awal dan akhir username
    username = username.strip()

    print(f"Mencari profil GitHub untuk username: {username}")

    #url API GitHub
    url = f"https://api.github.com/users/{username}"

    #tarik requeast ke API GitHub
    response = requests.get(url)

    # handling reponse
    if response.status_code == 200:
        data_user = response.json()
        print("Profil GitHub ditemukan:")
        print(f"Nama: {data_user['name']}")
        print(f"Username: {data_user['login']}")
        print(f"Bio: {data_user['bio']}")
        print(f"Repositori Publik: {data_user['public_repos']}")
        print(f"Followers: {data_user['followers']}")
        print(f"Following: {data_user['following']}")
    elif response.status_code == 404:
        print(f"Gagal mendapatkan profil GitHub. Status code: {response.status_code}")
    else:
        print(f"Terjadi kesalahan saat mencari profil GitHub. Status code: {response.status_code}")

if __name__ == "__main__":
    cari_github_profile()
