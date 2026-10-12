import os
import re
import tempfile
from flask import Flask, request, render_template, jsonify
from markitdown import MarkItDown

app = Flask(__name__)
md = MarkItDown()

# Patrón para detectar líneas compuestas solo por caracteres basura
# (los que aparecen cuando hay cuadros de texto o formas en Word)
PATRON_BASURA = re.compile(
    r'^[\s\u0080-\u00ff\u2000-\u206f\u2500-\u25ff\u2600-\u27bf]+$'
)
# Patrón para eliminar bloques largos de caracteres raros dentro de una línea
PATRON_BLOQUE = re.compile(
    r'[\u0080-\u00ff\u2000-\u206f\u2500-\u25ff\u2600-\u27bf]{4,}'
)

def limpiar_markdown(texto):
    """Elimina caracteres basura que aparecen al convertir docx con cuadros/formas."""
    lineas_limpias = []
    for linea in texto.splitlines():
        # Saltar líneas que son puro relleno de símbolos raros
        if PATRON_BASURA.match(linea.strip()):
            continue
        # Quitar bloques de símbolos raros dentro de líneas con contenido real
        linea = PATRON_BLOQUE.sub('', linea)
        lineas_limpias.append(linea)

    # Colapsar líneas en blanco consecutivas (máximo 1)
    resultado = []
    vacias = 0
    for l in lineas_limpias:
        if l.strip() == '':
            vacias += 1
            if vacias <= 1:
                resultado.append(l)
        else:
            vacias = 0
            resultado.append(l)

    return '\n'.join(resultado).strip()


@app.route('/')
def index():
    return render_template('plantilla.html')


@app.route('/convert', methods=['POST'])
def convert():
    if 'files' not in request.files:
        return jsonify({'error': 'No se enviaron archivos'}), 400

    archivos = request.files.getlist('files')
    resultados = []

    for f in archivos:
        if not f.filename:
            continue
        try:
            sufijo = os.path.splitext(f.filename)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=sufijo) as tmp:
                f.save(tmp.name)
                ruta_tmp = tmp.name

            resultado = md.convert(ruta_tmp)
            os.unlink(ruta_tmp)

            contenido = limpiar_markdown(resultado.text_content)
            nombre_md = os.path.splitext(f.filename)[0] + '.md'
            resultados.append({
                'nombre': nombre_md,
                'contenido': contenido
            })
        except Exception as e:
            resultados.append({
                'nombre': f.filename,
                'contenido': f'ERROR al convertir: {e}'
            })

    return jsonify({'resultados': resultados})


if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto, debug=False)