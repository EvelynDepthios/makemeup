Nama        : Evelyn Depthios <br />
NPM         : 2306207543 <br />
Kelas       : PBP F <br />

Link : http://evelyn-depthios-makemeup2.pbp.cs.ui.ac.id

[Tugas 2](#tugas-2)

[Tugas 3](#tugas-3)

[Tugas 4](#tugas-4)


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
