#bikin object JSON untuk menyimpan data profil_dev
profil_dev = {
    "Nickname": "Nala Goodman",
    "role": "Developer, Frontend, Ui/UX Designer",
    "description": "I am a passionate frontend developer and UI/UX designer with a keen eye for creating visually appealing and user-friendly interfaces.",
    "tools": ["HTML", "CSS", "JavaScript", "React", "Figma", "Adobe XD"],
    "kopi_hari_ini": 2
}

#manggil data profil_dev
print(f"nama: {profil_dev['Nickname']}")
print(f"role: {profil_dev['role']}")
print(f"deskripsi: {profil_dev['description']}")
print(f"tools yang digunakan: {profil_dev['tools'][3]} dan {profil_dev['tools'][4]}")