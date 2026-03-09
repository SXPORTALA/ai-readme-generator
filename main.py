import scanner
import ai_generator

pasta = input("Digite o caminho do projeto: ")

arquivos = scanner.escanear_projeto(pasta)

readme = ai_generator.gerar_readme_ia(arquivos)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README gerado com IA!")