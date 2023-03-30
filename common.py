from typing import Union

def xor(a , b):
    result = []

    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def divisao_crc(dado , chave):
    tamanho_chave = len(chave)
    tmp = dado[0:tamanho_chave]

    while tamanho_chave < len(dado):
        if tmp[0] == '1':
            tmp = xor(chave,tmp) + dado[tamanho_chave]
        else:
            tmp = xor('0' * tamanho_chave,tmp) + dado[tamanho_chave]
        tamanho_chave += 1

    if tmp[0] == '1':
        tmp = xor(chave, tmp)
    else:
        tmp = xor('0' * tamanho_chave, tmp)

    resultado_validacao = tmp
    return resultado_validacao

def str_to_binary(string:str) -> Union[str, None]:

    if not string:
        return None

    binary = ''.join(format(ord(x),'b')for x in string)
    return binary