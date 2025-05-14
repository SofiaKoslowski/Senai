from flask import Flask, render_template,request
import os

# Define a pasta onde estão s arquivos HTML (neste caso, a raiz do projeto)
template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir)

# Direcionamento para base do index HTML
@app.route("/")
def home ():
    return render_template("Index2.html")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3000)