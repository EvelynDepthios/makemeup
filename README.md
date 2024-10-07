**Nama        : Evelyn Depthios <br />**
**NPM         : 2306207543 <br />**
**Kelas       : PBP F <br />**

Link : http://evelyn-depthios-makemeup2.pbp.cs.ui.ac.id

[Tugas 2](#tugas-2)

[Tugas 3](#tugas-3)

[Tugas 4](#tugas-4)

[Tugas 5](#tugas-5)

[Tugas 6](#tugas-6)

# Tugas 2 #
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

```python
    INSTALLED_APPS = [
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


# Tugas 3 #
##  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? ##
*Data delivery* sangat penting dalam pengimplementasian sebuah platform untuk memastikan bahwa informasi atau data yang dihasilkan, dikirimkan, dan diterima secara efisien dan tepat waktu antara berbagai komponen platform. Berikut adalah alasan-alasan utama mengapa data delivery penting:
### 1. Efisiensi Operasional ###
*Data delivery* yang efektif memastikan data ditransfer antar sistem atau komponen dengan mulus, dimana hal ini krusial untuk *real-time operations* seperti platform e-commerce atau *financial services* untuk mempercepat proses bisnis dan *decision-making* dengan memberikan akses cepat pada data.
### 2. Integrasi dari Berbagai Sumber Data ###
Platform sering kali perlu menggabungkan dan mengintegrasikan data dari berbagai sumber. Platform data modern seperti yang dibangun di *cloud solution* (misalnya AWS atau Google Cloud) membantu menyederhanakan agregasi, normalisasi, dan integrasi data, memungkinkan bisnis untuk memperoleh wawasan dan membuat keputusan berbasis data​.

### 3. Skalabilitas & Fleksibilitas ###
*Data delivery* mendukung skalabilitas platform dengan memastikan bahwa infrastruktur pengelolaan data dapat berkembang seiring dengan pertumbuhan bisnis, baik untuk menangani big data ataupun memproses model AI, platform data perlu dapat mengelola volume, kecepatan, dan variasi data yang terus meningkat​.

### 4. Keamanan dan Kepatuhan ###
Mekanisme *data delivery* yang aman membantu melindungi informasi sensitif dan memastikan kepatuhan terhadap regulasi seperti GDPR atau CCPA. Tanpa pengiriman data yang kuat, platform rentan terhadap pelanggaran data dan masalah kepatuhan, yang dapat merusak kepercayaan dan operasi bisnis​.

Source : https://www.phdata.io/blog/how-to-implement-a-data-platform/, https://3cloudsolutions.com/resources/the-importance-of-a-modern-data-platform/ 

##  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? ##
- Dari segi sintaks dan strukturnya, JSON ;ebih sederhana dengan format yang lebih *human-readable*. JSON menggunakan objek dan array yang sudah familiar bagi developer, terutama mereka yang bekerja dengan JavaScript, karena JSON adalah subset dari JavaScript. Sedangkan XML, memiliki struktur yang lebih kompleks dengan penggunaan tag yang mirip dengan HTML. XML juga mendukung atribut, elemen, dan teks, yang membuatnya lebih kaya, tetapi lebih sulit dibaca.
- Dari segi ukuran dan kecepatannya, JSON lebih ringan karena tidak memerlukan tag pembuka dan penutup seperti XML. Hal ini dapat mengurangi ukuran file secara signifikan dan mempercepat proses parsing. XML memiliki overhead yang lebih besar karena penggunaan tag yang lebih banyak, sehingga menjadi lebih berat dan lambat untuk diproses.
- Dari segi parsing dan pemrosesan, parsing JSON lebih cepat dan lebih mudah karena sebagian besar bahasa pemrograman modern mendukungnya secara langsung dengan library atau metode bawaan. Parsing XML cenderung lebih kompleks dan membutuhkan parser khusus. XML juga memerlukan lebih banyak pemrosesan untuk mengekstrak data karena strukturnya yang lebih berlapis-lapis.
- Dari segi dukungan data, JSON cocok untuk memuat data struktur seperti objek dan array. JSON lebih cocok untuk data yang tidak memerlukan markup yang rumit. Sedangkan XML memiliki kemampuan markup yang lebih kuat dan mendukung hal-hal seperti skema yang dapat memvalidasi data. XML juga memiliki dukungan untuk namespace dan dokumen yang lebih kompleks, sehingga lebih fleksibel untuk dokumen yang membutuhkan deskripsi yang lebih detail.

Kesimpulannya, JSON lebih populer dibandingkan XML dikarenakan JSON jauh lebih sederhana dan lebih mudah untuk dibaca dan ditulis dibandingkan dengan XML, sehingga lebih menarik bagi developer yang mengutamakan efisiensi. Selain itu, JSON lebih efisien dalam ukuran data dan parsing, sehingga mempercepat transmisi data dan menghemat penggunaan bandwidth. JSON sangat terintegrasi dengan JavaScript, yang menjadikannya populer dalam pengembangan aplikasi web, terutama untuk AJAX dan API. Dukungan JSON yang luas di berbagai bahasa pemrograman dan framework modern menjadikannya pilihan utama untuk banyak aplikasi web, RESTful API, dan layanan berbasis cloud​

Source : https://aws.amazon.com/compare/the-difference-between-json-xml/#:~:text=JSON%20is%20generally%20a%20better,structures%20that%20require%20data%20exchange 

##  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? ##
Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form itu sesuai dengan aturan validasi yang telah ditentukan. Saat method ini dipanggil, Django akan menjalankan serangkaian validasi pada setiap field di form. Jika semua field memiliki data yang valid, method ini akan mengembalikan nilai `True` dan menyimpan data yang telah dibersihkan ke dalam atribut `cleaned_data`, yang kemudian bisa digunakan untuk diproses lebih lanjut, seperti menyimpan data ke database. Jika ada data yang setelah dicek tidak valid, method is_valid() akan mengembalikan `False` dan form akan menyertakan pesan error yang dapat ditampilkan ke *user/client*. Method ini penting karena memastikan bahwa hanya data yang valid yang diproses oleh sistem, sehingga membantu mencegah kesalahan atau potensi serangan seperti *injection* yang dapat terjadi jika data tidak divalidasi dengan baik​.

Source : https://docs.djangoproject.com/en/5.1/topics/forms/#:~:text=A%20Form%20instance%20has%20an,data%20in%20its%20cleaned_data%20attribute, https://docs.djangoproject.com/en/5.1/ref/forms/api/

##  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? ## 
CSRF (Cross-Site Request Forgery) adalah serangan di mana penyerang mencoba membuat *authenticated user* di suatu *sites* untuk melakukan aksi, seperti mengubah pengaturan akun atau mengirim data. Untuk melindungi dari serangan ini, Django menggunakan `csrf_token`, yaitu token unik yang disisipkan di setiap form yang menggunakan metode POST. Token ini kemudian diverifikasi saat form dikirim untuk memastikan bahwa permintaan tersebut memang berasal dari situs yang sah dan bukan dari situs berbahaya yang mencoba menipu *user*.

Jika kita tidak menambahkan `csrf_token`, penyerang bisa memanfaatkan sesi login *user* untuk mengirim permintaan berbahaya tanpa sepengetahuan mereka. Misalnya, jika *user* sudah login di sebuah bank dan mengunjungi situs lain yang berbahaya, situs tersebut dapat membuat *user* mengirim permintaan transfer dana tanpa persetujuan mereka, karena sesi *user* masih aktif di situs bank tersebut. Dengan adanya `csrf_token`, hanya form yang berasal dari situs yang sah yang akan diproses, sehingga melindungi aplikasi dari serangan CSRF yang berpotensi merusak atau merugikan.

Source : https://docs.djangoproject.com/en/5.1/howto/csrf/, https://docs.djangoproject.com/en/5.1/ref/csrf/

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step. ##
### Membuat input form untuk menambahkan objek model pada app sebelumnya. ###
1. Membuat berkas baru pada direktori `main` dengan nama `forms.py` sebagai struktur yang dapat menerima data *Product* baru.
2. Isi file `forms.py` dengan kode berikut:
```python
from django.forms import ModelForm
from main.models import Product

class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "ratings"]
```
Model menunjukkan model yang digunakan dalam *form* dan fields menunjukkan *field* dari model yang digunakan.
3. Buka file `views.py` yang ada pada direktori main dan tambahkan beberapa import pada bagian paling atas.
```python
from django.shortcuts import render, redirect
from main.forms import CreateProductForm
from main.models import Product
```
4. Masih pada file yang sama, tambahkan juga *function* baru dengan nama `create_product_form` untuk menerima request. *Function* tersebut akan memvalidasi input form dan menyimpan data dari *form* tersebut.

``` python
def create_product_form(request):
    form = CreateProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_form.html", context)
```
5. Lalu ubah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut.
```python
def show_main(request):
    main_products = [
        ...
    ]
    product_entries = Product.objects.all()

    new_products = [{'name': Product.name, 'price': Product.price, 'description': Product.description, 'category': Product.category, 'ratings' : Product.ratings} for Product in product_entries]
    
    all_products = main_products + new_products
    
    return render(request, 'main.html', {'products': all_products})
```
`Product.objects.all()` akan mengambil seluruh *Object* Product yang ada pada *database*
6. Buka `urls.py` yang ada pada direktori main dan import fungsi create_product_form yang telah dibuat. `from main.views import show_main, create_product_form`
7. Tambahkan juga path URL ke dalam variabel urlpatterns pada urls.py di folder main untuk mengakses fungsi yang sudah di-import sebelumnya.
``` python
urlpatterns = [
   ...
    path('create-product-form', create_product_form, name='create_product_form'),
]
```
8. Buat file dengan nama `create_product_form.html` pada direktori `main/templates` dan isi dengan kode berikut:
```python
{% extends 'base.html' %}
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <div>
    <input type="submit" value="Add New Product" />
  </div>
</form>

{% endblock %}
```
`<form method="POST">` sebagai *block* untuk *form* deengan metode POST.
`{% csrf_token %}` token yang di-*generate* secara otomatis oleh Django sebagai *security*
`{{ form.as_p }}` menampilkan fields yang sudah dibuat di `forms.py` dalam paragraf
`<input type="submit" value="Add New Product"/>` membuat tombol *submit* untuk mengirimkan *request* ke *function* `create_product_form` di `views.py`
9. Buka file `main.html` dan tambahkan tampilan data produk serta tombol untuk menambahkan produk baru yang akan *redirect* ke halaman *form* melalui penambahan kode berikut ke dalam bagian `{% block content %}`.
```html
    ...
    <div>
        {% for product in products %}
        <div>
            <!-- Nama Produk -->
            <div><strong>{{ product.name }}</strong>
            </div>
            <!-- Harga Produk -->
            <div>Rp {{ product.price }}</div>
            <!-- Deskripsi Produk -->
            <div>{{ product.description }}</div>
            <!-- Kategori Produk -->
            <div>Category: {{ product.category }}</div>
            <!-- Rating Kondisi Produk -->
            <div>Ratings: {{ product.ratings }}/10</div>
        </div>
        <br>
        {% endfor %}
    </div>
</body>
<a href="{% url 'main:create_product_form' %}">
  <button>Add New Product Entry</button>
</a>
<br />
{% endblock content %}
```

### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Buka file `views.py` di folder `main` dan tamabhkan beberapa *import* melalui kode berikut:
```python
from django.http import HttpResponse
from django.core import serializers
```
#### XML ####
Buat sebuah *function* baru yang menerima parameter request dengan nama `show_xml` dan sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product. Tambahkan juga return *function* `HttpResponse` yang berisi parameter data hasil query yang sudah diubah menjadi XML dan parameter `content_type="application/xml`.
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

#### JSON ####
Buat sebuah *function* yang menerima parameter request dengan nama `show_json` dan sebuah variabel di dalam *function* tersebut yang menyimpan hasil query dari seluruh data Product. Tambahkan juga return *function* berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diubah menjadi JSON dan parameter `content_type="application/json"`.
```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### XML by ID ####
Buat sebuah *function* yang menerima parameter *request* dan id dengan nama `show_xml_by_id` dan buat variabel di dalam *function* tersebut yang menyimpan hasil query dari Product sesuai dengan id. Tambahkan juga return *function* berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diubah menjadi XML dan parameter `content_type="application/xml"`.
```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

#### JSON by ID ####
Buat sebuah *function* yang menerima parameter *request* dan id dengan nama `show_json_by_id` dan buat variabel di dalam *function* tersebut yang menyimpan hasil query dari Product sesuai dengan id. Tambahkan juga return *function* berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diubah menjadi JSON dan parameter `content_type="application/json"`.
```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2. ###
1. Buka `urls.py` di dalam folder `main` dan *import* fungsi yang sudah dibuat.
```python
from main.views import show_main, create_product_form, show_xml, show_json, show_xml_by_id, show_json_by_id
```
2. Tambahkan juga path URL ke dalam `urlpattern` di file `urls.py` untuk mengakses *function* yang sudah dibuat dan di-import melalui kode berikut:
```python
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
##  Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md. ## 
### XML ###
![image](https://github.com/EvelynDepthios/makemeup/blob/main/images/ss_xml.png)

### XML by ID 1 ###
![image](https://github.com/EvelynDepthios/makemeup/blob/main/images/ss_xml1.png)

### JSON ###
![image](https://github.com/EvelynDepthios/makemeup/blob/main/images/ss_json.png)

### JSON by ID 2 ###
![image](https://github.com/EvelynDepthios/makemeup/blob/main/images/ss_json2.png)


# Tugas 4 #
##  Apa perbedaan antara HttpResponseRedirect() dan redirect() ##
- `HttpResponseRedirect()` adalah kelas yang digunakan untuk melakukan redirect secara manual dengan memberikan URL tujuan sebagai argumen.
- `redirect()` adalah shortcut dari Django yang mempermudah pembuatan HTTP redirect, karena dapat menerima URL, objek, atau nama URL, dan secara otomatis mengarahkan ke lokasi yang tepat tanpa memerlukan URL string.
Source : https://realpython.com/django-redirects/

##  Jelaskan cara kerja penghubungan model Product dengan User! ##
Penghubungan model Product dengan User dalam Django menggunakan ForeignKey untuk menciptakan relasi one-to-many. Dalam relasi ini, satu pengguna dapat memiliki banyak produk, tetapi setiap produk hanya bisa dimiliki oleh satu pengguna.

Ketika model Product didefinisikan dengan field user yang merupakan ForeignKey ke model User, Django secara otomatis mengelola integritas data. Jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus (karena `on_delete=models.CASCADE`).
```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    ratings = models.IntegerField()
```
Saat pengguna membuat produk baru, informasi tentang pengguna yang login (melalui request.user) ditetapkan ke field user pada produk. 
```python
product.user = request.user
product.save()
```
Ini memungkinkan pengambilan data yang terstruktur, di mana kita dapat dengan mudah query untuk menemukan semua produk yang dimiliki oleh pengguna tertentu. Dengan demikian, Django menjaga keterkaitan antara pengguna dan produk secara efisien dan aman.

##  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut. ##
- Authentication adalah proses memverifikasi identitas pengguna, biasanya dilakukan dengan mencocokkan username dan password.
- Authorization adalah proses memeriksa apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses sumber daya tertentu.
Ketika pengguna login, Django memverifikasi kredensial mereka (authentication). Setelah login, Django menentukan hak akses pengguna ke halaman dan fungsionalitas tertentu berdasarkan izin yang terkait dengan akun pengguna (authorization).
Source : https://www.onelogin.com/learn/authentication-vs-authorization#:~:text=Authentication%20and%20authorization%20are%20two,authorization%20determines%20their%20access%20rights.

##  Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan? ##
Django mengingat pengguna yang login melalui *session cookies*. Ketika pengguna berhasil login, Django membuat *session ID* yang unik dan menyimpannya di server. Session ID ini juga dikirim ke browser sebagai cookie bernama `sessionid`. Setiap kali pengguna melakukan permintaan (request) ke server, cookie ini dikirim bersama permintaan tersebut, memungkinkan Django untuk mengenali pengguna tanpa perlu login ulang. Jika sesi habis atau pengguna logout, session ID akan dihapus, dan pengguna harus login kembali.

Selain mengingat pengguna yang login, cookies memiliki beberapa kegunaan lain, di antaranya:
1. Menyimpan Preferensi Pengguna: Cookies bisa menyimpan pengaturan pribadi, seperti bahasa atau tema situs, sehingga pengalaman pengguna dapat dipersonalisasi.
2. Pelacakan dan Analitik: Cookies digunakan untuk melacak aktivitas pengguna di situs web, membantu pemilik situs memahami perilaku pengguna dan mengoptimalkan konten.
3. Keranjang Belanja: Pada situs e-commerce, cookies menyimpan item di keranjang belanja pengguna, meskipun mereka belum login atau kembali ke situs di lain waktu.
4. Autentikasi Berkelanjutan: Cookies memungkinkan situs mengingat pengguna di kunjungan berikutnya tanpa harus login ulang.
5. Iklan yang Dipersonalisasi: Cookies sering digunakan oleh pengiklan untuk menampilkan iklan yang relevan berdasarkan aktivitas pengguna di berbagai situs web.

Namun, pengguna harus berhati-hati karena beberapa cookies, terutama dari pihak ketiga, dapat menimbulkan masalah privasi. Beberapa risiko terkait cookies meliputi:
1. Pencurian Data: Jika cookie tidak dienkripsi dan dikirim melalui koneksi yang tidak aman (HTTP), data sensitif bisa dicuri oleh pihak ketiga.
2. Serangan XSS (Cross-Site Scripting): Cookies dapat diakses oleh skrip jahat jika tidak diatur sebagai HttpOnly, yang memungkinkan serangan pencurian cookie.
3. Serangan CSRF (Cross-Site Request Forgery): Cookies dapat disalahgunakan untuk melakukan aksi tidak sah jika tidak dilindungi oleh token CSRF.
4. Privasi: Cookies pihak ketiga dapat melacak perilaku pengguna di berbagai situs, menimbulkan masalah privasi.

Untuk meningkatkan keamanan, gunakan HTTPS, atur cookies dengan flag `HttpOnly` dan `Secure`, serta implementasikan proteksi CSRF.

Source : https://www-freecodecamp-org.translate.goog/news/everything-you-need-to-know-about-cookies-for-web-development/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). ##
### Membuat Fungsi Login, Logout, dan Form Registrasi ###
#### Form Registrasi ####
1. Pastikan untuk mengakitfkan *virtual env* terlebih dahulu
2. Tambahkan import berikut pada `views.py` di subdirektori main
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
UserCreationForm adalah formulir bawaan dari Django yang dirancang untuk mempermudah pembuatan formulir pendaftaran pengguna dalam aplikasi web. 

3. Masih di file yang sama, tambahkan fungsi `register` untuk membuat formulir registrasi dan menghasilkan akun pengguna.
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
`form.is_valid()` berfungsi untuk memvalidasi isi form dan `form.save()` digunakan untuk membuat data dan menyimpan data. 
4. Buat berkas HTML baru dengan nama `register.html` pada folder main/templates dan isi dengan kode berikut.
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
5. Tambahkan impor berikut pada file `urls.py` di subdirektori `main` dan *path url* ke `urlpatterns` untuk akses fungsinya.
```python
from main.views import register
...
 urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```
#### Login ####
1. Tambahkan import berikut pada bagian paling atas file `views.py` yang ada pada subdirektori `main`.
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
```
2. Tambahkan fungsi `login_user` ke dalam file `views.py` untuk mengautentikasi pengguna.
```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

3. Buat berkas HTML baru dengan nama `login.html` pada folder main/templates dan isi dengan kode berikut.
```{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}html
```
4. Tambahkan impor berikut pada file `urls.py` di subdirektori `main` dan *path url* ke `urlpatterns` untuk akses fungsinya.
```python
from main.views import login_user
...
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```
#### Logout ####
1. Tambahkan import `logout` pada bagian paling atas file `views.py` di subdirektori main
```python
from django.contrib.auth import logout
```
2. Tambahkan juga fungsi ini di bawahnya untuk melakukan mekanisme logout
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
3. Buka file `main.html` di direktori `main\templates` dan tambahkan kode berikut ini di paling bawah setelah tombol *Add New Product Entry*
```html
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```
4. Tambahkan impor berikut pada file `urls.py` di subdirektori `main` dan *path url* ke `urlpatterns` untuk akses fungsinya.
```python
from main.views import logout_user
...
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```
### Merestriksi Akses Page Main ###
1. Tambahkan import berikut pada `views.py` yang ada di subdirektori `main`
```python
from django.contrib.auth.decorators import login_required
```
Kode ini untuk impor *decorator* yang bisa mengharuskan pengguna login terlebih dahulu untuk akses suatu web.
2. Selanjutnya tambahkan lagi kode potongan berikut di atas fungsi `show_main()`
```python
...
@login_required(login_url='/login')
def show_main(request):
...
```
### Menerapkan *Cookies* dan Detail Informasi Last Login ###
1. Buka `views.py` di dalam subdirektori `main` dan tambahkan impor `HttpResponseRedirect`, `reverse`, dan `datetime`.
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Ganti fungsi pada `login_user` untuk menambahkan *cookie* untuk melihat kapan terakhir kali pengguna *login*. Kode pada blok `if form.is_valid()` diganti menjadi kode berikut.
```python
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
`response.setcookie('last_login', str(datetime.datetime.now()))` berfungsi untuk membuat *cookie* `last_login` dan menambahkannya ke dalam response
3. Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam `context`.
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    ...
}
```
4. Ubah fungsi `logout_user` sesuai dengan kode berikut.
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
`response.delete_cookie('last_login')` berfungsi untuk menghapus *cookie* `last_login` saat pengguna melakukan `logout`.
5. Buka berkas `main.html` pada folder `main/templates` dan isi dengan kode berikut di antara tabel dan tombol *logout* untuk menampilkan data *last login*
```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. ###
1. Jalankan proyek Django dengan perintah `python manage.py runserver`, pastikan virtual env sudah menyala
2. Buka http://localhost:8000/ di browser dan tekan tombol register now
3. Daftarkan diri untuk membuat akun
4. Setelah membuat akun, halaman web akan kembali ke awal dan lakukan login sesuai dengan username dan password yang didaftarkan.
5. Tekan tombol add product untuk menambahkan produk dan lakukan tiga kali untuk menambahkan tiga produk.
6. Tekan tombol logout untuk kembali ke halaman awal dan daftarkan lagi satu akun sesuai dengan langkah nomor 4.
7. Ulangi langkah nomor 5 dan dua akun pengguna dengan masing - masing tiga dummy data sudah terbuat.
<img src = https://github.com/EvelynDepthios/makemeup/blob/main/images/Dummy%20Product%201.png>
<img src = https://github.com/EvelynDepthios/makemeup/blob/main/images/Dummy%20Product%202.png>

### Menghubungkan Product dan User
1. Buka `models.py` pada subdirektori `main` dan tambahkan import berikut.
```python
from django.contrib.auth.models import User
```
2. Tambahkan kode berikut pada model `Product` untuk menghubungkan produk dengan user.
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
3. Buka `views.py` pada subdirektori `main` dan ubah fungsi `create_product` menjadi kode berikut:
```python
def create_product_form(request):
    form = CreateProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user  # Assign the product to the logged-in user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_form.html", context)
...
```
4. Ubah fungsi `show_main` menjadi kode berikut:
```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
...
```
5. Simpan semua perubahan dan migrasi model dengan `python3 manage.py makemigrations` dan `python3 manage.py migrate`.
6. Untuk mempersiapkan aplikasi web untuk environtment production, tambahkan sebuah import baru pada `settings.py` yang ada pada subdirektori proyek dan ganti variabel `DEBUG` menjadi seperti ini.
```python
import os
...
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
...
```

# Tugas 5 #
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas CSS selector diambil berdasarkan spesifisitas dengan urutan sebagai berikut:

1. **Inline Style** (dalam elemen HTML) memiliki prioritas tertinggi.
2. **ID Selector** (`#id`).
3. **Class, Attribute, dan Pseudo-class Selector** (`.class`, `[attr]`, `:hover`).
4. **Tag Selector** (seperti `p`, `h1`, `div`).
5. **Universal Selector** (`*`), yang memiliki prioritas paling rendah.
6. **Important (`!important`)** mengalahkan semua aturan di atas.

Aturan dengan spesifisitas lebih tinggi akan diambil jika beberapa selector diterapkan pada elemen yang sama.
Source : https://www.w3.org/TR/CSS21/cascade.html#specificity

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
**Mengapa responsive design penting:**

Responsive design sangat penting karena memungkinkan situs web untuk menyesuaikan tampilannya sesuai dengan ukuran layar perangkat yang digunakan (desktop, tablet, atau ponsel). Dengan meningkatnya penggunaan perangkat mobile, aplikasi web harus memberikan pengalaman pengguna yang optimal di berbagai ukuran layar. Tanpa responsive design, pengguna di perangkat mobile mungkin mengalami kesulitan dalam navigasi atau membaca konten, yang dapat menyebabkan penurunan tingkat kunjungan dan interaksi.

**Contoh aplikasi:**
- **Sudah menerapkan responsive design:**  
  - **YouTube:** Tampilan video dan navigasi secara otomatis menyesuaikan untuk berbagai perangkat, memastikan pengalaman yang konsisten di desktop dan ponsel.
  - **Twitter:** Baik di desktop maupun mobile, Twitter menyesuaikan layout-nya dengan baik, seperti tampilan feed dan elemen interaktif lainnya.
- **Belum menerapkan responsive design:**  
  - **Situs web lama yang belum diperbarui untuk mobile:** Beberapa situs bisnis kecil atau situs web yang belum menggunakan teknik modern mungkin masih mengalami layout yang terpotong atau tidak responsif ketika diakses dari perangkat mobile.

Source : https://developers.google.com/search/blog/2012/04/responsive-design-harnessing-power-of

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**Perbedaan antara Margin, Border, dan Padding:**

1. **Margin:**  
   - Ruang kosong di luar elemen, yang menciptakan jarak antara elemen tersebut dengan elemen lain di sekitarnya.  
   - **Contoh Implementasi:**
     ```css
     div {
       margin: 20px; /* Jarak 20px dari elemen lain */
     }
     ```

2. **Border:**  
   - Garis yang mengelilingi elemen, terletak di antara margin dan padding. Border dapat memiliki warna, ketebalan, dan gaya.
   - **Contoh Implementasi:**
     ```css
     div {
       border: 2px solid black; /* Border hitam dengan ketebalan 2px */
     }
     ```

3. **Padding:**  
   - Ruang kosong di dalam elemen, yang menciptakan jarak antara konten elemen dengan border elemen tersebut.
   - **Contoh Implementasi:**
     ```css
     div {
       padding: 10px; /* Jarak 10px dari konten ke border */
     }
     ```

**Visualisasi:**
- **Margin** berada di luar elemen,
- **Border** adalah garis di sekeliling elemen,
- **Padding** berada di dalam elemen, antara konten dan border.

Source : https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Flexbox (Flexible Box Layout):**

Flexbox adalah layout model CSS yang dirancang untuk menyusun elemen dalam satu dimensi, baik secara horizontal atau vertikal. Ini memungkinkan elemen-elemen dalam container fleksibel untuk menyesuaikan diri dengan mudah berdasarkan ukuran container dan orientasinya.

**Kegunaan Flexbox:**
- Mengatur elemen secara responsif tanpa perlu menggunakan float atau positioning.
- Memungkinkan elemen untuk menyesuaikan ukuran, jarak, dan urutan dengan mudah di dalam container.
- Sangat cocok untuk membuat layout baris atau kolom.

**Contoh Implementasi:**
```css
.container {
  display: flex;
  justify-content: space-between; /* Mengatur jarak antar elemen */
}
```

**Grid Layout:**

Grid layout adalah sistem layout dua dimensi yang memungkinkan kita untuk membuat struktur layout yang lebih kompleks dengan baris dan kolom. Dengan grid, kita bisa lebih mudah mengatur elemen secara presisi dalam grid yang terdefinisi dengan baik.

**Kegunaan Grid Layout:**
- Ideal untuk membuat layout yang lebih kompleks dengan beberapa baris dan kolom.
- Memudahkan pengaturan elemen dalam baris dan kolom secara fleksibel.
- Dapat digunakan untuk layout responsif dan adaptif dengan grid otomatis yang menyesuaikan ukuran layar.

**Contoh Implementasi:**
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr; /* Membuat dua kolom */
  grid-template-rows: auto;
}
```

**Perbedaan Utama:**
- **Flexbox** lebih cocok untuk layout satu dimensi (baik baris atau kolom).
- **Grid Layout** lebih baik digunakan untuk layout dua dimensi (baris dan kolom).

Source : https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout, https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! 
### 1. Implementasi Fungsi untuk Menghapus dan Mengedit Produk ###
a. Mengedit Produk
1. Di dalam `views.py`, buatlah fungsi `edit_product` yang menerima ID produk dan mengupdate informasi produk. Gunakan `CreateProductForm` sebagai form untuk mengedit produk.
```python
def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = CreateProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_product.html", context)
```
2. Buatlah template `edit_product.html` yang menggunakan form tersebut. Tampilkan field yang ada di `CreateProductForm`.
3. Di template `card_product.html`, buat tautan untuk mengedit produk yang mengarah ke view yang telah dibuat.

b. Menghapus Produk
1. Di dalam `views.py`, buatlah fungsi `delete_product` yang akan menghapus produk berdasarkan ID.sebagai form untuk mengedit produk.
```python
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Di template `card_product.html`, buat tautan untuk menghapus produk yang mengarah ke view yang telah dibuat.

Setelah kedua fungsi telah dibuat, di `urls.py`, buatlah rute URL untuk menghapus dan mengedit produk. Rute ini akan memanggil fungsi di `views.py` yang berfungsi untuk menangani operasi edit dan delete.
```python
from django.urls import path
from main.views import ..., edit_product, delete_product
urlpatterns = [
  ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
]
```

### 2. Kustomisasi Desain pada Template HTML Menggunakan CSS Framework Tailwind ###
Untuk menggunakan Tailwind dalam melakukan styling terhadap aplikasi Django, lakukan langkah-langkah berikut :
1. Buka project Django (make_me_up), buka file `base.html` yang telah dibuat sebelumnya pada templates folder yang berada di root project dan tambahkan potongan kode berikut.
```html
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```
Kode ini berfungsi untuk menyesuaikan ukuran dan perilaku perangkat mobile, serta menyambungkan template Django dengan Tailwind, dengan memanfaatkan script CDN (Content Delivery Network) dari Tailwind untuk diletakkan di dalam html template Django.

2. Untuk menambahkan styles pada Aplikasi dengan Tailwind dan External CSS, buatlah file `global.css` di folder `/static/css`.
3. Pada file `global.css`, kita dapat menambahkan kelas custom atau style css yang sudah didefinisikan sendiri.
4. Ubah file `base.html` agar dapat digunakan dalam template Django, menjadi seperti ini
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
5. Berikut contoh custom styling pada `global.css` 
```css
/* Color Palette */
:root {
    --color-white: #ffffff;
    --color-light-pink-1: #fef0f5; /* Very light pink */
    --color-light-pink-2: #ffd7e3; /* Pastel pink */
    --color-pink-1: #ffbdd3; /* Cotton candy pink */
    --color-pink-2: #ffa3c2; /* Carnation pink */
}

/* Form Styles */
.form-style form input, 
.form-style form textarea, 
.form-style form select {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid var(--color-pink-1); /* Pinkish Border */
    border-radius: 0.5rem; /* Slightly more rounded */
    background-color: var(--color-light-pink-1); /* Light pink background for inputs */
    color: #333; /* Text color */
    transition: all 0.3s ease; /* Smooth transition */
}

.form-style form input:focus, 
.form-style form textarea:focus, 
.form-style form select:focus {
    outline: none;
    border-color: var(--color-pink-2); /* Pink border on focus */
    box-shadow: 0 0 0 3px rgba(255, 163, 194, 0.4); /* Pink glow */
    background-color: #fff; /* Change background to white on focus */
}

/* Animation for shine effect */
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.4), rgba(255, 163, 194, 0.2) 50%, rgba(255, 255, 255, 0.4));
    background-size: 200% 100%;
    animation: shine 3s infinite linear;
}

/* General Button Style */
button {
    background-color: var(--color-pink-2); /* Pink background */
    color: white; /* White text */
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

button:hover {
    background-color: var(--color-pink-1); /* Lighter pink on hover */
    transform: translateY(-3px); /* Slight lift effect */
    box-shadow: 0 8px 15px rgba(255, 173, 196, 0.3); /* Shadow on hover */
}

/* Custom Styles for text input placeholders */
::placeholder {
    color: var(--color-pink-1); /* Light pink for placeholders */
    opacity: 0.7;
}

/* Form label styles */
.form-style form label {
    font-weight: 600;
    color: var(--color-pink-2); /* Pink for form labels */
    margin-bottom: 0.5rem;
}

/* Ratings Bar */
.ratings-bar {
    background-color: var(--color-light-pink-1); /* Light pink background for the bar */
    border-radius: 0.5rem;
}

.ratings-fill {
    background-color: var(--color-pink-2); /* Pink for the filled part */
    height: 100%;
    border-radius: 0.5rem;
}
```
**Kustomisasi halaman *login*, *register*, dan *add* product semenarik mungkin.**
1. Halaman `login`, `register`, dan `add` product dikustomisasi melalui *Tailwind* yang dapat di-search untuk manualnya, contohnya : `login.html`
<details> 
  <summary> Kode `Login.html`</summary>
  ```html
  {% extends 'base.html' %}
  {% load static %}

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}

  {% block content %}
  <div class="min-h-screen flex items-center justify-center w-screen bg-pink-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
      <div>
        <!-- Logo and Title -->
        <img src="{% static 'image/logo.png' %}" alt="Logo" class="mx-auto w-20 h-20 mb-4"> 
        <h1 class="text-4xl font-bold text-center text-black-600">MAKE me UP</h1>
      </div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-pink-600">
        Login to your account
      </h2>
      <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">

        <!-- Input Fields -->
        <div class="rounded-md shadow-sm space-y-4">
          <div>
            <label for="username" class="font-semibold text-black">Username</label>
            <div class="relative">
              <input id="username" name="username" type="text" required class="appearance-none rounded-md relative block w-full px-3 py-2 border border-pink-300 placeholder-pink-400 text-gray-900 focus:outline-none focus:ring-pink-400 focus:border-pink-500 focus:z-10 sm:text-sm" placeholder="Username">
            </div>
          </div>
          <div class="mt-4">
            <label for="password" class="font-semibold text-black">Password</label>
            <div class="relative">
              <input id="password" name="password" type="password" required class="appearance-none rounded-md relative block w-full px-3 py-2 border border-pink-300 placeholder-pink-400 text-gray-900 focus:outline-none focus:ring-pink-400 focus:border-pink-500 focus:z-10 sm:text-sm" placeholder="Password">
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-pink-500 hover:bg-pink-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-400">
            Sign in
          </button>
        </div>
      </form>

      <!-- Messages -->
      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
          <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
          </div>
        {% elif message.tags == "error" %}
          <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
          </div>
        {% else %}
          <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
          </div>
        {% endif %}
        {% endfor %}
      </div>
      {% endif %}

      <!-- Register Link -->
      <div class="text-center mt-4">
        <p class="text-sm text-gray-600">
          Don't have an account yet?
          <a href="{% url 'main:register' %}" class="font-medium text-pink-500 hover:text-pink-600">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```
</details>
Secara garis besar, saya menerapkan palette color dari `global.css` dan sisanya melakukan styling dengan beberapa kelas yang didefinisikan di `global.css` dan juga menggunakan styling dari *Tailwind* untuk desain yang interaktif.

2. Menyesuaikan `register.html` dan `create_product` dengan style CSS dan *Tailwind*diatas agar format web konsisten.
3. Perlu diperhatikan, jika tambahkan tag {% load static %} pada halaman HTML yang mengakses gambar. 

**Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.**
1. Agar lebih interaktif dan menarik, jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
2. Jika sudah ada product yang tersimpan, halaman daftar akan menampilkan detail setiap product dengan menggunakan *card*.

3. Untuk halaman main pada aplikasi ini, saya memutuskan untuk menambahkan *Carousel Photo* yang memungkinkan pengguna untuk melihat beberapa gambar secara bergantian, memberikan pengalaman yang lebih dinamis dan menarik. *JavaScript* berperan penting dalam mengendalikan fungsionalitas carousel, seperti peralihan gambar secara otomatis dan pengendalian navigasi (misalnya, tombol "next" dan "previous"). JavaScript digunakan untuk mengontrol transisi antar gambar dalam carousel.
```html
<!-- Carousel Section -->
<div class="relative flex items-center justify-center mb-6 w-full">

  <!-- Prev Button positioned tightly to the left of the carousel -->
  <button id="prevBtn" class="absolute left-4 transform bg-pink-500 text-white p-5 rounded-full shadow-lg focus:outline-none z-10">&larr;</button> <!-- Updated left positioning -->

  <!-- Carousel Section for Photos -->
  <div class="relative w-full mx-auto overflow-hidden"> <!-- Changed to w-full -->
    <div id="carousel-cards" class="flex transition-transform duration-500 ease-in-out">
      <!-- Card with Image 1 -->
      <div class="bg-white border border-pink-200 shadow-lg rounded-lg p-6 flex items-center justify-center w-full min-w-full flex-shrink-0">
        <img src="{% static 'image/promo1.png' %}" alt="Photo 1" class="w-full h-auto object-cover rounded-lg"/>
      </div>

      <!-- Card with Image 2 -->
      <div class="bg-white border border-pink-200 shadow-lg rounded-lg p-6 flex items-center justify-center w-full min-w-full flex-shrink-0">
        <img src="{% static 'image/promo2.jpg' %}" alt="Photo 2" class="w-full h-auto object-cover rounded-lg"/>
      </div>

      <!-- Card with Image 3 -->
      <div class="bg-white border border-pink-200 shadow-lg rounded-lg p-6 flex items-center justify-center w-full min-w-full flex-shrink-0">
        <img src="{% static 'image/promo3.jpg' %}" alt="Photo 3" class="w-full h-auto object-cover rounded-lg"/>
      </div>
    </div>
  </div>

  <!-- Next Button positioned tightly to the right of the carousel -->
  <button id="nextBtn" class="absolute right-4 transform bg-pink-500 text-white p-5 rounded-full shadow-lg focus:outline-none z-10">&rarr;</button> <!-- Updated right positioning -->

</div> 

<!-- JavaScript for Carousel Controls -->
<script>
  const carousel = document.getElementById('carousel-cards');
  const nextBtn = document.getElementById('nextBtn');
  const prevBtn = document.getElementById('prevBtn');
  let index = 0;

  function autoSwipe() {
    index = (index + 1) % 3; // Adjust according to number of images
    carousel.style.transform = `translateX(-${index * 100}%)`;
  }

  let autoSwipeInterval = setInterval(autoSwipe, 3000);

  nextBtn.addEventListener('click', () => {
    clearInterval(autoSwipeInterval);
    index = (index + 1) % 3;
    carousel.style.transform = `translateX(-${index * 100}%)`;
    autoSwipeInterval = setInterval(autoSwipe, 3000);
  });

  prevBtn.addEventListener('click', () => {
    clearInterval(autoSwipeInterval);
    index = (index - 1 + 3) % 3;
    carousel.style.transform = `translateX(-${index * 100}%)`;
    autoSwipeInterval = setInterval(autoSwipe, 3000);
  });
</script>
```
4. Untuk *product display*, saya membuat `card_product.html` untuk menampilkan informasi produk dan juga tombol untuk *edit* dan *delete* product yang terhubung juga. 
```html
<!-- Products Display -->
  {% if not products %}
  <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
    <p class="text-center text-gray-600 mt-4">Belum ada data product pada MAKE me UP.</p>
  </div>
  {% else %}
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full mb-12">
    {% for product_entry in products %}
      {% include 'card_product.html' with product_entry=product_entry %}
    {% endfor %}
  </div>
```

### 3. Untuk Setiap Card Product, Buatlah Dua Buah Button untuk Mengedit dan Menghapus Product ###
1. Setelah membuat *function* untuk mengedit dan menghapus produk, tambahkan bagian berikut pada `card_product.html` agar dapat diakses / ditekan.
```html
  <!-- Edit and Delete Buttons with Icons -->
  <div class="mt-4 flex space-x-2">
    <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-pink-500 hover:bg-pink-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 flex items-center justify-center">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L7.5 21.036H3v-4.5L16.732 3.732z" />
      </svg>
    </a>

    <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 flex items-center justify-center">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-1 12a2 2 0 01-2 2H8a2 2 0 01-2-2L5 7m5 4v6m4-6v6M10 3h4m-4 0a1 1 0 00-1 1v1h6V4a1 1 0 00-1-1m-4 0h4" />
      </svg>
    </a>
  </div>
```

### 4. Membuat *navigation bar* untuk *mobile* dan *desktop* view ###
1. Buatlah berkas `navbar.html` pada folder templates/ di root directory.
2. Styling `navbar.html` sesuai dengan preferensi, gunakan *Tailwind* agar navbar lebih responsif.
3. Buatlah navbar untuk *desktop* dan *mobile* view seperti ini.
**Desktop View**
```html
<div class="hidden md:flex items-center space-x-4">
  <!-- Links for Desktop View -->
  <a href="{% url 'main:home' %}" class="text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</a>
  <a href="{% url 'main:products' %}" class="text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Products</a>

  <!-- Categories Dropdown -->
  <div class="relative">
    <button id="categoryDropdown" class="text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium flex items-center">
      Categories
      <svg class="ml-1 w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
        <path d="M19 9l-7 7-7-7"></path>
      </svg>
    </button>
    <!-- Dropdown Menu -->
    <div id="dropdownMenu" class="hidden absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none z-50">
      <div class="py-1">
        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Lip Product</a>
        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Eye Product</a>
        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Face Product</a>
        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Body Care</a>
        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Fragrance</a>
      </div>
    </div>
  </div>        
  {% if user.is_authenticated %}
    <a href="{% url 'main:user_info' %}" class="block text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Welcome, {{ user.username }}</a>
    <a href="{% url 'main:logout' %}" class="text-center bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded transition duration-300">
      Logout
    </a>
  {% else %}
    <a href="{% url 'main:login' %}" class="text-center bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
      Login
    </a>
    <a href="{% url 'main:register' %}" class="text-center bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded transition duration-300">
      Register
    </a>
  {% endif %}
</div>
```

**Mobile View**
```html
...
<!-- Hamburger menu for mobile -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  <!-- Mobile menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full bg-pink-200">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
      <!-- Links for Mobile View -->
      <a href="{% url 'main:home' %}" class="block text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</a>
      <a href="{% url 'main:products' %}" class="block text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Products</a>

      <!-- Mobile Categories Dropdown -->
      <div class="relative">
        <button id="mobileCategoryDropdown" class="block text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium flex items-center">
          Categories
          <svg class="ml-1 w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M19 9l-7 7-7-7"></path>
          </svg>
        </button>
        <!-- Mobile Dropdown Menu -->
        <div id="mobileDropdownMenu" class="hidden mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none z-50">
          <div class="py-1">
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Lip Product</a>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Eye Product</a>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Face Product</a>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Body Care</a>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-pink-500 hover:text-white">Fragrance</a>
          </div>
        </div>
      </div>
            
      {% if user.is_authenticated %}
        <a href="{% url 'main:user_info' %}" class="block text-gray-700 hover:bg-pink-500 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Welcome, {{ user.username }}</a>
        <a href="{% url 'main:logout' %}" class="block text-center bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block text-center bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block text-center bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>
```
4. Untuk bagian *categories* meskipun belum bisa responsif, saya menambahkan *drop down menu* dengan menggunakan *JavaScript*
```html
<script>
  const btn = document.querySelector("button.mobile-menu-button");
  const menu = document.querySelector(".mobile-menu");

  btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });

  // Dropdown for Categories (Desktop)
  const categoryDropdown = document.getElementById("categoryDropdown");
  const dropdownMenu = document.getElementById("dropdownMenu");

  categoryDropdown.addEventListener("click", () => {
    dropdownMenu.classList.toggle("hidden");
  });

  // Dropdown for Categories (Mobile)
  const mobileCategoryDropdown = document.getElementById("mobileCategoryDropdown");
  const mobileDropdownMenu = document.getElementById("mobileDropdownMenu");

  mobileCategoryDropdown.addEventListener("click", () => {
    mobileDropdownMenu.classList.toggle("hidden");
  });
</script>
```

# Tugas 6 #
## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
1. **Membuat Website Lebih Menarik**  
JavaScript memungkinkan pengembang untuk membuat aplikasi web yang interaktif dan dinamis. Dengan JavaScript, elemen pada halaman web dapat merespons interaksi pengguna secara langsung, misalnya dengan menambahkan animasi, validasi form, atau pembaruan konten tanpa perlu memuat ulang halaman.

2. **Pengembangan Front-End dan Back-End**  
Awalnya JavaScript hanya digunakan di sisi klien (front-end), tetapi dengan hadirnya Node.js, JavaScript juga dapat digunakan di sisi server (back-end). Hal ini memungkinkan pengembang untuk menggunakan satu bahasa pemrograman di kedua sisi, yang dapat meningkatkan efisiensi pengembangan.

3. **Kompatibilitas di Semua Browser**  
JavaScript didukung oleh semua browser modern, membuatnya menjadi pilihan utama untuk meningkatkan pengalaman pengguna tanpa masalah kompatibilitas antar platform.

4. **Mendukung Asynchronous Programming**  
Dengan JavaScript, pengembang dapat membuat aplikasi web yang cepat dan responsif melalui penggunaan asynchronous programming, seperti AJAX atau Fetch API, untuk memuat data dari server tanpa harus memuat ulang halaman.

5. **Cross-Platform Development**  
JavaScript tidak hanya terbatas pada pengembangan aplikasi web, tetapi juga dapat digunakan untuk pengembangan aplikasi mobile (seperti dengan React Native) dan aplikasi desktop (seperti dengan Electron), memberikan fleksibilitas yang besar bagi pengembang.

Source : https://developer.mozilla.org/en-US/docs/Web/JavaScript, https://www.w3schools.com/js/js_intro.asp

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi dari penggunaan `await` ketika menggunakan `fetch()` adalah untuk menunggu hingga *Promise* yang dihasilkan oleh `fetch()` selesai. Dalam hal ini, `await` memastikan bahwa JavaScript menunggu hingga data dari `fetch()` selesai diambil sebelum melanjutkan ke kode berikutnya. Ini penting karena operasi `fetch()` bersifat *asynchronous*, artinya, permintaan HTTP akan dilakukan di latar belakang, dan JavaScript tidak akan menunggu secara default.

### Penjelasan Fungsi `await` pada `fetch()`:
```javascript
async function getData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  console.log(data);
}
```

Dalam contoh di atas:
1. `await fetch('https://api.example.com/data')` menunggu hingga `fetch()` selesai mengambil data dari URL yang diberikan.
2. Setelah selesai, `response` akan diisi dengan hasil permintaan HTTP tersebut.
3. Proses parsing `response` ke format JSON menggunakan `await response.json()` juga dilakukan setelah data sepenuhnya diambil.

### Apa yang Terjadi Jika Tidak Menggunakan `await`?

Jika tidak menggunakan `await`, fungsi `fetch()` akan langsung mengembalikan sebuah **Promise** yang belum selesai. Ini dapat menyebabkan masalah jika Anda mencoba menggunakan data sebelum proses pengambilan selesai. Sebagai contoh:

```javascript
function getData() {
  const response = fetch('https://api.example.com/data');
  console.log(response);  // Ini akan mencetak sebuah Promise, bukan hasil data.
}
```

Dalam kode di atas, `console.log(response)` akan mencetak **Promise** yang masih pending (belum selesai) karena `fetch()` belum selesai mengambil data. Anda tidak akan mendapatkan data yang sesungguhnya sampai Promise tersebut selesai, sehingga pemrosesan data tidak bisa dilakukan secara langsung.

- **Dengan `await`:** JavaScript akan menunggu hasil dari `fetch()` sebelum melanjutkan eksekusi.
- **Tanpa `await`:** Anda hanya akan mendapatkan Promise yang belum selesai dan harus menanganinya dengan cara lain, misalnya dengan `.then()`.

Menggunakan `await` adalah cara yang lebih sederhana dan lebih mudah dibaca dibandingkan dengan pendekatan `then()` pada **Promises**.

Source : https://www.w3schools.com/js/js_async.asp, https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
 
## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Kita perlu menggunakan decorator `@csrf_exempt` pada view yang akan digunakan untuk *AJAX POST* dalam situasi tertentu untuk menonaktifkan mekanisme **Cross-Site Request Forgery (CSRF) protection** pada view tersebut. Berikut alasannya:
1. **CSRF Protection Secara Default**  
Django memiliki *CSRF protection* secara default untuk semua request POST, terutama untuk melindungi aplikasi dari serangan CSRF. CSRF adalah serangan yang memanfaatkan kepercayaan pengguna yang telah login terhadap situs tertentu untuk mengirimkan permintaan berbahaya tanpa sepengetahuan pengguna.

2. **AJAX POST Request**  
Ketika mengirimkan request POST melalui AJAX, seringkali CSRF token harus disertakan dalam request agar permintaan POST diizinkan oleh Django. Jika CSRF token tidak disertakan atau tidak dikonfigurasi dengan benar, Django akan memblokir request POST dan mengembalikan error **403 Forbidden**.

3. **Penggunaan `@csrf_exempt`**  
`@csrf_exempt` digunakan untuk menonaktifkan pemeriksaan CSRF hanya pada view tertentu. Ini bisa diperlukan dalam situasi di mana kita tidak bisa atau tidak ingin menangani token CSRF di sisi klien, misalnya untuk request API atau AJAX tertentu.

4. **Risiko Penggunaan `@csrf_exempt`**  
Menggunakan `@csrf_exempt` berarti kita menonaktifkan proteksi keamanan CSRF pada view tersebut. Oleh karena itu, kita harus berhati-hati dan memastikan view yang diberi decorator `@csrf_exempt` hanya digunakan dalam konteks yang aman, seperti untuk endpoint API yang memerlukan autentikasi lain atau di mana tidak ada risiko serangan CSRF.

Source : https://docs.djangoproject.com/en/5.1/ref/csrf/,https://developer.mozilla.org/en-US/docs/Glossary/CSRF
 
## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
1. **Keamanan Data yang Lebih Terjamin**  
Frontend (misalnya, melalui JavaScript) berjalan di browser pengguna, dan pengguna bisa memodifikasi kode frontend, mengabaikan validasi atau bahkan memasukkan data yang tidak aman. Oleh karena itu, jika validasi hanya dilakukan di frontend, aplikasi masih rentan terhadap serangan seperti **SQL injection**, **XSS (Cross-Site Scripting)**, dan berbagai bentuk lainnya. Backend adalah tempat yang aman karena pengguna tidak dapat mengubah kode server.

2. **Menjaga Integritas dan Konsistensi**  
Validasi di frontend dapat dihindari atau dimanipulasi, sementara backend tidak bisa diakses langsung oleh pengguna, sehingga pembersihan data di backend memastikan integritas data yang masuk ke sistem tetap terjaga. Ini membantu memastikan data yang diterima oleh aplikasi adalah data yang bersih dan valid, meskipun ada upaya manipulasi dari sisi klien.

3. **Konsistensi Antar Platform**  
Jika aplikasi web Anda memiliki berbagai klien (seperti mobile apps, third-party API clients, atau command-line tools), melakukan validasi di backend memastikan bahwa aturan validasi diterapkan secara konsisten di semua platform, bukan hanya di satu antarmuka.

4. **Frontend untuk Pengalaman Pengguna (UX)**  
Meskipun validasi di frontend bermanfaat untuk memberikan pengalaman pengguna yang lebih baik dengan memberikan umpan balik secara langsung, tetap penting untuk menganggap frontend hanya sebagai lapisan pertama validasi. Backend harus tetap bertanggung jawab untuk memastikan bahwa input yang diterima sepenuhnya aman.

Source : https://docs.djangoproject.com/en/5.1/topics/security/, https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
 
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
### AJAX GET
**Mengubah kode cards data product agar dapat mendukung AJAX GET dan melakukan pengambilan data product menggunakan AJAX GET (data yang diambil hanyalah data milik pengguna yang logged-in.)**
1. Buka file `views.py` dan hapus dua baris ini :
```python
...
product_list = Product.objects.filter(user=request.user)
...
'products': product_list,
```
2. Ubah juga baris pertama views untuk `show_json` dan `show_xml` menjadi seperti ini :
```python
data = Product.objects.filter(user=request.user)
```
3. Hapus barisan kode 
```html
{% if not products %}
  <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
    <p class="text-center text-gray-600 mt-4">Belum ada data product pada MAKE me UP.</p>
  </div>
  {% else %}
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full mb-12">
    {% for product_entry in products %}
      {% include 'card_product.html' with product_entry=product_entry %}
    {% endfor %}
  </div>
  {% endif %}
```
4. Ganti menjadi kode berikut :
```python
  <div id="product_entry_cards"></div>
```
Bagian div yang menampilkan kartu produk harus diberi ID atau kelas CSS untuk target pengisian data produk yang diperoleh via AJAX.
5. Buatlah block `<script>` di bagian bawah berkas (sebelum {% endblock content %}) dan buatlah fungsi baru pada block `<script>` tersebut dengan nama `getProductEntries` dan `refreshProductEntries` yang digunakan untuk me-refresh data product secara asinkronus.
```html
<script>
  // Fetch Product Entries
  async function getProductEntries() {
    return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

  // Refresh Product Entries
  async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries();
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data product pada MAKE me UP.</p>
            </div>
        `;
    } else {
      classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-6 gap-y-6 w-full";
      productEntries.forEach((item) => {
          const brand = DOMPurify.sanitize(item.fields.brand);
          const product_name = DOMPurify.sanitize(item.fields.product_name);
          const description = DOMPurify.sanitize(item.fields.description);
          htmlString += `
          <div class="relative bg-white shadow-lg rounded-lg p-6 mb-6 flex flex-col justify-between border border-pink-200 w-full transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
              <div class="absolute top-4 right-4">
                  <span class="bg-pink-100 text-pink-500 text-xs font-bold py-1 px-2 rounded-full">${item.fields.category}</span>
              </div>
              <div class="flex flex-col">
                  <h3 class="text-pink-700 font-bold text-lg mb-1">${item.fields.brand}</h3>
                  <h4 class="text-gray-900 font-semibold text-lg mb-1">${item.fields.product_name}</h4>
                  <p class="text-gray-500 text-sm mb-2">${item.fields.description}</p>
                  <p class="text-pink-600 font-bold text-lg">Rp ${item.fields.price}</p>
              </div>
              <div class="flex items-center mt-2">
                  <div class="flex items-center text-pink-500">
                      ${generateStarRating(item.fields.ratings)}
                      <span class="ml-2 text-gray-600">${item.fields.ratings}</span>
                  </div>
              </div>
              <div class="flex space-x-2 mt-4">
                  <a href="/edit-product/${item.pk}" class="bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded-lg flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                      </svg>
                      Edit
                  </a>
                  <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                      </svg>
                      Delete
                  </a>
              </div>
          </div>
          `;
      });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
  }
  refreshProductEntries();
</script>
```
Pada kode ini, `document.getElementById("product_entry_cards")` digunakan untuk mengambil elemen `div` tempat kartu produk ditampilkan, lalu `innerHTML` dipakai untuk mengosongkan dan memperbarui isinya dengan data produk yang diambil melalui fungsi AJAX GET (`getProductEntries()`). Data produk diproses dalam `forEach` loop, di mana setiap produk dikonversi menjadi elemen HTML dengan tampilan kartu, disanitasi menggunakan `DOMPurify` untuk keamanan. Fungsi `refreshProductEntries()` bertugas memperbarui daftar produk secara asinkron, memeriksa apakah data kosong atau tidak, dan mengatur ulang kelas CSS elemen untuk menampilkan produk dalam layout grid. Jika tidak ada produk, pesan "Belum ada data product" akan muncul.

### AJAX POST
**Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.**
1. Di bawah kode `<div id="product_entry_cards"></div>`, tambahkan potongan kode ini :
```html
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
  <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out max-h-[90vh] overflow-y-auto">
    <!-- Modal header -->
    <div class="flex items-center justify-between p-4 border-b rounded-t">
      <h3 class="text-xl font-semibold text-gray-900">
        Add New Product Entry
      </h3>
      <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Close modal</span>
      </button>
    </div>
    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style max-h-[70vh] overflow-y-auto">
      <form id="productEntryForm" method="POST">
        {% csrf_token %}
        <div class="mb-4">
          <label for="brand_name" class="block text-sm font-medium text-gray-700">Brand Name</label>
          <input type="text" id="brand_name" name="brand_name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter brand name" required>
        </div>

        <div class="mb-4">
          <label for="product_name" class="block text-sm font-medium text-gray-700">Product Name</label>
          <input type="text" id="product_name" name="product_name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product name" required>
        </div>

        <div class="mb-4">
          <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
          <textarea id="description" name="description" rows="3" class="mt-1 block w-full resize-none border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product description" required></textarea>
        </div>

        <div class="mb-4">
          <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
          <select id="category" name="category" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" required>
            <option value="Lip Product">Lip Product</option>
            <option value="Eye Product">Eye Product</option>
            <option value="Face Product">Face Product</option>
            <option value="Body Care">Body Care</option>
            <option value="Hair Care">Hair Care</option>
            <option value="Fragrance">Fragrance</option>
          </select>
        </div>

        <div class="mb-4">
          <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
          <div class="flex">
            <span class="inline-flex items-center px-3 bg-pink-100 text-gray-900 border border-pink-300 rounded-l-md">
              Rp
            </span>
            <input type="number" id="price" name="price" class="form-input w-full rounded-r-md border-pink-300 focus:ring-pink-500 focus:border-pink-500" placeholder="Enter price" required>
          </div>
        </div>

        <div class="mb-4">
          <label for="ratings" class="block text-sm font-medium text-gray-700">Ratings (1-5)</label>
          <input type="number" id="ratings" name="ratings" min="1" max="5" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product rating" required>
        </div>
      </form>
    </div>
    
    <!-- Modal footer -->
    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
      <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-pink-500 hover:bg-pink-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
      <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
    </div>
  </div>
</div>
```
2. Tambahkan fungsi JavaScript berikut :
```html
<script>
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
</script>
```
Fungsi `showModal()` dan `hideModal()`: Fungsi `showModal()` digunakan untuk menampilkan modal, dan `hideModal()` untuk menutup modal. Modal ini akan muncul saat tombol "Add New Product Entry by AJAX" diklik. 
3. Ubahlah bagian tombol Add New Product Entry untuk melakukan penambahan data dengan AJAX.
```html
<!-- Add New Product Button -->
 ...
  <a href="{% url 'main:create_product_entry' %}" class="bg-gradient-to-r from-pink-500 via-pink-400 to-pink-300 hover:from-pink-300 hover:to-pink-500 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:scale-105 shadow-lg">
    Add New Product Entry
  </a>
  <!-- Add New Product by AJAX Button -->
  <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="bg-gradient-to-r from-pink-500 via-pink-400 to-pink-300 hover:from-pink-300 hover:to-pink-500 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:scale-105 shadow-lg" onclick="showModal();">
    Add New Product Entry by AJAX
  </button>    
  ...
```

**Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.**
1. Tambahkan kedua import berikut pada file `views.py` dan fungsi baru `create_product_entry_ajax` yang menerima parameter request.
```python
...
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
...
@csrf_exempt
@require_POST
def create_product_entry_ajax(request):
    brand = strip_tags(request.POST.get('brand'))
    product_name = strip_tags(request.POST.get('product_name'))
    price = request.POST.get('price')
    description = strip_tags(request.POST.get('description'))
    category = request.POST.get('category')
    ratings = request.POST.get('ratings')
    user = request.user

    product_entry = Product(
        user=user,
        brand=brand,
        product_name=product_name,
        price=price,
        description=description,
        category=category,
        ratings=ratings
    )
    product_entry.save()
    return HttpResponse(b"CREATED", status=201)
```
Decorator `@csrf_exempt` digunakan untuk menonaktifkan pengecekan CSRF token pada request, sehingga Django tidak akan memverifikasi CSRF untuk fungsi ini. `@require_POST` memastikan bahwa fungsi hanya dapat diakses melalui POST request, dan akan mengembalikan error 405 Method Not Allowed jika pengguna mengirim request dengan metode lain. Pada bagian `request.POST.get()`, data yang dikirimkan melalui form diambil secara manual, seperti `brand`, `product_name`, `price`, `description`, `category`, dan `ratings`, dengan menggunakan `strip_tags()` untuk membersihkan input dari HTML tags yang mungkin berbahaya. Selanjutnya, objek baru `Product` dibuat menggunakan data yang diterima, di mana atribut seperti `user`, `brand`, dan `product_name` diisi dari request. Setelah itu, produk baru tersebut disimpan ke dalam basis data dengan `product_entry.save()`, dan Django mengembalikan status 201 (Created) untuk menunjukkan bahwa produk berhasil ditambahkan.

**Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.**
1. Buka file `urls.py` di main/templates, dan tambahkan kode berikut :
```python
from django.urls import path
from .views import create_product_entry_ajax

urlpatterns = [
    # path lainnya
    path('create-product-entry-ajax', create_product_entry_ajax, name='create_product_entry_ajax'),
]
```

**Hubungkan form yang telah dibuat di dalam modal kamu ke path /create-ajax/.**
Dalam form modal yang dibuat di HTML, pastikan form diarahkan ke path /create-ajax/. Namun, karena kita akan menggunakan AJAX POST, kita tidak akan langsung mengarahkan form menggunakan atribut action, melainkan kita akan menangani submit form dengan JavaScript. Berikut adalah fungsi JavaScript untuk menangani submit form secara asinkronus. Saat form disubmit, data akan dikirim ke path /create-ajax/ tanpa me-reload halaman, dan setelah produk berhasil ditambahkan, daftar produk akan di-refresh menggunakan fungsi refreshProductEntries().
```html
<script>
  function createProductEntry() {
    fetch("{% url 'main:create_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries())

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

  document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    createProductEntry();
  })
</script>
```
`new FormData(document.querySelector('#productEntryForm'))` digunakan untuk membuat objek FormData baru yang berisi data dari form pada modal. Objek FormData ini memungkinkan data form dikirimkan ke server menggunakan metode `POST` secara asinkronus tanpa perlu melakukan reload halaman. 

`document.getElementById("productEntryForm").reset()` digunakan untuk mengosongkan atau mereset isi field dalam form modal setelah data produk berhasil dikirim dan disubmit, sehingga form kembali ke kondisi kosong siap diisi ulang.

`document.getElementById("productEntryForm")` digunakan untuk mengambil elemen form dengan ID `productEntryForm` dari DOM, yaitu form di modal untuk menambahkan produk. `addEventListener("submit", ...)` menambahkan event listener ke form tersebut, yang akan memanggil fungsi callback saat form di-submit. `e => {...}` adalah callback yang ditulis dengan notasi arrow function ES6, yang akan dijalankan saat form di-submit. `e.preventDefault()` digunakan untuk mencegah perilaku default form yang biasanya mengirimkan data ke URL di atribut `action`, karena kita menggunakan AJAX untuk mengirim data. `createProductEntry()` kemudian dipanggil untuk menambahkan produk secara asinkronus.

**Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan.**
Setelah produk berhasil ditambahkan ke basis data, kita perlu melakukan refresh daftar produk secara dinamis tanpa reload seluruh halaman. Untuk itu, gunakan fungsi `refreshProductEntries()` (sebelumnya sudah ditambahkan di atas) yang memanggil data produk terbaru melalui AJAX GET dan memperbarui tampilan produk:
- Ketika pengguna menambahkan produk baru melalui modal, data produk dikirimkan ke /create-ajax/ secara asinkronus.
- Setelah produk baru berhasil ditambahkan, daftar produk diperbarui secara otomatis tanpa reload halaman.
- Fungsi refreshProductEntries() digunakan untuk mengambil dan menampilkan daftar produk terbaru menggunakan AJAX GET.