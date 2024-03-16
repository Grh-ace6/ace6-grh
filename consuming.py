#Função utilizar os ids para baixar os pdf's
import requests
import PyPDF2


#Função para baixar e salvar como PDF os boletins
def download_pdf(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("PDF baixado com sucesso!")
    else:
        print("Erro ao baixar o PDF:", response.status_code)


# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_filename):
    text = ""
    with open(pdf_filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

#Controles de loop/consumo_api
start_id = 1150
loop_count = 662

#Construindo o url e nome do arquivo
url = f"https://sipac.sig.ufal.br/public/baixarBoletim.do?publico=true&idBoletim={start_id}"
filename = f"/boletins/BOLETIM_{start_id}"

#Loop que vai pegar os boletins
for _ in range(loop_count):
    url = f"https://sipac.sig.ufal.br/public/baixarBoletim.do?publico=true&idBoletim={start_id}"
    filename = f"/boletins/BOLETIM_{start_id}"
    download_pdf(url, filename)
    start_id+=1

#Até aqui baixando tudo desde de 2022, :D