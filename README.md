Tomcat Server Manager

Este projeto automatiza a configuração e inicialização do Apache Tomcat por meio de uma interface web simples, construída com Flask. Ele permite iniciar e parar o servidor Tomcat com um clique, sem necessidade de abrir manualmente o terminal.

Funcionalidades

Interface Web com Flask: Fornece uma página HTML para interação.
Iniciar o Servidor: Executa o script startup.bat do Tomcat automaticamente.
Parar o Servidor: Executa o script shutdown.bat para desligar o servidor.
Configuração Automática: Define CATALINA_HOME automaticamente para evitar configurações manuais.

Tecnologias Utilizadas
 
Python (Flask, subprocess)
Apache Tomcat
HTML/CSS (para a interface básica)

Como Usar

Configurar o Tomcat: Coloque a pasta apache-tomcat-9.0.93 no mesmo diretório do script.

Instalar dependências:
pip install flask

Executar a aplicação:
python script.py

Acessar a interface: No navegador, vá para http://127.0.0.1:5000/.
