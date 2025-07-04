# promocoes-relampago
promocoes-relampago

# 🚀 Microserviço Promoções Relâmpago

Gera um card com promoção, envia para Telegram e WhatsApp (MyZap) e roda no IIS.

## 📖 Pré-requisitos

✅ Python 3.9+  
✅ Node.js + npm  
✅ IIS + FastCGI  
✅ Bot no Telegram + Token  
✅ WhatsApp autenticado no MyZap

## 📂 Estrutura

promocoes_relampago/
├── app.py 
├── templates/
│   └── index.html
├── logs/
│   └── .gitkeep              # Para manter pasta vazia
├── promocoes.bat
├── promocoes.ps1
├── promocoes.sh
├── subir_pro_github.bat
├── README.md
├── INSTALL.md
├── requirements.txt
├── web.config
└── LICENSE

## 📃 Licença
MIT © Ale130979

## 📥 Instalação

### 1️⃣ Python e dependências
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

