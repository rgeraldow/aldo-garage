# Aldo's Garage

**Tugas 2 PBP - Kelas B**

> **Aldo's Garage** merupakan proyek Django sederhana berbentuk e-commerce berbasis website untuk memenuhi Tugas Individu mata kuliah PBP Gasal 2024/2025 yang dapat diakses pada link [ini](http://rogerio-geraldo-aldo-garage.pbp.cs.ui.ac.id/) .

[Website Aldo's Garage](http://rogerio-geraldo-aldo-garage.pbp.cs.ui.ac.id/)

## **Tugas 2**

## **Step-step pengerjaan Proyek Aldo's Garage**

* ### Melakukan Inisiasi Project

Petama-tama saya membuat direktori baru dengan nama aldo-garage, kemudian setelah itu saya membuat file `requirements.txt` yang berisi dependencies dan mengisinya dengan dependencies yang ada.

Setelah itu saya melakukan instalasi menggunakan virtual environment pada terminal dengan command `pip install -r requirements.txt` lalu membuat proyek Django dengan perintah `django-admin startproject aldo-garage .`

* ### Run Server Django

Untuk melakukan runserver, saya menambahkan `["localhost", "127.0.0.1"]` pada `ALLOWED_HOSTS` yang ada pada file `setting.py` untuk melakukan deployment kemudian menjalankan server dengan command `python manage.py runserver`

* ### Menginisiasi `main`

Untuk membuat `main` lakukan command `python manage.py startapp main`, kemudian kita harus menambahkan `main` ke `INSTALLED_APPS` pada file `settings.py`.

Setelah menginisiasi `main` saya mengubah file `models.py` pada direktori `main` untuk melakukan mendefinisikan model baru dengan class dan fungsi yang ada pada tutorial.

Setelah itu saya melakukan migrate model baru tersebut dengan command `python manage.py makemigrations` dan `python manage.py migrate`.

* ### Membuat `main.html`

Mengisi file `main.html` dengan template:

```
<h1>Aldo's Garage</h1>

<h5>NPM: </h5>
<p>{{npm}}</p> 

<h5>Name: </h5>
<p>{{name}}</p>

<h5>Class: </h5>
<p>{{class}}</p> 

<h5>E-Commerce: </h5>
<p>{{e-commerce}}</p> 

<h5>Produk: </h5>
<p>{{product}}</p>

<h5>Harga: </h5>
<p>{{price}}</p> 

```

Kemudian kita juga harus mengisi file `views.py` dengan template function `show_main` yang ada pada file tutorial.

* ### Routing `main`

Saya mengatur URL pada aplikasi `main` dengan mengedit file `urls.py` pada folder `main` dengan template:

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Setelah itu kita dapat menjalankan `main` dengan command `python manage.py runserver`

## **Jawaban Tugas 2**

* ### Bagan request client ke web aplikasi berbasis Django

![](/BAGAN.jpg)

Dalam alur kerja Django, urls.py bertugas mengatur routing dengan meneruskan request pengguna ke fungsi yang sesuai di views.py. Di views.py, logika aplikasi diimplementasikan, seperti mengambil atau memodifikasi data dari models.py yang terhubung dengan basis data. Data yang diambil kemudian diteruskan ke berkas HTML (template) untuk menghasilkan tampilan yang akan dilihat pengguna. Setelah semua proses selesai, views.py mengembalikan response yang berisi HTML hasil render kepada pengguna, yang kemudian ditampilkan di browser.

* ### Jelaskan fungsi git dalam pengembangan perangkat lunak!


Git berfungsi sebagai sistem kontrol versi yang membantu pengembang melacak dan mengelola perubahan kode dalam proyek perangkat lunak. Dengan Git, pengembang dapat bekerja secara kolaboratif, membuat cabang (branch) untuk fitur baru, dan menggabungkannya (merge) kembali ke cabang utama setelah diuji. Ini juga memungkinkan rollback ke versi sebelumnya jika terjadi kesalahan, sehingga mempermudah pengelolaan versi dan integritas kode dalam pengembangan perangkat lunak.

* ### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?


Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan utama. Pertama, Django adalah framework "batteries-included", artinya Django menyediakan banyak fitur bawaan seperti sistem autentikasi, manajemen basis data, dan routing, sehingga pengembang pemula bisa langsung fokus pada pengembangan aplikasi tanpa perlu membangun fitur-fitur dasar dari awal. Kedua, Django menggunakan bahasa Python, yang terkenal mudah dipelajari dan digunakan, menjadikannya pilihan yang baik untuk pemula. Selain itu, Django menerapkan pola Model-View-Template (MVT) yang memisahkan logika aplikasi, data, dan tampilan, sehingga membantu pengembang memahami struktur aplikasi yang terorganisir dengan baik. Dukungan dokumentasi yang kuat dan komunitas yang aktif juga menjadikan Django populer di kalangan pemula.

* ### Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan teknik ini untuk memetakan objek-objek Python ke dalam tabel-tabel basis data relasional secara otomatis. Dalam ORM, setiap model di Django merepresentasikan sebuah tabel di basis data, dan setiap atribut dari model tersebut merepresentasikan kolom di tabel. ORM memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan kode Python tanpa perlu menulis query SQL secara langsung. Hal ini mempermudah manipulasi data dan membuat kode lebih bersih, terstruktur, dan mudah dipelihara.
