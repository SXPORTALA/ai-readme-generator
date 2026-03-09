import os

def escanear_projeto(pasta):

    estrutura = []

    for root, dirs, files in os.walk(pasta):

        for file in files:
            caminho = os.path.join(root, file)
            estrutura.append(caminho)

    return estrutura