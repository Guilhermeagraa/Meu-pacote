from PIL import Image, ImageOps

def preto_e_branco(imagem):
    return imagem.convert("L")

def inverter_cores(imagem):
    return ImageOps.invert(imagem)

def redimensionar(imagem, largura, altura):
    return imagem.resize((largura, altura))
