from flask import Flask, render_template

app = Flask(__name__)

formations = [
    {"id": 1, "titre": "DevOps & CI/CD", "duree": "40h", "niveau": "Intermédiaire"},
    {"id": 2, "titre": "Docker & Kubernetes", "duree": "30h", "niveau": "Avancé"},
    {"id": 3, "titre": "Python pour le Web", "duree": "25h", "niveau": "Débutant"},
    {"id": 4, "titre": "Linux Administration", "duree": "20h", "niveau": "Intermédiaire"},
    {"id": 5, "titre": "Sécurité Réseau", "duree": "35h", "niveau": "Avancé"},
]

@app.route("/")
def index():
    return render_template("HomePage.html")

@app.route("/formations")
def index():
    return render_template("index.html", formations=formations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)