import typer
from .scanner import escanear_projeto
from .ai_generator import gerar_readme_ia

app = typer.Typer()


@app.command()
def generate(path: str = "."):
    """
    Gera automaticamente um README.md usando IA
    """

    arquivos = escanear_projeto(path)

    readme = gerar_readme_ia(arquivos)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    typer.echo("README.md gerado com sucesso!")


if __name__ == "__main__":
    app()