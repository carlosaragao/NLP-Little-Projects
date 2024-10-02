from textblob import TextBlob

def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

if __name__ == "__main__":
    text = input("Digite um texto para correção ortográfica: ")
    corrected_text = correct_spelling(text)
    print(f"Texto corrigido: {corrected_text}")