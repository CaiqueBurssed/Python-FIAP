import json

# with open("bd.json", "r") as arquivo_json:
#     dic = json.load(arquivo_json)
#     for chave, dados in dic.items():
#         print(chave + " | " + str(dados))

dicionario = {
  "CHAVES":["CHAVES DO 8", "14/04/2022", "RECEP_01"],
  "QUICO":["QUICO FLORES", "24/04/2022", "RAIOX_01"],
  "FLORINDA": ["DONA FLORINDA", "18/04/2022", "RECEP_03"]
}

print(dicionario)

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, "bd1.json")
