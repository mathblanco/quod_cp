# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:44:33 2026

@author: mathe
"""

def salvar_csv(df, caminho):

    df.to_csv(caminho, index=False)


def salvar_json(df, caminho):

    df.to_json(
        caminho,
        orient="records",
        force_ascii=False,
        indent=4
    )