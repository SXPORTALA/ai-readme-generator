# 🤖 Gerador de README com IA

Bem-vindo ao **Gerador de README com IA**! Esta é uma ferramenta poderosa para automatizar a criação de READMEs detalhados e profissionais para os seus projetos Python. Utilizando inteligência artificial, ele analisa a estrutura do seu projeto e gera conteúdo relevante, poupando seu tempo e garantindo que sua documentação esteja sempre atualizada.

## ✨ Recursos

*   **Geração de READMEs assistida por IA:** Crie READMEs completos com base na análise do seu código e estrutura de arquivos.
*   **Análise Automática do Projeto:** O `scanner.py` examina o seu diretório para entender a composição do projeto.
*   **Interface de Linha de Comando (CLI):** Fácil de usar através do terminal com o `cli.py`.
*   **Configuração via Variáveis de Ambiente:** Gerencie chaves de API e outras configurações sensíveis usando o arquivo `.env`.
*   **Extensível:** Estrutura modular permite fácil adição de novas funcionalidades ou integração com diferentes modelos de IA.

## 🚀 Instalação

Siga estes passos para configurar e executar o Gerador de README em seu ambiente local:

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd gerador-readme
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuração

Para usar a funcionalidade de IA, você precisará de uma chave de API para o serviço de IA que está sendo utilizado (por exemplo, OpenAI).

1.  **Crie um arquivo `.env` na raiz do seu projeto** (na mesma pasta que `main.py`).
2.  **Adicione sua chave de API** e quaisquer outras configurações necessárias, como no exemplo:

    ```env
    OPENAI_API_KEY=sua_chave_secreta_aqui
    # Outras variáveis de ambiente podem ser adicionadas aqui
    ```

    *Certifique-se de que o arquivo `.env` esteja listado no seu `.gitignore` para evitar que suas chaves de API sejam versionadas.*

## 💡 Uso

Após a instalação e configuração, você pode gerar um README para o seu projeto:

1.  **Navegue até a raiz do seu projeto** (onde o `main.py` e `.env` estão).

2.  **Execute o gerador:**
    ```bash
    python main.py
    ```

    Ou, se for uma aplicação CLI empacotada:
    ```bash
    gerador-readme generate
    ```

    O script irá analisar o seu projeto e gerar um arquivo `README.md` na raiz do seu diretório.

## 📂 Estrutura do Projeto

```
.
├── .env                  # Variáveis de ambiente
├── .vs/                  # Arquivos de solução do Visual Studio (ignorados)
├── __pycache__/          # Cache de bytecode Python (ignorados)
├── gerador-readme.pyproj # Projeto Python do Visual Studio
├── gerador-readme.slnx   # Solução do Visual Studio
├── generator.py          # Lógica principal de geração
├── main.py               # Ponto de entrada da aplicação
├── readme_gen/           # Pacote principal da lógica do gerador
│   ├── ai_generator.py   # Módulo para interação com APIs de IA
│   ├── cli.py            # Módulo da interface de linha de comando
│   ├── scanner.py        # Módulo para escanear a estrutura do projeto
│   ├── __init__.py
│   └── __pycache__/
├── readme_gen.egg-info/  # Metadados do pacote Python (ignorados)
├── requirements.txt      # Dependências do projeto
├── setup.py              # Script de setup para distribuição do pacote
└── README.md             # Este arquivo README (gerado por esta ferramenta!)
```

## 🤝 Contribuição

Sinta-se à vontade para contribuir com este projeto! Se você tiver sugestões, relatórios de bugs ou quiser implementar novos recursos, por favor:

1.  Faça um fork do repositório.
2.  Crie uma nova branch (`git checkout -b feature/minha-feature`).
3.  Faça suas alterações e commit-as (`git commit -m 'feat: Minha nova feature'`).
4.  Envie para a branch (`git push origin feature/minha-feature`).
5.  Abra um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a [SUA LICENÇA AQUI, por exemplo, MIT License](LICENSE).
=======
# AI README Generator

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Gerador automático de **README.md** usando Inteligência Artificial.
A ferramenta analisa a estrutura de um projeto e gera documentação automaticamente.

---

# 🚀 Features

* 🔍 Analisa automaticamente a estrutura do projeto
* 🤖 Usa IA para gerar README profissional
* 📄 Gera documentação em Markdown
* ⚡ Funciona com qualquer projeto local

---

# 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SXPORTALA/gerador-readme.git
cd gerador-readme
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```
GEMINI_API_KEY=sua_chave_aqui
```

Essa chave será usada para acessar o modelo **Google Gemini**.

---

# ▶️ Uso

Execute o gerador:

```bash
python -m readme_gen.cli .
```

Ou analise outra pasta:

```bash
python -m readme_gen.cli caminho/do/projeto
```

Depois da execução será criado automaticamente:

```
README.md
```

---

# 🧪 Exemplo

### Estrutura do projeto analisado

```
meu-projeto
│
├─ main.py
├─ api.py
└─ utils.py
```

### README gerado

```
# Meu Projeto

## Descrição
Este projeto fornece uma API simples em Python.

## Instalação
pip install -r requirements.txt

## Uso
python main.py
```

---

# 📂 Estrutura do Projeto

```
gerador-readme
│
├─ readme_gen
│  ├─ cli.py
│  ├─ scanner.py
│  └─ ai_generator.py
│
├─ requirements.txt
└─ README.md
```

---

# 🔒 Segurança

Nunca envie sua chave de API para o repositório.

Adicione ao `.gitignore`:

```
.env
__pycache__/
*.pyc
```

---

# 🧠 Tecnologias

* Python
* IA com **Google Gemini**
* Manipulação de arquivos

---

# 📄 Licença

MIT License

>>>>>>> 10cb49499c6bbbc0b794abf6d6b628945fd1ed1c
