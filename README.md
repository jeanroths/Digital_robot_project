# Projeto simulação robô digital
O projeto Robô Digital tem por objetivo a elaboração de uma solução completa de integração entre as Tecnologias de Automação (TA) e as Tecnologias de Informação (TI). Trata-se de uma representação digital para um braço robótico com conexão em tempo real com sua contrapartida no mundo real.

## Tecnologias Usadas
- Backend em Flask;
- Banco de dados com SQLite3;
- Frontend em HTML;
- Godot Engine para simulação.

## Estrutura do projeto
Abaixo encontra-se a árvore de pastas do repositório:

``` bash
.
├── .gitattributes
├── README.md
├── venv
│   ├── Include/site/python3.10/greenlet
│   ├── Lib/site-packages
|   ├── pyvenv.cfg
│   ├── Scripts
│   │   ├── Activate.ps1
│   │   ├── Activate
│   │   ├── activate.bat
│   │   ├── deactivate.bat
│   │   ├── flask.exe
│   │   ├── pip.exe
│   │   ├── pip3.10.exe
│   │   ├── pip3.exe
│   │   ├── python.exe
│   │   ├── pythonw.exe
│   │   ├── src
│   │   |   └── app.py
│   │   |   ├── robot.db
│   │   |   ├── Simulacao_godot
│   │   |   |    └──.gitattributes
│   │   |   |    ├──.gitignore
│   │   |   |    ├── Braco.gd
│   │   |   |    ├── cena_simulacao.tscn
│   │   |   |    ├── millennium_falcon_interior_background_drawing_by_bantambb_dbowvuj-fullview.jpg
│   │   |   |    ├── millennium_falcon_interior_background_drawing_by_bantambb_dbowvuj-fullview.jpg.import
│   │   |   |    ├── pngwing.com.png
│   │   |   |    ├── pngwing.com.png.import
│   │   |   |    ├── project.godot
│   │   |   └── templates
│   │   |   |    └──index1.html
```
Os principais diretórios e arquivos do repositório são:
- A pasta (./Scripts) que contém a pasta (./src) com os scripts que contém os códigos do backend, frontend e simulação na Godot Engine;
- A pasta (./Simulacao_godot) que contêm os arquivos project.godot e Braco.gd que são os scripts responsáveis pela simulação do robô;
- A pasta (./templates) que contém o arquivo html que é o front de interface para o usuário fazer as requisições de posições do robô;
- Os arquivos app.py e robot.db na pasta (./src) que são o backend com as APIs em flask e o banco de dados conectado a ela.

## Backend
- No arquivo app.py, é possível encontrar o backend com as rotas de requisição GET e PUT, em que a primeira seleciona do banco de dados robot.db as colunas das posições X,Y,Z e rotação e passa esses valores em formato JSON e por meio do render_template conectado com o arquivo do front index1.html passa essas informações, e a segunda adiciona nas mesmas colunas novos valores no banco de dados por um INSERT em SQL e transforma esses valores em JSON para mandar para o front;
- Nesse arquivo é definido também o endereço de servidor local para hospedar a construção.

## Frontend
- No arquivo index1.html, é possível encontrar o frontend que,por meio de funções no seu Script, adiciona os valores em JSON definidos no backend para a página,ao acessar o endereço principal com a rota GET, e com esses valores ao apertar botões que estão no HTML que pedem para devolver o histórico e posições atuais, são inseridos na página HTML, assim como no endereço com a rota PUT em que novos valores são inserido pelo usuário, mandados para o banco de dados e transformados em JSON no backend.

## Simulação Godot
- Na pasta Simulacao_godot, ao ser aberta pela Godot Engine, é possível navegar pelas estruturas que compõem o simulador, e o script responsável por conectar-se com as requisições feitas pelo usuário e fazer com que haja a simulação de movimentação do robô é o Braco.gd;
- Nesse arquivo é feita uma requisição HTTP que se conecta com a rota de endereço definida pelo backend e é criada uma variável para pegar os valores em JSON desse backend, e por meio do acesso à propriedade da imagem colocada para simular o movimento do robô, os valores acessados pelo JSON são substitídos como coordenadas no eixo X e Y da interface, assim como os valores de rotação para essa imagem. Além disso, como é uma simulação de 2 dimensões, ou seja, abarca coordenadas em X e Y, para valores do eixo Z, a propriedade mudada da imagem foi a cor.
