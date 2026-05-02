# 🚀 FastAPI Auth API — Tutorial Lengkap (Run & Testing)

Tutorial ini menjelaskan cara menjalankan API FastAPI sederhana (Register & Login dengan JWT) serta cara mengetesnya menggunakan HTTPie.

---

## 📦 1. Persiapan

Pastikan kamu sudah install Python (disarankan 3.9+).

### Install dependency:

```bash
pip install fastapi uvicorn python-multipart python-jose passlib[bcrypt]
```

---

## 📂 2. Struktur Project

```bash
fast-api-web/
│
├── app/
│   ├── coba.py
│   └── users.json
```

---

## ▶️ 3. Menjalankan Server

Masuk ke folder project:

```bash
cd fastapi-app
```

Jalankan server:

```bash
uvicorn fast-api-web.coba:app --reload
```

Jika berhasil, akan muncul:

```bash
Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 4. Akses API

Buka di browser:

* Swagger Docs (untuk testing manual):

```
http://127.0.0.1:8000/docs
```

---

## 🧪 5. Testing dengan HTTPie

### 🔐 Register User

```bash
http POST :8000/register username=fatan password=12345
```

Response berhasil:

```json
{
  "message": "Register berhasil"
}
```

---

### 🔑 Login User

```bash
http POST :8000/login username=fatan password=12345
```

Response:

```json
{
  "access_token": "TOKEN_KAMU",
  "token_type": "bearer"
}
```

⚠️ Simpan `access_token`, akan dipakai di langkah berikutnya.

---

### 🔒 Akses Endpoint Protected

Gunakan token dengan format `Bearer`:

```bash
http GET :8000/profile Authorization:"Bearer TOKEN_KAMU"
```

Contoh:

```bash
http GET :8000/profile Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

Response:

```json
{
  "user": {
    "sub": "fatan",
    "exp": 1777728784
  }
}
```

---

## ❌ Error yang Sering Terjadi

### 1. 401 Unauthorized

* Lupa pakai `Bearer`
* Token salah / expired

---

### 2. 422 Unprocessable Entity

* Format request salah
* Field tidak lengkap

---

### 3. 400 Bad Request

* User tidak ditemukan
* Password salah

---

## ✅ Checklist API Berhasil

Pastikan semua ini berjalan:

* [x] Register user berhasil
* [x] Login menghasilkan token
* [x] Endpoint protected bisa diakses dengan token
* [x] Tanpa token → ditolak (401)

---

## 💡 Tips

* Gunakan `/docs` untuk testing cepat
* Gunakan HTTPie untuk simulasi real request
* Simpan token di environment variable agar lebih praktis

Contoh:

```bash
TOKEN="eyJhbGc..."
http GET :8000/profile Authorization:"Bearer $TOKEN"
```

---

## 🎯 Selanjutnya

Setelah ini, kamu bisa:

* Menghubungkan API ke frontend (Vue/React)
* Mengganti penyimpanan user ke database (SQLite/MySQL)
* Menambahkan fitur seperti logout, refresh token, dll

---

Happy coding 🚀
