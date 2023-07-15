<div align="center">
  <table width="1000px">
    <theader>
      <tr>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
        <th>
          <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
          <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
          <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
          <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
        </th>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
      </tr>
    </theader>
    <tbody>
      <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
      <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
  </table>
</div>

<div align="center">
    <span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
</div>

<div align="center">
  <table width="1000px">
    <theader>
      <tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
    </theader>
    <tbody>
      <tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 02</td></tr>
      <tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Relaciones de uno a muchos, muchos a muchos, impresion de pdf y emails</td></tr>
      <tr><td>NÚMERO DE PRÁCTICA:</td><td>07</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td width="60px">  III  </td></tr>
      <tr><td>FECHA DE PRESENTACIÓN:</td><td>14/07/2023</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">23:59</td></tr>
      <tr>
        <td colspan="4">NOMBRE:
          <ul>
            <li>Melsy Melany Huamaní Vargas</li>
          </ul>
        </td>
        <td>NOTA:</td><td></td>
      </tr>
      <tr>
        <td colspan="6" width="1000px">DOCENTES:
          <ul>
            <li>Anibal Sardon Paniagua</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>


##
## ACTIVIDADES


***Creando proyecto e instalando***

Se utiliza el sistema Windows para instalar las herramientas necesarias y crear el proyecto. En este caso, se escogió una aplicación library para que se muestran libros, autores<br/><br/>

- Creando el ambiente para el proyecto
    ```sh
    C:\Users\melsy>mkvirtualenv my_env7
    created virtual environment CPython3.11.1.final.0-64 in 3903ms
      creator CPython3Windows(dest=C:\Users\melsy\Envs\my_env7, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\melsy\AppData\Local\pypa\virtualenv)
        added seed packages: pip==23.1.2, setuptools==67.8.0, wheel==0.40.0
      activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    ```
    <br/>

- Se instala django
    ```sh
    (my_env7) C:\Users\melsy>pip install django
    Collecting django
    Downloading Django-4.2.3-py3-none-any.whl (8.0 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 13.8 MB/s eta 0:00:00
    Collecting asgiref<4,>=3.6.0 (from django)
    Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
    Collecting sqlparse>=0.3.1 (from django)
    Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
    Collecting tzdata (from django)
    Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
    Installing collected packages: tzdata, sqlparse, asgiref, django
    Successfully installed asgiref-3.7.2 django-4.2.3 sqlparse-0.4.4 tzdata-2023.3
    ```
    <br/>

