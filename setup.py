from setuptools import setup, find_packages

setup(
    name="readme-gen",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "google-genai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "readme-gen=readme_gen.cli:app"
        ]
    }
)