from django.shortcuts import render
from imagens.utils.image_gen import gerar_imagem
from io import BytesIO
import base64

def gerar_view(request):
    imagem_base64 = None

    if request.method == "POST":
        prompt = request.POST.get("descricao")
        try:
            imagem = gerar_imagem(prompt)
            buffer = BytesIO()
            imagem.save(buffer, format="PNG")
            imagem_base64 = base64.b64encode(buffer.getvalue()).decode()
        except Exception as e:
            print(f"Erro: {e}")

    return render(request, "gerador.html", {"imagem_base64": imagem_base64})