- Instalando xhtml2pdf para que posteriormente podamos convertir en pdf
    ```sh
    (my_env7) C:\Users\melsy>pip install --pre xhtml2pdf
    Collecting xhtml2pdf
    Downloading xhtml2pdf-0.2.11.tar.gz (108 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.3/108.3 kB 3.2 MB/s eta 0:00:00
    Preparing metadata (setup.py) ... done
    Collecting arabic-reshaper>=3.0.0 (from xhtml2pdf)
    Downloading arabic_reshaper-3.0.0-py3-none-any.whl (20 kB)
    Collecting html5lib>=1.0.1 (from xhtml2pdf)
    Downloading html5lib-1.1-py2.py3-none-any.whl (112 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 112.2/112.2 kB 6.4 MB/s eta 0:00:00
    Collecting Pillow>=8.1.1 (from xhtml2pdf)
    Using cached Pillow-10.0.0-cp311-cp311-win_amd64.whl (2.5 MB)
    Collecting pyHanko>=0.12.1 (from xhtml2pdf)
    Downloading pyHanko-0.19.0-py3-none-any.whl (407 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 407.5/407.5 kB 8.5 MB/s eta 0:00:00
    Collecting pyhanko-certvalidator>=0.19.5 (from xhtml2pdf)
    Downloading pyhanko_certvalidator-0.23.0-py3-none-any.whl (106 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.8/106.8 kB 6.0 MB/s eta 0:00:00
    Collecting pypdf>=3.1.0 (from xhtml2pdf)
    Downloading pypdf-3.12.1-py3-none-any.whl (254 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 254.8/254.8 kB 7.9 MB/s eta 0:00:00
    Collecting python-bidi>=0.4.2 (from xhtml2pdf)
    Downloading python_bidi-0.4.2-py2.py3-none-any.whl (30 kB)
    Collecting reportlab<4,>=3.5.53 (from xhtml2pdf)
    Downloading reportlab-3.6.13-cp311-cp311-win_amd64.whl (2.3 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 9.9 MB/s eta 0:00:00
    Collecting svglib>=1.2.1 (from xhtml2pdf)
    Downloading svglib-1.5.1.tar.gz (913 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 913.9/913.9 kB 14.6 MB/s eta 0:00:00
    Preparing metadata (setup.py) ... done
    Collecting six>=1.9 (from html5lib>=1.0.1->xhtml2pdf)
    Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
    Collecting webencodings (from html5lib>=1.0.1->xhtml2pdf)
    Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
    Collecting asn1crypto>=1.5.1 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading asn1crypto-1.5.1-py2.py3-none-any.whl (105 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 105.0/105.0 kB ? eta 0:00:00
    Collecting qrcode>=6.1 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading qrcode-7.4.2-py3-none-any.whl (46 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.2/46.2 kB ? eta 0:00:00
    Collecting tzlocal>=4.3 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading tzlocal-5.0.1-py3-none-any.whl (20 kB)
    Collecting click>=7.1.2 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading click-8.1.5-py3-none-any.whl (98 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.1/98.1 kB ? eta 0:00:00
    Collecting requests>=2.24.0 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading requests-2.31.0-py3-none-any.whl (62 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB ? eta 0:00:00
    Collecting pyyaml>=5.3.1 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading PyYAML-6.0-cp311-cp311-win_amd64.whl (143 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 143.2/143.2 kB ? eta 0:00:00
    Collecting cryptography>=3.3.1 (from pyHanko>=0.12.1->xhtml2pdf)
    Downloading cryptography-41.0.2-cp37-abi3-win_amd64.whl (2.6 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 15.2 MB/s eta 0:00:00
    Collecting oscrypto>=1.1.0 (from pyhanko-certvalidator>=0.19.5->xhtml2pdf)
    Downloading oscrypto-1.3.0-py2.py3-none-any.whl (194 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 194.6/194.6 kB 11.5 MB/s eta 0:00:00
    Collecting uritools>=3.0.1 (from pyhanko-certvalidator>=0.19.5->xhtml2pdf)
    Downloading uritools-4.0.1-py3-none-any.whl (10 kB)
    Collecting lxml (from svglib>=1.2.1->xhtml2pdf)
    Downloading lxml-4.9.3-cp311-cp311-win_amd64.whl (3.8 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 18.5 MB/s eta 0:00:00
    Collecting tinycss2>=0.6.0 (from svglib>=1.2.1->xhtml2pdf)
    Downloading tinycss2-1.2.1-py3-none-any.whl (21 kB)
    Collecting cssselect2>=0.2.0 (from svglib>=1.2.1->xhtml2pdf)
    Downloading cssselect2-0.7.0-py3-none-any.whl (15 kB)
    Collecting colorama (from click>=7.1.2->pyHanko>=0.12.1->xhtml2pdf)
    Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
    Collecting cffi>=1.12 (from cryptography>=3.3.1->pyHanko>=0.12.1->xhtml2pdf)
    Downloading cffi-1.15.1-cp311-cp311-win_amd64.whl (179 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 179.0/179.0 kB ? eta 0:00:00
    Collecting typing-extensions (from qrcode>=6.1->pyHanko>=0.12.1->xhtml2pdf)
    Downloading typing_extensions-4.7.1-py3-none-any.whl (33 kB)
    Collecting pypng (from qrcode>=6.1->pyHanko>=0.12.1->xhtml2pdf)
    Downloading pypng-0.20220715.0-py3-none-any.whl (58 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.1/58.1 kB 3.0 MB/s eta 0:00:00
    Collecting charset-normalizer<4,>=2 (from requests>=2.24.0->pyHanko>=0.12.1->xhtml2pdf)
    Downloading charset_normalizer-3.2.0-cp311-cp311-win_amd64.whl (96 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 5.8 MB/s eta 0:00:00
    Collecting idna<4,>=2.5 (from requests>=2.24.0->pyHanko>=0.12.1->xhtml2pdf)
    Downloading idna-3.4-py3-none-any.whl (61 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB ? eta 0:00:00
    Collecting urllib3<3,>=1.21.1 (from requests>=2.24.0->pyHanko>=0.12.1->xhtml2pdf)
    Downloading urllib3-2.0.3-py3-none-any.whl (123 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.6/123.6 kB ? eta 0:00:00
    Collecting certifi>=2017.4.17 (from requests>=2.24.0->pyHanko>=0.12.1->xhtml2pdf)
    Downloading certifi-2023.5.7-py3-none-any.whl (156 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.0/157.0 kB ? eta 0:00:00
    Requirement already satisfied: tzdata in c:\users\melsy\envs\my_env7\lib\site-packages (from tzlocal>=4.3->pyHanko>=0.12.1->xhtml2pdf) (2023.3)
    Collecting pycparser (from cffi>=1.12->cryptography>=3.3.1->pyHanko>=0.12.1->xhtml2pdf)
    Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 kB 7.2 MB/s eta 0:00:00
    Building wheels for collected packages: xhtml2pdf, svglib
    Building wheel for xhtml2pdf (setup.py) ... done
    Created wheel for xhtml2pdf: filename=xhtml2pdf-0.2.11-py3-none-any.whl size=350609 sha256=4accc136623a97c6fc304ea108a96c16d1596449482f437a42145946921768d2
    Stored in directory: c:\users\melsy\appdata\local\pip\cache\wheels\0f\60\ff\19293124ab7d2cae9672575eaa3d64aaabff6ff2d240da67f0
    Building wheel for svglib (setup.py) ... done
    Created wheel for svglib: filename=svglib-1.5.1-py3-none-any.whl size=30976 sha256=ec6157ef5c8ac3f903219c27a0fb462bd7a66ca4a2c5d8855219ea30ab2b887f
    Stored in directory: c:\users\melsy\appdata\local\pip\cache\wheels\7e\01\0e\e6e336915d6e8448890a695770ba88fe030cc71060988016f6
    Successfully built xhtml2pdf svglib
    Installing collected packages: webencodings, pypng, asn1crypto, arabic-reshaper, urllib3, uritools, tzlocal, typing-extensions, tinycss2, six, pyyaml, pypdf, pycparser, Pillow, oscrypto, lxml, idna, colorama, charset-normalizer, certifi, requests, reportlab, qrcode, python-bidi, html5lib, cssselect2, click, cffi, svglib, cryptography, pyhanko-certvalidator, pyHanko, xhtml2pdf
    Successfully installed Pillow-10.0.0 arabic-reshaper-3.0.0 asn1crypto-1.5.1 certifi-2023.5.7 cffi-1.15.1 charset-normalizer-3.2.0 click-8.1.5 colorama-0.4.6 cryptography-41.0.2 cssselect2-0.7.0 html5lib-1.1 idna-3.4 lxml-4.9.3 oscrypto-1.3.0 pyHanko-0.19.0 pycparser-2.21 pyhanko-certvalidator-0.23.0 pypdf-3.12.1 pypng-0.20220715.0 python-bidi-0.4.2 pyyaml-6.0 qrcode-7.4.2 reportlab-3.6.13 requests-2.31.0 six-1.16.0 svglib-1.5.1 tinycss2-1.2.1 typing-extensions-4.7.1 tzlocal-5.0.1 uritools-4.0.1 urllib3-2.0.3 webencodings-0.5.1 xhtml2pdf-0.2.11
    ```
    <br/>

