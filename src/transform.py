# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:44:11 2026

@author: mathe
"""

import re
import pandas as pd


def extrair_campos_layout(linhas):

    dados = []

    pattern = re.compile(r"^(\S+)\s+(.+?)\s+(Tag|Atributo)\s+(\[[^\]]+\])$")

    for linha in linhas:

        match = pattern.search(linha)

        if match:

            dados.append({
                "tag_ou_atributo": match.group(1),
                "nome_campo": match.group(2),
                "tipo": match.group(3),
                "multiplicidade": match.group(4)
            })

    return pd.DataFrame(dados)