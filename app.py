import os
import tempfile
from flask import Flask, request, render_template, jsonify
from markitdown import MarkItDown

app = Flask(__name__)
md = MarkItDown()

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

            nombre_md = os.path.splitext(f.filename)[0] + '.md'
            resultados.append({
                'nombre': nombre_md,
                'contenido': resultado.text_content
            })
        except Exception as e:
            resultados.append({
                'nombre': f.filename,
                'contenido': f'ERROR al convertir: {e}'
            })

    return jsonify({'resultados': resultados})

if __name__ == '__main__':
    print("Servidor iniciado en http://localhost:5000")
    app.run(port=5000, debug=False)