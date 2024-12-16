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
Instalamos os pacotes e as bilbiotecas necessárias
### 1.2 Dados:
Pegamos o conjunto de dados proposto que tinha 8589 imagens e selecionamos de maneira aleatória 500 imagens de garrafas abertas e 500 imagens de garrafas fechadas e criamos duas pastas "img_path_fechada" e "img_path_aberta" para criarmos o nosso conjunto de dados do projeto.
### 1.3 Pré-processamento dos dados:
a) Redimensionamos as imagens para 224x224 pixels.
b) Geramos novas imagens com o ImageDataGenerator para treinamento do nosso modelo.
c) Utilizamos uma rede neural convolucional (CNN) e parametrizamos com o models.Sequential, especificando as camadas de convolução, pulling, flatten e dense.
d) Devido as limitações de recurso computacional e tempo, usamos 10 épocas para treinamento, tendo uma acurácia de 99,48% na classificação das imagens das garrafas como "aberta" ou "fechada".
e) Salvamos o modelo "garrafa_model.keras".
## 2. Criação da API Flask (app.py)
a) Utilizamos o flask para a criação da API (app.py).
b) Implementamos tratamento de erros para entradas inválidas. 
## 3. Criação de uma interface para interagir com a API e realizar testes (app_streamlit.py)
a) Utilizamos o streamlit para a criação da interface (app_streamlit.py)
b) a url que está rodando esta infterface do streamlit é http://localhost:8501/
## 4. requirements.txt
Colocamos os requisitos necessários para rodar esta solução no requirements.txt
## 5. Criamos arquivos para a conteinerização
a) Dockerfile-api (para a API)
b) Dockerfile-model (para o modelo)
c) Dockerfile-frontend (para o streamlit)
d) docker-compose.yml
## 6. Sugestão de possíveis casos de uso para esta solução
Esta ferramenta pode ser aproveitada em uma linha de produção de engarramento de bebidas.
Ao final do processo, teríamos o algoritmo atuando no controle da qualidade e identificando se as garrafas, após o recebimento do líquido, elas foram fechadas ou não.
## 7. Proposta de Infraestrutura Escalável no GCP
### 7.1. Frontend (Streamlit)
Implantar o Streamlit App no Cloud Run, garantindo escalabilidade e alta disponibilidade para a interface.
### 7.2. Backend (API Flask)
Implantar a API Flask no Cloud Run, conectada ao modelo de inferência.
O modelo pode ser otimizado para inferência rápida (TensorFlow Lite ou ONNX).
### 7.3. Banco de Dados
Utilizar Cloud Storage para armazenar imagens e Firestore para logs e metadados das inferências.
### 7.4. Balanceamento e Segurança
Configurar um Cloud Load Balancer para distribuir tráfego entre instâncias da API.
Usar API Gateway para gerenciar autenticação e acessos.
### 7.5. Monitoramento e Resiliência
Utilizar Cloud Monitoring para métricas (latência, erros) e alertas automáticos.
Configurar backups automáticos no Firestore e escalabilidade automática com o Cloud Run.
### 7.6. Escalabilidade
Cloud Run ajusta instâncias automaticamente conforme a demanda.
Projetar para tolerância a falhas com redundância geográfica.
