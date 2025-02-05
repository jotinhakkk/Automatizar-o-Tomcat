import subprocess
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def styles():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'style.css')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

tomcat_bin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apache-tomcat-9.0.93", "bin")
start_bat_file = os.path.join(tomcat_bin_path, "startup.bat")
shutdown_bat_file = os.path.join(tomcat_bin_path, "shutdown.bat")
os.environ['CATALINA_HOME'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apache-tomcat-9.0.93")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-bat')
def start_bat():
    if not os.path.exists(start_bat_file):
        return f"Arquivo BAT não encontrado em: {start_bat_file}"
    try:
        subprocess.Popen(
            ["cmd", "/c", "start", "", start_bat_file],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
            env=os.environ
        )
        return "Servidor iniciado com sucesso!"
    except Exception as e:
        return f"Erro ao iniciar o servidor: {e}"

@app.route('/stop-bat')
def stop_bat():
    if not os.path.exists(shutdown_bat_file):
        return f"Arquivo BAT não encontrado em: {shutdown_bat_file}"
    try:
        subprocess.Popen(
            ["cmd", "/c", "start", "", shutdown_bat_file],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
            env=os.environ
        )
        return "Servidor parado com sucesso!"
    except Exception as e:
        return f"Erro ao parar o servidor: {e}"

if __name__ == '__main__':
    app.run(debug=True)
