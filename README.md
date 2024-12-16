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
## 8. Cenários de Alto Rendimento
### 8.1 Simulação de tráfego pesado
#### 8.1.1 Ferramenta para teste de carga:
Use ferramentas como Apache JMeter, Locust, ou K6 para simular 1.000 solicitações por segundo.
Configure múltiplos usuários simultâneos e distribua as requisições para endpoints relevantes da API Flask.
Meça latência, throughput, e taxas de erro.
#### 8.1.2 Resultados esperados:
Documente como a API se comporta sob tráfego pesado: latência média, porcentagem de erros (como 429 Too Many Requests), e consumo de recursos (CPU/RAM).
### 8.2. Plano de escalabilidade e balanceamento de carga
#### 8.2.1 Balanceamento de carga:
Use um balanceador de carga como NGINX ou AWS Application Load Balancer para distribuir requisições entre instâncias da API.
Configure o balanceamento com políticas como round-robin ou least-connections.
#### 8.2.2 Armazenamento em cache:
Integre caching usando Redis ou Memcached:
- Cacheie respostas para imagens idênticas.
- Reduza requisições duplicadas.
#### 8.2.3 Dimensionamento horizontal:
Implante a API em contêineres usando Docker.
Orquestre com Kubernetes ou AWS ECS para escalar horizontalmente com base em métricas (por exemplo, aumentar o número de réplicas quando o uso da CPU ultrapassar 70%).
#### 8.2.4 Dimensionamento vertical:
Configure escalabilidade vertical para servidores em que a API esteja hospedada (aumentar recursos de CPU/RAM).
Exemplos: aumente o tamanho da máquina EC2 na AWS ou redimensione a instância no Google Cloud.
## 9. Design do Banco de Dados
### 9.1 Requisitos:
#### 9.1.1 Logs de solicitações, incluindo:
- Metadados da imagem (nome do arquivo, tamanho, formato).
- Resultados da classificação (aberta/fechada).
- Registros de data e hora.
- Informações do cliente (IP, chave de API, user-agent).
#### 9.1.2 Proposta de design:
- SQL:
  - Banco relacional como PostgreSQL:
    - Tabela: request_logs
      - id (chave primária, UUID).
      - timestamp (data e hora).
      - metadata (JSON ou colunas separadas para cada metadado).
      - classification_result (string: "aberta" ou "fechada").
      - client_info (JSON ou colunas separadas como IP, user-agent).
    - Escalabilidade:
      - Use particionamento de tabelas baseado em tempo (ex.: particione por dia/mês).
      - Habilite réplicas de leitura para otimizar consultas de análise.
- NoSQL:
  - Banco não relacional como MongoDB:
      - Coleção: request_logs
  - Escalabilidade:
      - Configurar um cluster sharded para distribuir dados entre múltiplos servidores.
      - Habilitar backups automáticos e failover.

## 10. Monitoramento e Métricas
### 10.1 KPIs
- Tempo de resposta: Tempo médio de resposta em milissegundos.
- Taxa de erro: Percentual de requisições com falha (4xx e 5xx).
- Uso de recursos: CPU, memória, e latência por instância.
- Throughput: Número de requisições processadas por segundo.
### 10.2 Ferramentas de monitoramento:
#### 10.2.1 Grafana:
- Configure painéis para monitorar tempo de resposta e taxa de erro.
- Use Prometheus como back-end para coletar métricas.
#### 10.2.2 Log Management:
- Integre com Elastic Stack (ELK) para armazenar e visualizar logs.
- Analise erros e padrões de tráfego em tempo real.
#### 10.2 . Acompanhamento de logs de aplicações:
- Use ferramentas como New Relic ou DataDog para monitoramento detalhado de transações.
## 11. Segurança
### 11.1 Autenticação e validação:
#### 11.1.1 Chaves de API:
Exigir chaves de API únicas para cada cliente.
Revogar chaves comprometidas ou inativas.
#### 11.1.2 OAuth 2.0:
Implemente um fluxo de autenticação para clientes que exigem múltiplos acessos.
### 11.2 Validação de entrada:
#### 11.2.1 Validação de imagem:
Verifique o formato, tamanho, e tipo de imagem (ex.: apenas JPEG/PNG).
Use bibliotecas como Pillow para validação.
### 11.3 Outras medidas:
#### 11.3.1 Limitação de taxa:
Use bibliotecas como Flask-Limiter para restringir solicitações por cliente (ex.: 100 req/minuto).
#### 11.3.2 Higienização de entrada:
Proteja contra ataques injection (ex.: SQL Injection) validando inputs.
#### 11.3.3 HTTPS:
Habilite HTTPS com certificados TLS via Let's Encrypt.

