# Aldo's Garage

**Tugas Individu - Kelas B**

> **Aldo's Garage** merupakan suatu website yang menjual berbagai mobil dan dapat dikatakan sebagai e-commerce. Aldo's Garage menjual mobil-mobil vintage dan dapat diakses pada link [ini](http://rogerio-geraldo-aldogarage.pbp.cs.ui.ac.id/).

[Website Aldo's Garage](http://rogerio-geraldo-aldogarage.pbp.cs.ui.ac.id/)

## **Penjelasan**

<details>
<summary> <b> Tugas 2 </b> </summary>

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

</details>

<details>
<summary> <b> Tugas 3 </b> </summary>

## **Jawaban Tugas 3**

* ### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Karena dalam mengimplementasikan suatu platform kita bertujuan untuk memastikan bahwa data yang dikirim antar sistemnya dapat berjalan dengan cara yang cepat, efisien, aman, dan konsisten. Apabila kita tidak menggunakan data delivery dalam sebuah platform, maka aplkasi tidak mungkin bisa menyajikan informasi yang tepat kepada pengguna secara real-time. Data delivery juga dapat memungkinkan platform untuk beroperasi secara terdistribusi yang tentunya mendukung skala besar serta memfasilitasi komunikasi antar komponen yang berbeda secara smooth.

* ### Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    JSON (JavaScript Object Notation) lebih populer dibandingkan XML (eXtensible Markup Language) karena struktur JSON yang lebih ringkas dan mudah dibaca baik oleh manusia maupun mesin. JSON menggunakan sintaks pasangan *key-value* yang sederhana, mirip dengan objek dalam banyak bahasa pemrograman, sehingga menghasilkan ukuran file yang lebih kecil dan lebih efisien dalam transfer data. Sebaliknya, XML memerlukan banyak tag pembuka dan penutup, membuatnya lebih verbose dan menghasilkan ukuran file yang lebih besar. JSON juga lebih mudah diintegrasikan dan didukung langsung oleh hampir semua bahasa pemrograman modern, menjadikannya pilihan yang lebih praktis untuk pertukaran data dalam aplikasi web dan API.

* ### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method `is_valid()` pada form di Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua persyaratan validasi yang ditentukan, baik dari sisi form field maupun validasi kustom yang didefinisikan pengguna. Ketika `is_valid()` dipanggil, Django akan memeriksa apakah semua field form diisi dengan benar sesuai dengan tipe data yang diharapkan dan aturan validasi, seperti panjang maksimum, format email, atau validasi logika lainnya. Jika semua validasi lolos, method ini mengembalikan `True`, dan data yang telah dibersihkan dapat diakses melalui atribut `cleaned_data`. Sebaliknya, jika terdapat kesalahan, `is_valid()` akan mengembalikan `False` dan menyimpan pesan kesalahan di atribut `errors`. Method ini penting untuk memastikan bahwa data yang diproses dalam aplikasi aman dan sesuai dengan aturan yang telah ditentukan sebelum disimpan ke database atau digunakan lebih lanjut.

* ### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan yang disebut **Cross-Site Request Forgery (CSRF)**. Serangan ini terjadi ketika penyerang membuat pengguna yang sudah login mengirimkan permintaan yang tidak diinginkan, seperti mengubah kata sandi atau melakukan transaksi, tanpa sepengetahuan pengguna. Dengan menambahkan `csrf_token` ke form, Django menghasilkan token unik yang disertakan setiap kali pengguna mengirimkan form. Token ini kemudian diperiksa oleh server untuk memastikan bahwa permintaan benar-benar berasal dari aplikasi, bukan dari sumber lain yang berbahaya. Jika kita tidak menambahkan `csrf_token`, aplikasi bisa menjadi rentan terhadap serangan CSRF, yang memungkinkan penyerang melakukan aksi jahat tanpa persetujuan pengguna.

## **Step-by-step Pengimplementasian Checklist**

* ### Membuat `forms.py`

    Pertama-tama saya membuat form untuk menerima input dengan membuat file `forms.py` pada direktori main dengan kode

    ```
    from django.forms import ModelForm
    from main.models import CarEntry

    class CarEntryForm(ModelForm):
        class Meta:
            model = CarEntry
            fields = ["name", "price", "description", "car_horsepower"]
    ```

* ### Mengubah dan menambahkan fungsi pada `views.py`

    Setelah membuat file `forms.py`, saya kemudian melakukan modifikasi pada function `show_main` pada file `views.py` saya dengan kode

    ```
    def show_main(request):
        car_entries = CarEntry.objects.all()

        context = {
            'npm' : '2306245623',
            'name': 'Rogerio Geraldo Wibhowo',
            'class': 'PBP B',
            'car_entries': car_entries
        }

        return render(request, "main.html", context)
    ```

    Kemudian saya menambahkan function baru yaitu `create_car_entry` pada file `views.py` untuk menerima data dan berisi

    ```
    def create_car_entry(request):
        form = CarEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_car_entry.html", context)
    ```

* ### Membuat template baru

    Saya membuat template baru untuk tampilan ketika menambahkan produk dengan nama `create_car_entry.html` pada direktori `templates` yang ada pada `main` yang berisi

    ```
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Mood Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Car Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```

    Diikuti dengan menambahkan kode berikut pada file `main.html` dalam bentuk tabel serta menambahkan button `Add Car Entry` untuk menambahkan form

    ```
    {% if not car_entries %}
    <p>Belum ada data mobil yang masuk.</p>
    {% else %}
    <table>
    <tr>
        <th>Car Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Horsepower</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data mobil di bawah baris ini 
    {% endcomment %} 
    {% for car_entry in car_entries %}
    <tr>
        <td>{{car_entry.name}}</td>
        <td>{{car_entry.price}}</td>
        <td>{{car_entry.description}}</td>
        <td>{{car_entry.car_horsepower}}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_car_entry' %}">
    <button>Add New Car Entry</button>
    </a>
    ```

* ### Mengembalikan data dalam bentuk XML dan JSON

    Pertama saya menambahkan import `HttpRespnse` dan `Serializer` pada file `views.py`

    ```
    from django.http import HttpResponse
    from django.core import serializers
    ```

    Lalu saya membuat function baru dengan nama `show_xml` dan `show_json` masih pada file `views.py`

    ```
    def show_xml(request):
        data = CarEntry.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = CarEntry.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = CarEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = CarEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    Function `show_xml_by_id` dan `show_json_by_id` digunakan untuk melakukan return data berdasarkan id.

    Setelah itu, saya melakukan import function yang telah saya buat pada file `urls.py` yang ada pada `main`

    ```
    ...
    from main.views import show_main, create_car_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
    ...
    ```

    Lalu tambahkan path ke dalam `urlpatterns` untuk mengakses function yang telah diimport

    ```
    ...
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-car-entry', create_car_entry, name='create_car_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

Dengan ini, input `form` dapat dijalankan dengan command `python manage.py runserver` dengan membuka link <http://localhost:8000>.

## Postman
## **1. XML**
![XML](xml.png)

## **2. JSON**
![JSON](json.png)

## **3. XML by ID**
![XML by ID](<xml id.png>)

## **4. JSON by ID**
 ![JSON by ID](<json id.png>)

</details>

<details>
<summary> <b> Tugas 4 </b> </summary>

## **Jawaban Tugas 4**

* ### Apa perbedaan antara `HttpresponseRedirect()` dan `redirect()`?
    `HttpResponseRedirect()` dan `redirect()` adalah dua metode yang digunakan di Django untuk mengarahkan pengguna dari satu URL ke URL lain, tetapi mereka memiliki beberapa perbedaan. `HttpResponseRedirect()` adalah sebuah class yang digunakan untuk membuat respons HTTP dengan kode status 302 (redirect sementara) dan membutuhkan URL secara eksplisit sebagai argumen. Sementara itu, `redirect()` adalah fungsi shortcut yang lebih fleksibel karena mampu menerima berbagai jenis input, seperti URL, nama view, atau bahkan objek model, dan secara otomatis membuat objek `HttpResponseRedirect`. Karena `redirect()` lebih mudah dan fleksibel, banyak yang lebih memilihnya, terutama ketika perlu melakukan pengalihan dengan nama view atau instance model. Di sisi lain, `HttpResponseRedirect()` lebih cocok jika kita hanya ingin bekerja langsung dengan URL yang sudah pasti.

* ### Bagaimana cara menghubungkan model `Product` dengan `User`?
    Untuk menghubungkan model Product dengan User di Django, kita bisa menggunakan ForeignKey. ForeignKey memungkinkan setiap produk (Product) terkait dengan satu pengguna (User), yang biasanya berarti bahwa seorang pengguna bisa membuat atau memiliki banyak produk, tapi setiap produk hanya dimiliki oleh satu pengguna. Caranya adalah dengan menambahkan field user di model Product yang merujuk ke model User. Berikut ini contoh dari kode saya:

    ```
    import uuid
    from django.db import models
    from django.contrib.auth.models import User

    class CarEntry(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        car_horsepower = models.IntegerField(default=0)

    ```

    Pada kode di atas, `user = models.ForeignKey(User, on_delete=models.CASCADE)` menghubungkan model Product dengan model User. Field user akan menyimpan informasi tentang pengguna yang memiliki produk tersebut. Argumen `on_delete=models.CASCADE` memastikan bahwa jika pengguna dihapus, semua produk yang terkait dengannya juga akan dihapus. Dengan cara ini, model Product dan User bisa saling terhubung di aplikasi Django.

* ### Perbedaan antara authentication dan authorization
    Authentication dan authorization adalah dua konsep berbeda yang sering digunakan dalam pengelolaan akses pengguna. **Authentication** (otentikasi) adalah proses memverifikasi identitas pengguna, misalnya saat pengguna login dengan memasukkan username dan password untuk membuktikan bahwa mereka adalah siapa yang mereka klaim. Sedangkan **authorization** (otorisasi) adalah proses menentukan apa yang diizinkan atau dapat diakses oleh pengguna setelah mereka berhasil diautentikasi. Jadi, authentication menjawab pertanyaan "siapa kamu?" dan authorization menjawab "apa yang bisa kamu lakukan?"

    Saat pengguna login, yang pertama kali dilakukan adalah proses authentication, di mana Django memeriksa apakah username dan password yang dimasukkan cocok dengan yang tersimpan di database. Jika berhasil, pengguna dianggap **terotentikasi**. Setelah itu, Django akan mengecek **otorisasi** berdasarkan peran atau izin yang dimiliki pengguna, untuk menentukan halaman atau tindakan apa yang boleh mereka akses.

    Dalam Django, proses authentication diimplementasikan dengan menggunakan **session** dan **middleware**. Django memiliki sistem otentikasi bawaan yang mencakup fungsi untuk login, logout, dan mengelola sesi pengguna. Sedangkan untuk authorization, Django menggunakan **permissions** (izin) yang dapat ditetapkan pada level pengguna atau grup pengguna untuk menentukan akses apa yang diizinkan bagi mereka.

* ### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
    Django mengingat pengguna yang telah login dengan menggunakan **cookies** dan **session**. Ketika pengguna berhasil login, Django membuat sebuah cookie di browser pengguna yang berisi ID unik. ID ini terhubung dengan data sesi yang disimpan di server, di mana Django menyimpan informasi pengguna yang sudah terautentikasi. Jadi, setiap kali pengguna mengunjungi halaman, browser mereka akan mengirimkan cookie tersebut, dan Django bisa mengenali pengguna dari ID sesi yang ada di cookie. Dengan cara ini, pengguna tidak perlu login ulang setiap kali mereka memuat halaman baru selama sesi masih aktif.

    Selain untuk mengingat pengguna yang login, **cookies** digunakan untuk berbagai tujuan lain, seperti menyimpan preferensi pengguna (misalnya, bahasa yang dipilih atau tema tampilan), melacak aktivitas pengguna di situs web, atau menyimpan keranjang belanja dalam e-commerce. Namun, tidak semua cookies aman. Beberapa cookies bisa dieksploitasi oleh pihak ketiga, terutama jika tidak dilindungi dengan baik. Untuk meningkatkan keamanan, Django mendukung penggunaan **secure cookies** yang hanya dikirim melalui koneksi HTTPS, serta **HttpOnly cookies** yang mencegah akses cookies dari JavaScript, sehingga melindungi dari serangan cross-site scripting (XSS). Oleh karena itu, meskipun cookies sangat berguna, perlu berhati-hati dalam penggunaannya untuk memastikan keamanan.

## **Step-by-step Pengimplementasian Checklist**

* ### Tambahkan fungsi `def register(request)` pada file `views.py`

    Pertama-tama saya menambahkan fungsi `register()` untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form. 

    ```
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages

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

* ### Membuat file baru bernama `register.html`

    Buat dan isi file `register.html` `pada direktori main/templates` dengan template:

    ```
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

    Kemudian lakukan impor fungsi `register()` pada `urls.py` dan tambahkan path ke dalam `urlpatterns`
    
    ```
    ...
    form main.views import register
    
     urlpatterns = [
        ...
        path('register/', register, name='register'),
    ]
    ```

* ### Membuat fungsi login dan logout
    Pada file `views.py` tambahkan fungsi `login_user()` dan `logout_user()` untuk mengautentikasi pengguna yang login dan logout. 

    ```
    from django.contrib.auth.forms import UserCreationForm AuthenticationForm
    from django.contrib.auth import authenticate, login, logout

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

    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

    Diikuti dengan membuat file html baru yaitu `login.html` pada direktori `main/templates` dan isi dengan template:

    ```
    {% extends 'base.html' %}

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

    {% endblock content %}
    ```

    Untuk membuat button logout, tambahkan kode ini pada `main.html` yang ada pada direktori `main/templates` setelah hyperlink tag untuk `Add New Car Entry`

    ```
    ...
    <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    </a>
    ...
    ```

    Lalu kita harus mengimpor dan menambahkan kode pada file `views.py` seperti ini

    ```
    from main.views import login_user
    from main.views import logout_user

    urlpatterns = [
        ...
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ]
    ```

* ### Merestriksi akses halaman Main

    Pada file `views.py` tambahkan impor `login_required` dan potongan kode di atas fungsi `show_main` seperti berikut

    ```
    from django.contrib.auth.decorators import login_required

    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ```

    Setelah melakukan restriksi pada akses halaman main, kita sudah bisa menjalankan proyek dengan command `python manage.py runserver` dan jika kita membuka <http://localhost:8000> kita akan langsung diarahkan ke halaman login.

* ### Cara menggunakan data dari Cookies

    Untuk menggunakan data dari cookies, kita harus menambahkan impor dan mengubah potongan kode di blok `if form.is_valid()` pada file `views.py` dengan

    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse

    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```

    Lalu pada fungsi `show_main` tambahkan potongan kode `'last_login': request.COOKIES['last_login']` pada variabel `context` seperti berikut ini

    ```
    context = {
        'npm' : '2306245623',
        'name': request.user.username,
        'class': 'PBP B',
        'car_entries': car_entries,
        'last_login': request.COOKIES['last_login'],
    }

    ```

    Kita juga perlu mengubah fungsi `logout_user` dengan kode seperti ini

    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

    Terakhir tambahkan kode pada `main.html` untuk menampilkan data waktu login terakhir dari cookie tersebut

    ```
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

* ### Menghubungkan model `CarEntry` dengan User

    Tambahkan impor `User` pada `models.py` dan tambahkan potongan kode seperti berikut

    ```
    ...
    from django.contrib.auth.models import User

    class CarEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
    ```

    Lalu buka file `views.py` dan ubah fungsi `create_car_entry` menjadi seperti berikut

    ```
    def create_car_entry(request):
        form = CarEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            car_entry = form.save(commit=False)
            car_entry.user = request.user
            car_entry.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_car_entry.html", context)
    ```

    Parameter `commit` haruslah bernilai `False` agar mencegah Django langsung menyimpan objek yang telah dibuat dari form langsung ke database.

    Kemudian ubah value dari `car_entries` dan `context` pada fungsi `show_main` dengan kode seperti berikut

    ```
    def show_main(request):
        car_entries = CarEntry.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
            ...
        }
    ...
    ```

    Agar nama yang ditampilkan sesuai dengan nama yang user input saat login.

    Terakhir tambahkan `import os`  dan ganti variabel `DEBUG` pada file `settings.py` dengan

    ```
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
    ```

    Jangan lupa lakukan migration untuk menyimpan semua perubahan yang telah dilakukan, lalu bukalah link website dan tugas 4 selesai.