- Se crea el proyecto dentro de la carpeta ``projects`` y dentro de esta se crea la aplicación ``library`` para usarla más adelante.
    ```sh
    (my_env7) C:\Users\melsy>cd projects
    (my_env7) C:\Users\melsy\projects> django-admin startproject proyecto
    (my_env7) C:\Users\melsy\projects>cd proyecto
    (my_env7) C:\Users\melsy\projects\proyecto>python manage.py startapp library
    ```
    <br/>

- Se corre el servidor y se puede ver lo siguiente

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img1.png" style="width:70%"/><br/>

<br/>

***Creando los modelos, uno a muchos, muchos a muchos***

- Primero se añade la aplicación creada en el archivo ``settings.py`` de ``lab07``.
    ```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'library' # Se agrega esta linea
    ]
    ```
    <br/>

- Se crea el modelo ``Author`` que tiene relación de uno a muchos con el modelo ``Book``.
    ```py
    class Author(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name
    ```
    <br/>

- Ahora se crea el modelo ``Publisher`` que en este caso tiene relación de muchos a muchos con el modelo ``Book``.
    ```py
    class Publisher(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name
    ```
    <br/>

- Se tiene el modelo ``Book`` el cual tiene relación uno a muchos con el que se usa ``author = models.ForeignKey(Author, on_delete=models.CASCADE)`` y muchos a muchos con ``publisher = models.ManyToManyField(Publisher)``.
    ```py
    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        publisher = models.ManyToManyField(Publisher)
        summary = models.TextField()

        def __str__(self):
            return self.title
    ```
    <br/>

