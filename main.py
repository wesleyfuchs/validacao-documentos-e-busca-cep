
# def format_cpf(self):
#     fatia_um = self.cpf[:3]
#     fatia_dois = self.cpf[3:6]
#     fatia_tres = self.cpf[6:9]
#     fatia_quatro = self.cpf[9:]
#     return (
#         "{}.{}.{}-{}".format(
#             fatia_um,
#             fatia_dois,
#             fatia_tres,
#             fatia_quatro
#         )
#     )

#
# print(cpf)

from cpf_cnpj import Documento


exemplo_cpf = "01234567890"
exemplo_cnpj = "35379838000112"

documento_cpf = Documento.cria_documento(exemplo_cpf)
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
print(documento_cpf)
print(documento_cnpj)

from telefones_br import Telefones
import re

telefone = "552126481234"

telefone_objeto = Telefones(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)

from datas import DatasBr
from datetime import datetime, timedelta

cadastro = DatasBr()
print(cadastro)

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1, hours=20)
#
# print(hoje - amanha)

hoje = DatasBr()
print(hoje.tempo_cadastro())

import requests

from acesso_cep import BuscaEndereco
cep = "80060120"
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r)

# a = objeto_cep.acessa_via_cep()
# print(a)
# print(type(a))
# print(dir(a))
# print(a.text)
# print(a.json())
# print(a.json()['cep'])
# print(a.json()['localidade'])

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)