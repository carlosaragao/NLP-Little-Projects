from transformers import pipeline

def extract_entities(text):
    nlp = pipeline('ner', grouped_entities=True)
    result = nlp(text)
    return result

if __name__ == "__main__":
    text = input("Digite um texto para extração de entidades: ")
    result = extract_entities(text)
    for entity in result:
        print(f"Entidade: {entity['word']}, Tipo: {entity['entity_group']}, Score: {entity['score']:.4f}")


# PER (Person): Nomes de pessoas, incluindo indivíduos famosos, personagens históricos, etc.
# Exemplo: "Albert Einstein", "Barack Obama"

# ORG (Organization): Nomes de organizações, empresas, instituições, etc.
# Exemplo: "Google", "United Nations"

# LOC (Location): Nomes de locais geográficos, como cidades, países, regiões, etc.
# Exemplo: "New York", "Brazil"

# MISC (Miscellaneous): Entidades diversas que não se encaixam nas outras categorias, mas ainda são de interesse.
# Exemplo: "Nobel Prize", "iPhone"

# DATE (Date): Datas, períodos, e outras expressões temporais.
# Exemplo: "January 1, 2020", "last week"

# TIME (Time): Horas e períodos de tempo específicos.
# Exemplo: "3:00 PM", "two hours"

# MONEY (Money): Quantias monetárias e unidades de moeda.
# Exemplo: "$100", "€50"

# PERCENT (Percent): Porcentagens.
# Exemplo: "20%", "50 percent"

# GPE (Geopolitical Entity): Entidades políticas e geográficas.
# Exemplo: "United States", "European Union"

# FAC (Facility): Instalações e edifícios significativos.
# Exemplo: "Eiffel Tower", "Empire State Building"
