from socket import socket
from common import divisao_crc, str_to_binary

# Função que faz a codificação da palavra/dado
def encode_dado(dado, chave):
    tamanho_chave = len(chave)
    appended_dado = dado + '0' * (tamanho_chave - 1)
    resto = divisao_crc(appended_dado, chave)
    binario_codificado = dado + resto
    return binario_codificado

# Cria o socket a conecta na porta do receiver
s = socket()
port = 5050
s.connect(('127.0.0.1', port))

# Pega a mensagem a ser enviada e transforme em binário
input_string = input("\nMensagem: ")
binary = str_to_binary(input_string)
print("Dado em binário :", binary)

# Faz a codificação do binário junto com a chave do CRC
key = '1001'
binario =  encode_dado(input_string, key)

# Envio o dados em binário para o receiver
print("Dado a ser enviado ao receptor: ", binario)
s.sendto(binario.encode(),('127.0.0.1', 5050))

# Imprime a resposta do receiver
print("Resposta: ", s.recv(1024).decode(), "\n")