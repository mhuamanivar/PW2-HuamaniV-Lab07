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
    (my_env7) C:\Users\melsy\projects> django-admin startproject lab07
    (my_env7) C:\Users\melsy\projects>cd lab07
    (my_env7) C:\Users\melsy\projects\lab07>python manage.py startapp library
    ```
    <br/>

- Se corre el servidor y se puede ver lo siguiente

    <img src="a" style="width:70%"/><br/>

<br/>
