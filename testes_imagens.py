from image_tools import abrir_imagem, mostrar_imagem, salvar_imagem
from image_tools import preto_e_branco, inverter_cores, redimensionar

# Abrir imagem
img = abrir_imagem("minha_imagem.jpg")

# Aplicar filtro preto e branco
img_pb = preto_e_branco(img)
mostrar_imagem(img_pb)
salvar_imagem(img_pb, "minha_imagem_pb.jpg")

# Inverter cores
img_invertida = inverter_cores(img)
mostrar_imagem(img_invertida)
salvar_imagem(img_invertida, "minha_imagem_invertida.jpg")

# Redimensionar
img_red = redimensionar(img, 300, 300)
mostrar_imagem(img_red)
salvar_imagem(img_red, "minha_imagem_red.jpg")
