# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:44:48 2026

@author: mathe
"""

from src.extract_pdf import extrair_texto_pdf
from src.transform import extrair_campos_layout
from src.save_data import salvar_csv, salvar_json


caminho_pdf = "data/Anexo_1.pdf"

csv_saida = "output/dicionario_dados.csv"
json_saida = "output/dicionario_dados.json"


def main():

    linhas = extrair_texto_pdf(caminho_pdf)

    df = extrair_campos_layout(linhas)

    print(df.head(20))

    salvar_csv(df, csv_saida)

    salvar_json(df, json_saida)


if __name__ == "__main__":
    main()