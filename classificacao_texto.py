from transformers import pipeline

classifier_pipeline = pipeline('zero-shot-classification')

def classify_text(text):
    labels = ["esportes", "política", "tecnologia", "entretenimento"]
    result = classifier_pipeline(text, candidate_labels=labels)
    return result

def main():
    print("Classificação de Texto. Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Encerrando a classificação de texto. Até mais!")
            break
        result = classify_text(user_input)
        print(result)

if __name__ == "__main__":
    main()