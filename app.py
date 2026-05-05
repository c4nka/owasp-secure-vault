import os
from flask import Flask, render_template
from routes.vulnerable import vul_bp

app = Flask(__name__)
# Ortam değişkeninden gizli anahtarı al, yoksa varsayılanı kullan
app.secret_key = os.environ.get("SECRET_KEY", "gizli_anahtar_varsayilan")

# Rotaları (Blueprints) uygulamaya kaydet
app.register_blueprint(vul_bp, url_prefix="/vulnerable")
# TODO: Kusursuz rota kodlandığında buraya eklenecek.

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
