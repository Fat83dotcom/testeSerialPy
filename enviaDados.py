import serial
from time import sleep

with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as conect:
    while 1:
        conect.reset_input_buffer()
        bufferDados: list = []
        while len(bufferDados) < 4:
            conect.write("u".encode('utf-8'))
            if conect.in_waiting > 0:
                recebeDados = conect.readline()
                decodificado = recebeDados.decode('utf-8')
                bufferDados.append(decodificado)
                print(decodificado)
            sleep(0.05)
            conect.write("p".encode('utf-8'))
            if conect.in_waiting > 0:
                recebeDados = conect.readline()
                decodificado = recebeDados.decode('utf-8')
                bufferDados.append(decodificado)
                print(decodificado)
            sleep(0.05)
            conect.write("1".encode('utf-8'))
            if conect.in_waiting > 0:
                recebeDados = conect.readline()
                decodificado = recebeDados.decode('utf-8')
                bufferDados.append(decodificado)
                print(decodificado)
            sleep(0.05)
            conect.write("2".encode('utf-8'))
            if conect.in_waiting > 0:
                recebeDados = conect.readline()
                decodificado = recebeDados.decode('utf-8')
                bufferDados.append(decodificado)
                print(decodificado)
            sleep(0.05)
        
        print(bufferDados)
        sleep(0.8)
