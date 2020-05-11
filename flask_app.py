from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login')
def outro_inicio():
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)