- Se hacen las migraciones de los modelos del proyecto.
    ```sh
    (my_env7) C:\Users\melsy\projects\proyecto>python manage.py makemigrations
    Migrations for 'library':
      library\migrations\0001_initial.py
        - Create model Author
        - Create model Publisher
        - Create model Book
    (my_env7) C:\Users\melsy\projects\proyecto>python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, library, sessions
    Running migrations:
      Applying library.0001_initial... OK
    ```
    <br/>

<br/>

***Configurando views, email y PDF***

- Se crean las vistas para ver la lista de libro y los detalles del libro seleccionado en ``views.py`` de library.
    ```py
    from django.shortcuts import render
    from .models import Book

    def book_list(request):
        books = Book.objects.all()
        return render(request, 'library/book_list.html', {'books': books})

    def book_detail(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'library/book_detail.html', {'book': book})
    ```
    <br/>

- Se crea la función ``generate_pdf`` para generar el PDF con los detalles de un libro y se agregan los siguientes import en ``views.py`` de library.
    ```py
    from django.shortcuts import render, get_object_or_404
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    from .models import Book

    def generate_pdf(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        template_path = 'library/invoice.html'
        context = {
            'book': book,
        }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="book_details.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('Error al generar el PDF', status=500)
        return response
    ```
    <br/>

- Se crea la función ``send_email`` en ``views.py`` de library, para enviar un email el cual utiliza la función anterior para enviar el PDF con los detalles del libro.
    ```py
    from django.shortcuts import render, get_object_or_404
    from django.http import HttpResponse
    from django.template.loader import get_template
    from django.core.mail import EmailMessage
    from xhtml2pdf import pisa
    from .models import Book

    def send_email(request, book_id):
        if request.method == 'POST':
            pdf = generate_pdf(request, book_id)
            email_address = request.POST.get('email')

            email = EmailMessage(
                'Detalles del libro',
                'Adjunto encontrarás los detalles del libro en formato PDF.',
                'melsy@gmail.com',
                [email_address]
            )

            email.attach('book_details.pdf', pdf.getvalue(), 'application/pdf')
            email.send()

            return render(request, 'library/email_sent.html')
        
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'library/book_detail.html', {'book': book})
    ```
    <br/>

- En el archivo ``settings.py`` de proyecto se colocan las credenciales del email para enviar el correo, par esto se utilizó la página de ``Mailtrap`` el cual brinda estas credenciales para pruebas de correo.
    ```py
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'bd45a037fa56d1'
    EMAIL_HOST_PASSWORD = '9a7f42a21e19bf'
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    ```
    <br/>

<br/>

***Configurando URLs***

- Se colocan las urls de library en el archivo de ``urls.py`` de proyecto para que puedan ser reconocidas.
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('library/', include('library.urls')),
    ]
    ```
    <br/>

- Se colocan las urls en el archivo de ``urls.py`` de library para que sean reconocidas posteriormente.
    ```py
    from django.urls import path
    from . import views

    app_name = 'library'

    urlpatterns = [
        path('books/', views.book_list, name='book_list'),
        path('book/<int:book_id>/', views.book_detail, name='book_detail'),
        path('book/<int:book_id>/pdf/', views.generate_pdf, name='generate_pdf'),
        path('book/<int:book_id>/email/', views.send_email, name='send_email'),
    ]
    ```
    <br/>

<br/>

***Creando los archivos HTML dentro de library/templates/library***

- En primer lugar, se modifica el archivo ``settings.py`` de proyecto para que reconozca los archivos html.
    ```py
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')], # Se agrega esta línea
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
    <br/>

- Se crea el archivo ``book_list.html`` con lo siguiente.
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lista de libros</title>
    </head>
    <body>
        <h1>Lista de libros</h1>
        <ul>
        {% for book in books %}
            <li><a href="{% url 'library:book_detail' book.id %}">{{ book.title }}</a></li>
        {% empty %}
            <li>No hay libros disponibles.</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    ```
    <br/>

- Se crea el archivo ``book_detail.html`` con lo siguiente.
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Detalles del libro</title>
    </head>
    <body>
        <h1>Detalles del libro</h1>
        <h2>{{ book.title }}</h2>
        <p>Autor: {{ book.author.name }}</p>
        <p>Publicado por:</p>
        <ul>
            {% for publisher in book.publisher.all %}
                <li>{{ publisher.name }}</li>
            {% endfor %}
        </ul>
        <p>Resumen: {{ book.summary }}</p>
        <form action="{% url 'library:send_email' book.id %}" method="POST">
            {% csrf_token %}
            <label for="email">Enviar PDF por email:</label><br>
            <input type="email" id="email" name="email"><br>
            <input type="submit" value="Enviar">
        </form>
        <a href="{% url 'library:generate_pdf' book.id %}">Descargar en PDF</a>

    </body>
    </html>
    ```
    <br/>

