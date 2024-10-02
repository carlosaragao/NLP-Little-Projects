from transformers import pipeline

sentiment_pipeline = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result

def main():
    print("Análise de Sentimento. Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Encerrando a análise de sentimento. Até mais!")
            break
        result = analyze_sentiment(user_input)
        print(f"Sentimento: {result['label']}, Score: {result['score']:.4f}")

if __name__ == "__main__":
    main()