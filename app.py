import os
from flask import Flask, request
from groq import Groq
app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_KEY"))
@app.route("/")
def home():
    return "JARVIS ONLINE"
@app.route("/comando")
def comando():
    q = request.args.get("c","oi")
    r = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":q}])
    return r.choices[0].message.content
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
