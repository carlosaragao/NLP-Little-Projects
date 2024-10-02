from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline('summarization')
    result = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return result

if __name__ == "__main__":
    text = input("Digite um texto longo para resumo: ")
    result = summarize_text(text)
    print(result[0]['summary_text'])