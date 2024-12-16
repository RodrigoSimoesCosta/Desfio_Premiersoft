from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.preprocessing import image
#from keras.preprocessing import image
from tensorflow.keras.models import load_model
import io
from PIL import Image

# Inicializando o Flask
app = Flask(__name__)

# Carregando o modelo treinado
model = load_model('garrafa_model.keras')

# Função para classificar a imagem
def classify_image(img):
    img = img.resize((224, 224))
    img = np.array(img) / 255.0  # Normalizar a imagem
    img = np.expand_dims(img, axis=0)  # Adicionar batch dimension
    prediction = model.predict(img)
    return prediction[0][0]

#Adicionar uma rota para / no seu arquivo app.py
@app.route("/")
def home():
    return "Bem-vindo ao Flask!"

@app.route('/favicon.ico')
def favicon():
    return "", 204  # Sem conteúdo


# Rota para classificar a imagem
@app.route('/classificar', methods=['POST'])
def classificar():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de imagem fornecido'}), 400

    file = request.files['image']

    if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            img = Image.open(io.BytesIO(file.read()))
            confidence = classify_image(img)
            status = 'aberta' if confidence > 0.5 else 'fechada'
            return jsonify({
                'status': status,
                'confidence': float(confidence)
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Formato de arquivo inválido. São aceitas apenas imagens nos formatos .png, .jpg e .jpeg.'}), 400

# Rodando a API
if __name__ == '__main__':
    app.run(debug=True)
