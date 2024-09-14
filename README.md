Nama        : Evelyn Depthios <br />
NPM         : 2306207543 <br />
Kelas       : PBP F <br />

Link : http://evelyn-depthios-makemeup2.pbp.cs.ui.ac.id

# Tugas 2
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial) ##

### Membuat Sebuah proyek Django baru ###
1. Membuat direktori baru, lalu buka command prompt dan buat virtual env dengan menjalankan perintah `python3 -m venv ennv` untuk macOS untuk dependencies package.
2. Aktifkan virtual env dengan menjalankan `source env/bin/activate` (macOS)
3. Buatlah sebuah file dalam direktori sama dengan nama `requirements.txt` dan isi dengan dependencies berikut
`django`
`gunicorn`
`whitenoise`
`psycopg2-binary`
`requests`
`urllib3`
4. Install dependencies dengan perintah berikut `pip install -r requirements.txt` (pastikan virtual env aktif)
5. Buatlah projek Django sesuai dengan nama yang diinginkan dengan perintah berikut `django-admin startproject make_me_up .`
6. Buka file settings.py dalam folder yang telah terbuat, dan ubah ALLOWED_HOSTS menjadi `ALLOWED_HOSTS = ["localhost", "127.0.0.1"]`
7. Buka command prompt dan jalankan perintah `python3 manage.py runserver` (macOS) dan cek http://localhost:8000 untuk melihat apakah aplikasi Django berhasil dibuat.
8. Untuk mengentikan server, tekan `Ctrl+C` di command prompt dan tuliskan perintah `deactivate` untuk mematikan virtual env. 
9. Push hasil perubahan ke GitHub dan PWS

### Membuat aplikasi dengan nama main pada proyek tersebut ###
1. Mengaktifkan virtual environment dengan perintah `source env/bin/activate` (macOS).
2. Jalankan perintah `python3 manage.py startapp main` (macOS) untuk membuat aplikasi baru dengan nama main.
3. Buka file settings.py di dalam proyek Django dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 
```INSTALLED_APPS = [
    ...,
    'main'
]
```

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main ###
1. Buat file dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur route URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
show_main digunakan sebagai tampilan ketika URL terkait diakses dan app_name sebagai nama unik pada pola URL aplikasi.

2. Buka file `urls.py` di direktori proyek Django, bukan `urls.py` yang di direktori `main` dan tambahkan route URL seperti berikut:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
Berkas `urls.py` pada proyek mengatur rute URL utama. Fungsi include digunakan untuk memuat rute dari aplikasi lain (seperti `main`). Path URL kosong ('') memungkinkan aplikasi main diakses langsung sebagai halaman utama.

### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut ###
1. Buka file `models.py` dan isi file dengan nama dan atribut yang wajib ada : `name`, `price`, `description`.
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
```
2. Jalankan perintah `python3 manage.py makemigrations` dan `python3 manage.py migrate` (macOS) untuk mengaplikasikan perubahan model.

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. ###
1. Buka file `views.py` dalam direktori `main`.
2. 2. Tambahkan kode dan function berikut ke dalam file.
```python 
from django.shortcuts import render

def show_main(request):
    # Data produk didefinisikan secara manual dalam bentuk list of dictionaries
    products = 
        {
            'name': 'Lip Butter Balm for Hydration & Shine',
            'price': 24000,
            'description': 'Moisturizing lip balm for hydration and shine.',
        }
    return render(request, 'main.html', products)
``` 
3. Buat folder dengan nama `templates` di dalam folder main dan buat file dengan nama `main.html`, lalu isi dengan kode html untuk menampilkan data di `views.py`.
```html
<div>
    <div>{{ product.name }}</div>
    <div>Rp {{ product.price }}</div>
    <div>{{ product.description }}</div>
