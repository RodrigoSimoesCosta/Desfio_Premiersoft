import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Carregar o modelo
model = load_model('garrafa_model.keras')

# Função para classificar a imagem
def classify_image(img):
    img = img.resize((224, 224))  # Redimensionar para o tamanho esperado
    img = np.array(img) / 255.0  # Normalizar a imagem
    img = np.expand_dims(img, axis=0)  # Adicionar batch dimension
    prediction = model.predict(img)
    confidence = prediction[0][0]
    status = 'aberta' if confidence > 0.5 else 'fechada'
    return status, confidence

# Interface do Streamlit
st.title("Classificador de Garrafas")

# Instruções para o usuário
st.write("Envie uma imagem para classificar se a garrafa está aberta ou fechada.")

# Upload de arquivo
uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Abrir a imagem
    img = Image.open(uploaded_file)

    # Exibir a imagem carregada
    st.image(img, caption="Imagem carregada", use_column_width=True)

    # Classificar a imagem
    st.write("Classificando a imagem...")
    status, confidence = classify_image(img)

    # Exibir os resultados
    st.write(f"**Status:** {status}")
    st.write(f"**Confiança:** {confidence:.2f}")
