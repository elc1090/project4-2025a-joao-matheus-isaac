import os
import requests
from PIL import Image
from io import BytesIO

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

def gerar_imagem(prompt):
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"inputs": prompt}
    response = requests.post(MODEL_URL, headers=headers, json=data)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Erro na geração da imagem: {response.status_code} - {response.text}")