</div>
```

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py ###
1. Buat berkas dengan nama `urls.py` dalam folder `main` dan isi dengan kode berikut untuk mengatur route URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

###  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet ###
1. Buka web PWS (https://pbp.cs.ui.ac.id/) dan buatlah akun.
2. Setelah berhasil login, buat projek baru dengan tekan tombol `Create New Project`. Setelah diarahkan ke halaman lain, isi `Project Name` dengan nama sesuai yang diinginkan. Lalu, tekan `Create New Project`
3. Akan muncul dua informasi, Project Credentials dan Project Command. Simpan credentials yang diperoleh di tempat yang aman, karena seterusnya credentials ini tidak akan bisa dilihat lagi. 
4. Pada `settings.py` di proyek Django yang sudah dibuat tadi, tambahkan URL deployment PWS pada ALLOWED_HOSTS.
```python
...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "evelyn-depthios-makemeup.pbp.cs.ui.ac.id"]
...
```
5. Lakukan git add, commit, dan push perubahan ke repo GitHub.
6. Jalankan perintah Project Command Prompt sebelumnya pada halaman PWS. 
```
git remote add pws http://pbp.cs.ui.ac.id/evelyn.depthios/makemeup
git branch -M main
git push pws main
```
7. Apabila statusnya masih `Building`, artinya proyek masih dalam proses deployment. Apabila statusnya `Running`, maka proyek sudah bisa diakses pada URL deployment. Tekan tombol `View Project` yang terdapat pada halaman proyek untuk melihat keberhasilan.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html ##
![image](https://github.com/user-attachments/assets/b4791769-68e1-465f-a5c8-749fce13046c)

Diagram tersebut menggambarkan alur siklus request-response dalam aplikasi web Django. Ketika klien mengirimkan permintaan (request), permintaan tersebut pertama kali diterima oleh urls.py, yang bertanggung jawab untuk memetakan URL yang diminta ke fungsi yang sesuai di views.py. Fungsi dalam views.py kemudian memproses permintaan tersebut; jika membutuhkan data dari basis data, fungsi ini akan berinteraksi dengan models.py, yang merupakan representasi dari struktur basis data dan berfungsi sebagai ORM (Object-Relational Mapping). Setelah data diperoleh, views.py mengirimkan data tersebut ke template HTML untuk dirender. Template tersebut kemudian menghasilkan halaman web yang akan dikirim kembali sebagai respons ke klien, menyelesaikan siklus komunikasi
Source : PPT Fasilkom UI, https://intellipaat.com/blog/tutorial/python-django-tutorial/

## Jelaskan fungsi git dalam pengembangan perangkat lunak! ##
Git adalah sistem kontrol versi yang berfungsi untuk:
1. Melacak perubahan: Git mencatat setiap perubahan yang dilakukan pada kode, sehingga memudahkan pengembang untuk melihat riwayat perubahan.
2. Kolaborasi: Git memungkinkan beberapa pengembang bekerja pada proyek yang sama secara bersamaan tanpa bentrok, karena masing-masing bisa bekerja di branch terpisah.
3. Branching dan Merging: Pengembang dapat bekerja di fitur atau bagian kode yang berbeda secara paralel dan kemudian menggabungkannya (merge) ketika siap.
4. Revert Perubahan: Jika ada kesalahan pada versi terbaru, Git memungkinkan kita untuk kembali ke versi sebelumnya dengan mudah.
Source : https://dcloud.co.id/blog/apa-itu-git.html

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? ##
1. Framework yang Komprehensif: Django menyediakan banyak fitur bawaan yang sangat membantu bagi pemula, seperti autentikasi, manajemen user, serta ORM untuk database.
2. Konvensi Berbasis Konfigurasi: Django menyediakan banyak aturan dan praktik terbaik yang membuat pengembang tidak perlu melakukan konfigurasi berlebihan.
3. Documentasi yang Baik: Django memiliki dokumentasi yang lengkap dan jelas, sehingga memudahkan pemula dalam belajar.
4. Keamanan Bawaan: Django memiliki fitur keamanan bawaan yang melindungi dari ancaman umum seperti SQL Injection dan Cross-Site Scripting (XSS).
Source : https://www.jagoanhosting.com/blog/django/

## Mengapa model pada Django disebut sebagai ORM? ##
ORM (Object-Relational Mapping) adalah teknik yang memungkinkan kita berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL secara langsung. Model Django disebut sebagai ORM karena:
1. Representasi Data sebagai Objek: Setiap tabel di database direpresentasikan sebagai kelas Python, dan setiap baris pada tabel tersebut adalah objek dari kelas tersebut.
2. Abstraksi Database: Kita tidak perlu menulis query SQL secara manual. Django ORM akan secara otomatis menerjemahkan operasi Python ke dalam query SQL yang sesuai.
3. Dukungan untuk Berbagai Database: ORM memungkinkan kita berpindah dari satu database ke database lainnya tanpa mengubah kode Python, hanya dengan mengubah konfigurasi di `settings.py`.
Source : https://rumahcoding.co.id/pengantar-django-orm-memahami-dan-menggunakan-model-dalam-django/
