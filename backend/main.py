from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI GitOps API",
    version="1.0"
)

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message":"Version GitOps automatique v5"}

@app.post("/chat")
def chat(data: Question):

    question = data.question.lower()

    if "bonjour" in question:
        answer = "Bonjour, comment puis-je vous aider ?"

    elif "gitops" in question:
        answer = "GitOps est une méthode de déploiement basée sur Git."

    elif "argocd" in question:
        answer = "ArgoCD synchronise automatiquement Kubernetes avec Git."

    elif "kubernetes" in question:
        answer = "Kubernetes orchestre les conteneurs."

    else:
        answer = "Je suis une IA de démonstration."

    return {
        "question": data.question,
        "answer": answer
    }