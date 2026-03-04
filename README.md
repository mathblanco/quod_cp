# Quod — Extração do Dicionário de Dados (Anexo 1)

Pipeline de extração e estruturação do dicionário de dados a partir do PDF do Anexo 1.

---

## O que faz

Lê o `Anexo_1.pdf` (manual de arquivos do Cadastro Positivo), extrai os campos via análise de layout e salva o resultado estruturado em `.csv` e `.json` para uso posterior — inclusive como referência durante a modelagem.

---

## Estrutura do projeto

```
├── data/
│   └── Anexo_1.pdf
├── output/
│   ├── dicionario_dados.csv
│   └── dicionario_dados.json
├── src/
│   ├── extract_pdf.py     # Leitura e extração de texto do PDF
│   ├── transform.py       # Parsing do layout → DataFrame estruturado
│   └── save_data.py       # Exportação para CSV e JSON
└── main.py                # Entrypoint
```

---

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

O script imprime as primeiras 20 linhas extraídas no terminal e salva os arquivos em `output/`.

---

## Output

Ambos os arquivos representam o mesmo conteúdo em formatos distintos:

| Arquivo | Uso |
|---|---|
| `dicionario_dados.csv` | Análise em Excel / pandas |
| `dicionario_dados.json` | Consumo via API ou integração com outros sistemas |
