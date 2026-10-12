\# ConversorMD



Convierte documentos (docx, pdf, xlsx, pptx, imágenes, audio, etc.) a Markdown usando MarkItDown de Microsoft, con una interfaz web moderna.



\## Características



\- Interfaz web con diseño de alto impacto (glassmorphism, gradientes, animaciones).

\- Conversión ilimitada de archivos, sin límite de cantidad.

\- Descarga individual de cada .md.

\- Descarga de todos en un ZIP.

\- Opción de unificar todos los resultados en un solo archivo .md.

\- Barra de estadísticas (archivos, convertidos, errores).



\## Requisitos



\- Python 3.10 o superior.

\- pip (viene con Python).

\- Navegador moderno (Chrome, Edge, Firefox).



\## Instalación



1\. Clona el repositorio:



&#x20;  git clone https://github.com/TU-USUARIO/ConversorMD.git

&#x20;  cd ConversorMD



2\. Instala las dependencias:



&#x20;  python -m pip install flask markitdown\[all]



3\. Ejecuta el servidor:



&#x20;  python app.py



4\. Abre tu navegador en:



&#x20;  http://localhost:5000



\## Uso



1\. Arrastra tus archivos a la zona de carga (o haz clic para seleccionarlos).

2\. Pulsa el botón "Convertir".

3\. Descarga cada archivo individualmente, todos en un ZIP, o unifícalos en uno solo.



\## Estructura del proyecto



ConversorMD/

├── app.py                 # Servidor Flask

├── iniciar.bat            # Lanzador para Windows

├── README.md              # Este archivo

├── .gitignore             # Archivos ignorados por Git

└── templates/

&#x20;   └── plantilla.html     # Interfaz web



\## Tecnologías



\- Python 3

\- Flask

\- MarkItDown (Microsoft)

\- HTML, CSS, JavaScript

\- JSZip (para el ZIP en el cliente)



\## Licencia



MIT

