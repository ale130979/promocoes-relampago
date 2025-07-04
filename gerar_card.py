from PIL import Image, ImageDraw, ImageFont

def gerar_card_promocional():
    largura, altura = 1080, 1080
    imagem = Image.new('RGB', (largura, altura), color=(245, 245, 245))
    draw = ImageDraw.Draw(imagem)

    # Fontes
    fonte_titulo = ImageFont.truetype("arialbd.ttf", 40)
    fonte_normal = ImageFont.truetype("arial.ttf", 36)
    fonte_pequena = ImageFont.truetype("arial.ttf", 28)

    # Texto
    titulo = "Sofá Living Malibu 2,30m Cinza Bouclê - King House"
    de = "De: R$1.829,90"
    por = "Por: R$1.234,05 - 32% OFF no Pix"
    parcelado = "ou R$1.299 em 12x R$108,25 sem juros"
    link = "https://mercadolivre.com/sec/2U6HQSf"
    rodape = "✨ Design moderno, elegante e super confortável!"

    # Desenhar
    draw.text((60, 50), titulo, font=fonte_titulo, fill="black")
    draw.text((60, 150), de, font=fonte_normal, fill="gray")
    draw.text((60, 220), por, font=fonte_normal, fill="green")
    draw.text((60, 290), parcelado, font=fonte_normal, fill="black")
    draw.text((60, 380), link, font=fonte_pequena, fill="blue")
    draw.text((60, 450), rodape, font=fonte_pequena, fill="black")

    # Salvar
    imagem.save("card_promocional.png")
    print("Imagem salva como card_promocional.png")

gerar_card_promocional()