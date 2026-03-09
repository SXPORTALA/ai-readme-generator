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

