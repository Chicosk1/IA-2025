from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2-large")

def analyze_cars(cars):
    texto = "Analise os seguintes carros e recomende o melhor baseado em preço e localização:\n\n"
    for c in cars:
        texto += f"- {c['modelo']} ({c['site']}) - R${c['preco']} - Local: {c['local']}\n"
    
    texto += "\nResponda de forma breve com o carro mais vantajoso e o motivo."

    output = pipe(
        texto,
        max_new_tokens=200,
        temperature=0.7,
        do_sample=True,
        truncation=True,
        pad_token_id=50256
    )

    return output[0]["generated_text"]
