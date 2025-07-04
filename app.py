from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import telegram

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Configurações
TELEGRAM_TOKEN = "SEU_TOKEN_TELEGRAM"
TELEGRAM_CHAT_ID = "@SEU_CANAL"
MYZAP_URL = "http://localhost:3333/send-image"
NUMERO_DESTINO_WPP = "5511999999999"  # pode ser dinâmico depois

# Geração do card
def gerar_card():
    largura, altura = 1080, 1080
    imagem = Image.new('RGB', (largura, altura), color=(255, 255, 255))
    draw = ImageDraw.Draw(imagem)

    url_img_produto = "https://http2.mlstatic.com/D_NQ_NP_2X_803086-MLB54944096141_042023-F.webp"
    resp = requests.get(url_img_produto)
    img_produto = Image.open(BytesIO(resp.content)).resize((960, 540))
    imagem.paste(img_produto, (60, 20))

    fonte_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 38)
    fonte_texto = ImageFont.truetype("DejaVuSans.ttf", 32)
    fonte_pequena = ImageFont.truetype("DejaVuSans.ttf", 28)

    draw.rectangle([(40, 580), (1040, 1060)], fill=(250, 250, 250), outline=(220, 220, 220), width=2)

    titulo = "Sofá Living Malibu 2,30m Cinza Bouclê - King House"
    de = "De: R$1.829,90"
    por = "Por: R$1.234,05 - 32% OFF no Pix"
    parcelado = "ou R$1.299 em 12x R$108,25 sem juros"
    link = "https://mercadolivre.com/sec/2U6HQSf"
    rodape = "✨ Design moderno, elegante e super confortável!"

    draw.text((60, 600), titulo, font=fonte_titulo, fill="black")
    draw.text((60, 650), de, font=fonte_texto, fill="gray")
    draw.text((60, 700), por, font=fonte_texto, fill="green")
    draw.text((60, 750), parcelado, font=fonte_texto, fill="black")
    draw.text((60, 810), link, font=fonte_pequena, fill="blue")
    draw.text((60, 860), rodape, font=fonte_pequena, fill="black")

    imagem.save("card_promocional.png")

# Envia para Telegram
def enviar_telegram():
    legenda = (
        "🛋️ Sofá Living Malibu 2,30m Cinza Bouclê - King House\n"
        "De: R$1.829,90\n"
        "Por: R$1.234,05 - 32% OFF no Pix\n"
        "ou R$1.299 em 12x R$108,25 sem juros\n"
        "🔗 https://mercadolivre.com/sec/2U6HQSf\n"
        "✨ Design moderno, elegante e super confortável!"
    )
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    with open("card_promocional.png", "rb") as img:
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=img, caption=legenda)

# Envia para WhatsApp via MyZap
def enviar_whatsapp():
    legenda = (
        "🛋️ Sofá Living Malibu 2,30m Cinza Bouclê - King House\n"
        "De: R$1.829,90\n"
        "Por: R$1.234,05 - 32% OFF no Pix\n"
        "ou R$1.299 em 12x R$108,25 sem juros\n"
        "🔗 https://mercadolivre.com/sec/2U6HQSf"
    )
    with open("card_promocional.png", 'rb') as img:
        files = {'file': img}
        data = {
            'phone': NUMERO_DESTINO_WPP,
            'caption': legenda,
            'filename': 'card_promocional.png'
        }
        r = requests.post(MYZAP_URL, data=data, files=files)
        if r.status_code != 200:
            print("Erro WhatsApp:", r.text)

# Página inicial
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Gera e envia
@app.post("/gerar-e-enviar")
async def gerar_e_enviar():
    gerar_card()
    enviar_telegram()
    enviar_whatsapp()
    return RedirectResponse("/", status_code=303)
