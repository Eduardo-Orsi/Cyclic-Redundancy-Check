from socket import socket
from common import divisao_crc

# Função que faz a decodificação da palavra/dado
def decode_dado(dado, chave):
    tamanho_chave = len(key)
    appended_data = dado.decode() + '0' * (tamanho_chave - 1)
    resto = divisao_crc(appended_data, chave)
    return resto

# Cria o socket que receberá dados
s = socket()
port = 5050
s.bind(('127.0.0.1', port))
s.listen(5)
print("Socket criado e escutando chamadas \n")


while True:

    # Recebe dados vindos do sender
    c , addr = s.accept()
    print('Conectou com: ',addr)
    data = c.recv(1024)

    # Valida se o dado foi recebido e imprime o mesmo
    if not data:
        break
    print("Dado recebido em binário:",data.decode())

    # Faz a decodificação do dado e valida o mesmo
    key = '1001'
    resto = decode_dado(data,key)
    print(f"Resto do MOD: {resto} \n")

    temp = "0" * (len(key)-1)
    if resto == temp:
        c.sendto(("Dados recebido sem erros: " + data.decode()).encode(),('127.0.0.1',5050))
    else:
        c.sendto(("Erro no dado recebido!").encode(),('127.0.0.1',5050))

    # Fecha a conexão
    c.close()
