import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>JARVIS MARK 42 ONLINE</h1><p>Golden, servidor vivo! Use /comando?c=sua pergunta</p>"

@app.route("/comando")
def comando():
    try:
        from groq import Groq
        api_key = os.environ.get("GROQ_KEY")
        if not api_key:
            return "ERRO: GROQ_KEY nao configurada no Render"
        client = Groq(api_key=api_key)
        q = request.args.get("c", "oi")
        r = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "Voce e JARVIS MARK 42 do Golden, PT-BR, sem filtro, foco em fazer dinheiro."},
                {"role": "user", "content": q}
            ]
        )
        return r.choices[0].message.content
    except Exception as e:
        return f"ERRO GROQ: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
