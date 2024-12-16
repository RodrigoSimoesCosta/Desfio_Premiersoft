# Desfio_Premiersoft
Criação de API para Detecção de Garrafa Aberta/Fechada com Escalabilidade Considerações
# Objetivo:
Desenvolver e implementar uma API Flask capaz de identificar se uma garrafa de cerveja está aberta ou fechada com base em imagens. Este desafio avalia sua expertise em Machine Learning, Computer Vision, desenvolvimento de API, design de infraestrutura e implantação de soluções escaláveis e confiáveis para aplicações práticas.
# Descrição do desafio:
Uma de nossas marcas de cerveja visa automatizar a detecção do status da garrafa (aberta ou fechada) por meio de uma API escalável e eficiente. Sua tarefa é construir uma prova de conceito (PoC) que classifique o status da garrafa, forneça uma pontuação de confiança para o resultado, exponha essa funcionalidade por meio de uma API baseada em Flask e aborde considerações de infraestrutura para implantação e escalabilidade.
# Solução
Desenvolvedor: Rodrigo Simões Costa
Data: 16/12/2024
## 1. Criação do modelo (desafio_premier_soft.py)
Nome do arquivo: desafio_premier_soft.py
Linguagem: Criamos um modelo em python que segue as seguintes etapas:
### 1.1 Instalação de Pacotes e Importação das Bibliotecas:
instalamos os pacotes e as bilbiotecas necessárias
### 1.2 Dados:
Pegamos o conjunto de dados proposto que tinha 8589 imagens e selecionamos de maneira aleatória 500 imagens de garrafas abertas e 500 imagens de garrafas fechadas e criamos duas pastas "img_path_fechada" e "img_path_aberta" para criarmos o nosso conjunto de dados do projeto.
### 1.3 Pré-processamento dos dados:
a) Redimensionamos as imagens para 224x224 pixels.
b) Geramos novas imagens com o ImageDataGenerator para treinamento do nosso modelo.
c) Utilizamos uma rede neural convolucional (CNN) e parametrizamos com o models.Sequential, especificando as camadas de convolução, pulling, flatten e dense.
d) Devido as limitações de recurso computacional e tempo, usamos 10 épocas para treinamento, tendo uma acurácia de 99,48% na classificação das imagens das garrafas como "aberta" ou "fechada".
e) Salvamos o modelo "garrafa_model.keras".
## Criação da API Flask (app.py)
a) Utilizamos o flask para a criação da API (app.py).
b) Implementamos tratamento de erros para entradas inválidas. 
## Criação de uma interface para interagir com a API e realizar testes (app_streamlit.py)
a) Utilizamos o streamlit para a criação da interface (app_streamlit.py)
b) a url que está rodando esta infterface do streamlit é http://localhost:8501/


