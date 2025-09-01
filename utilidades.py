from PIL import Image

def abrir_imagem(caminho):
    return Image.open(caminho)

def mostrar_imagem(imagem):
    imagem.show()

def salvar_imagem(imagem, caminho):
    imagem.save(caminho)
