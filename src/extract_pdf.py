import pdfplumber


def extrair_texto_pdf(caminho_pdf):

    linhas = []

    with pdfplumber.open(caminho_pdf) as pdf:

        for pagina in pdf.pages:

            texto = pagina.extract_text()

            if texto:
                linhas.extend(texto.split("\n"))

    return linhas