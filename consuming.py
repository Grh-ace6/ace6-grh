import os
import requests

# Função para baixar e salvar como PDF os boletins
def download_pdf(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("PDF baixado com sucesso!")
    else:
        print("Erro ao baixar o PDF:", response.status_code)


# Controles de loop/consumo_api
start_id = 1150
loop_count = 662

# Loop que vai pegar os boletins
for _ in range(loop_count):
    url = f"https://sipac.sig.ufal.br/public/baixarBoletim.do?publico=true&idBoletim={start_id}"
    filename = f"boletins/BOLETIM_{start_id}.pdf"  # Alteração aqui: adição da extensão .pdf
    download_pdf(url, filename)
    start_id += 1

print("Download dos boletins concluído!")
