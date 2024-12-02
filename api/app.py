from flask import Flask,render_template,request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formacao')
def formacao():
    return render_template('formacao.html')

@app.route('/projetos')
def projetos():
    return render_template ('projetos.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)