- Se crea el archivo ``invoice.html`` para mostrar en PDF el contenido requerido.
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Detalles del libro</title>
        <style type="text/css">
            body {
                font-weight: 200;
                font-size: 14px;
            }
            .header {
                font-size: 20px;
                font-weight: 100;
                text-align: center;
                color: #007cae;
            }
            .title {
                font-size: 22px;
                font-weight: 100;
                padding: 10px 20px 0px 20px;  
            }
            .details {
                padding: 10px 20px 0px 20px;
                text-align: left !important;
            }
            .hrItem {
                border: none;
                height: 1px;
                color: #333;
                background-color: #fff;
            }
        </style>
    </head>
    <body>
        <div class='wrapper'>
            <div class='header'>
                <p class='title'>Detalles del libro</p>
            </div>
            <div class='details'>
                <p>Autor: {{ book.author.name }}</p>
                <p>Publicado por: 
                {% for publisher in book.publisher.all %}
                    {{ publisher.name }}{% if not forloop.last %}, {% endif %}
                {% empty %}
                    Sin publicaciones
                {% endfor %}
                </p>
                <p>Resumen: {{ book.summary }}</p>
                <hr class='hrItem' />
            </div>
        </div>
    </body>
    </html>
    ```
    <br/>

- Se crea el archivo ``email_sent.html`` donde se confirma que el correo ha sido enviado.
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Confirmación de envío de correo</title>
    </head>
    <body>
        <h1>Correo electrónico enviado</h1>
        <p>Se ha enviado el correo electrónico con los detalles del libro en formato PDF.</p>
    </body>
    </html>
    ```
    <br/>

<br/>

***Configurando página de admin***

- En primer lugar se modifica ``admin.py`` de library para que se puedan crear los modelos de author, book y publisher.
    ```py
    from django.contrib import admin
    from .models import Book, Author, Publisher

    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        pass

    @admin.register(Author)
    class AuthorAdmin(admin.ModelAdmin):
        pass

    @admin.register(Publisher)
    class PublisherAdmin(admin.ModelAdmin):
        pass
    ```
    <br/>

- Se crea el superusuario para acceder a la página del administrador.
    ```sh
    (my_env7) C:\Users\melsy\projects\proyecto>python manage.py createsuperuser
    Username (leave blank to use 'melsy'): mhuamanivar
    Email address: mhuamanivar@unsa.edu.pe
    Password:
    Password (again):
    This password is too common.
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    ```
    <br/>

<br/>

***Creando nuevos libros en página de admin***

- Se va a la página del admin

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img2.png" style="width:70%"/><br/>

- Luego se da en ``add`` para añadir un libro, y colocamos los detalles importantes, se crea tres libros como ejemplo.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img3.png" style="width:70%"/><br/>

- Después se puede ver la lista de libros creados en la pagina del admin.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img4.png" style="width:70%"/><br/>

<br/>

***Viendo la página principal***

- Se va a la pagina ``http://127.0.0.1:8000/library/books/`` y se ve la lista de libros

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img5.png" style="width:40%"/><br/>

- Se da click a uno de ellos y se pueden ver los detalles del libro

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img6.png" style="width:70%"/><br/>

- Para enviar un correo, se inserta el correo al que se desea enviar

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img7.png" style="width:70%"/><br/>

- Posteriormente se puede ver la pagina que menciona que se ha enviado correctamente.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img8.png" style="width:40%"/><br/>

- Como se eligió trabajar con Mailtrap, entonces se va a la página y se puede ver que ha sido enviado correctamente el mensaje, además se ve de quien para quien va dirigido y el archivo que ha sido enviado en ``Attachments``.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img9.png" style="width:70%"/><br/>

- Por otro lado, si se quiere enviar un PDF, entonces se hace click en ``Descargar en PDF`` y le damos en guardar en la carpeta que queremos.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img10.png" style="width:70%"/><br/>

- Se confirma que ha sido guardado con el navegador.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img11.png" style="width:40%"/><br/>

- Finalmente se puede ver el archivo en formato PDF, que contiene los detalles del libro.

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab07/main/imagenes/img12.png" style="width:70%"/><br/>