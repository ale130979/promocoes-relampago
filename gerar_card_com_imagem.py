from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def gerar_card_promocional():
    largura, altura = 1080, 1080
    imagem = Image.new('RGB', (largura, altura), color=(255, 255, 255))
    draw = ImageDraw.Draw(imagem)

    # Carregar imagem do produto (sofá)
    url_imagem_produto = "https://http2.mlstatic.com/D_NQ_NP_2X_803086-MLB54944096141_042023-F.webp"  # Exemplo real
    response = requests.get(url_imagem_produto)
    img_produto = Image.open(BytesIO(response.content)).resize((960, 540))
    imagem.paste(img_produto, (60, 20))  # Topo

    # Fontes
    fonte_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 38)
    fonte_texto = ImageFont.truetype("DejaVuSans.ttf", 32)
    fonte_pequena = ImageFont.truetype("DejaVuSans.ttf", 28)

    # Caixa branca abaixo da imagem
    draw.rectangle([(40, 580), (1040, 1060)], fill=(250, 250, 250), outline=(220, 220, 220), width=2)

    # Texto
    titulo = "Sofá Living Malibu 2,30m Cinza Bouclê - King House"
    de = "De: R$1.829,90"
    por = "Por: R$1.234,05 - 32% OFF no Pix"
    parcelado = "ou R$1.299 em 12x R$108,25 sem juros"
    link = "https://mercadolivre.com/sec/2U6HQSf"
    rodape = "✨ Design moderno, elegante e super confortável!"

    # Desenhar textos
    draw.text((60, 600), titulo, font=fonte_titulo, fill="black")
    draw.text((60, 650), de, font=fonte_texto, fill="gray")
    draw.text((60, 700), por, font=fonte_texto, fill="green")
    draw.text((60, 750), parcelado, font=fonte_texto, fill="black")
    draw.text((60, 810), link, font=fonte_pequena, fill="blue")
    draw.text((60, 860), rodape, font=fonte_pequena, fill="black")

    # Salvar
    imagem.save("card_promocional.png")
    print("✅ Card salvo como 'card_promocional.png'")

gerar_card_promocional()