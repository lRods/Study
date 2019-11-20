import os
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import DES

def main():
    os.system('cls')
    print("\n ----- Criptografia DES -----\n")
    print(" ENCRIPTAR\n")
    encrypt()

    print(" DECRIPTAR\n")
    decrypt()

    print("\n ----- FIM ----- \n")
    input("Pressione ENTER para finalizar...")


def encrypt():
    # Pegando chave para encriptacao que deve ter 8 bytes
    key = input(" Insira uma senha de 8 caracteres: ")
    while True:
        # validacao da chave com acoes caso seja maior ou menor que 8 caracteres
        if len(key) < 8 or len(key) > 8:
            os.system('cls')
            print("\n ----- Criptografia DES -----\n")
            print(" ENCRIPTAR\n")

            print(" *** A senha deve ter 8 caracteres!")
            key = input(" Insira novamente: ")
            continue
        else:
            break

    # Pegando a mensagem que sera encriptada
    plaintext = input("\n Insira o texto a ser encriptado: \n ")

    # Passando chave e mensagem para bytes para fazer a encriptacao
    keyBytes = key.encode()
    plaintextBytes = plaintext.encode()

    # Encriptando a mensagem, resultado em bytes
    cipher = DES.new(keyBytes, DES.MODE_OFB)
    msgBytes = cipher.encrypt(plaintextBytes)

    # Passando IV e a mensagem encriptada de bytes para base64, para o armazenamento no arquivo
    iv = b64encode(cipher.iv).decode('utf-8')
    msg = b64encode(msgBytes).decode('utf-8')

    # Colocando resultado no formato JSON para facilitar armazenamento e manipulacao
    result = json.dumps({'iv':iv, 'msg':msg})

    # Armazenando a chave no arquivo keyFile
    keyFile = open('data/keyFile.txt', 'w')
    keyFile.write(key)
    keyFile.close()

    # Armazenando o JSON da mensagem no arquivo msgJsonFile
    msgJsonFile = open('data/msgJsonFile.txt', 'w')
    msgJsonFile.write(result)
    msgJsonFile.close()

    # Armazenando texto plano para comparacao posterior no arquivo plaintxtFile
    plaintxtFile = open('data/plaintxtFile.txt', 'w')
    plaintxtFile.write(plaintext)
    plaintxtFile.close()

    print("\n Mensagem encriptada: \n", msg)
    print("\n Mensagem criptografada com sucesso.\n\n")


def decrypt():
    # Este loop eh para a validacao da chave, se bate com a chave salva no arquivo
    while True:
        # Pegando chave para decriptacao que deve ter 8 bytes
        key = input(" Insira a senha de 8 caracteres: ")
        while True:
            # validacao da chave com acoes caso seja maior ou menor que 8 caracteres
            if len(key) < 8 or len(key) > 8:
                os.system('cls')
                print("\n ----- Criptografia DES -----\n")
                print(" DECRIPTAR\n")

                print(" *** A senha deve ter 8 caracteres!")
                key = input(" Insira novamente: ")
                continue
            else:
                break

        # Comparando a chave digitada com a chave armazenada no arquivo keyFile
        keyFile = open('data/keyFile.txt', 'r')
        correctKey = keyFile.read()
        keyFile.close()

        if key == correctKey:
            # Passando a chave para bytes para a decriptacao
            keyBytes = key.encode()

            # pegando o result do arquivo msgJsonFile
            msgJsonFile = open('data/msgJsonFile.txt', 'r')
            result = msgJsonFile.read()
            msgJsonFile.close()

            # Separando IV e mensagem encriptada do JSON e decodificando o base64 para bytes
            b64 = json.loads(result)
            iv = b64decode(b64['iv'])
            msg = b64decode(b64['msg'])

            # Fazendo a decriptacao
            cipher = DES.new(keyBytes, DES.MODE_OFB, iv=iv)
            plaintext = cipher.decrypt(msg)
            plaintext = plaintext.decode('utf-8')

            # Comparando mensagem decriptada com a mensagem no arquivo plaintxtFile
            plaintxtFile = open('data/plaintxtFile.txt', 'r')
            correctPlaintext = plaintxtFile.read()
            plaintxtFile.close()

            if plaintext == correctPlaintext:
                print(" Texto decriptado: \n", plaintext)
                print("\n Decriptacao e validacao realizados com sucesso.")
            else:
                print(" Falha da decriptacao.")

            break
        else:
            os.system('cls')
            print("\n ----- Criptografia DES -----\n")
            print("DECRIPTAR\n")
            print(" Chave incorreta, falha na decriptacao. Tente novamente:\n")

main()