from languages import detectar_linguagens

def gerar_readme(arquivos):

    linguagens = detectar_linguagens(arquivos)

    readme = "# 📦 Documentação do Projeto\n\n"

    readme += "## 🧠 Linguagens detectadas\n\n"

    for lang in linguagens:
        readme += f"- {lang}\n"

    readme += "\n---\n"

    readme += "## 📁 Estrutura do projeto\n\n"

    for arquivo in arquivos:
        readme += f"- {arquivo}\n"

    return readme