# Modelo para comunicação serial Arduino em uma arquitetura cliente/servidor
-> Script enviaDados.py envia um caractere definido, aguarda uma resposta do arduino e exibe os dados enviados.
-> Script main.cpp aguarda uma comunicação serial, recebe o caracter, verifica e devolve o valor requerido.
## Os dois scripts simulam uma arquiterura cliente/servidor muito simples e não implementa nenhum protocolo específico, ficando a cargo do programado definir a maneira que o script .py envia a requisição.

** É necessário instalar o pacote pyserial no script Python **
-> Versão usada nesse modelo: pyserial==3.5

Documentação:
-> https://pyserial.readthedocs.io/en/latest/index.html
-> https://www.arduino.cc/reference/en/language/functions/communication/serial/