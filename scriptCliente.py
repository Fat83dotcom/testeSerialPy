import serial
from time import sleep

with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as conectSerial:
    while 1:
        conectSerial.reset_input_buffer()
        bufferDados: list = []
        while len(bufferDados) < 4:
            conectSerial.write("u".encode('utf-8'))
            if conectSerial.in_waiting > 0:
                dadosRecebidos = conectSerial.readline()
                dadosDecodificados = dadosRecebidos.decode('utf-8')
                bufferDados.append(dadosDecodificados)
                print(dadosDecodificados)
            sleep(0.05)
            conectSerial.write("p".encode('utf-8'))
            if conectSerial.in_waiting > 0:
                dadosRecebidos = conectSerial.readline()
                dadosDecodificados = dadosRecebidos.decode('utf-8')
                bufferDados.append(dadosDecodificados)
                print(dadosDecodificados)
            sleep(0.05)
            conectSerial.write("1".encode('utf-8'))
            if conectSerial.in_waiting > 0:
                dadosRecebidos = conectSerial.readline()
                dadosDecodificados = dadosRecebidos.decode('utf-8')
                bufferDados.append(dadosDecodificados)
                print(dadosDecodificados)
            sleep(0.05)
            conectSerial.write("2".encode('utf-8'))
            if conectSerial.in_waiting > 0:
                dadosRecebidos = conectSerial.readline()
                dadosDecodificados = dadosRecebidos.decode('utf-8')
                bufferDados.append(dadosDecodificados)
                print(dadosDecodificados)
            sleep(0.05)
        
        print(bufferDados)
        sleep(0.8)
