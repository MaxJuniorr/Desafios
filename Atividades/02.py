import re
texto = '(091)91234 5678 91 91234 5678 45565 91-91234-5678 cavalo (91) 91234-5678'
expressão = r'\(?\d{2,3}\)?[\s\-]?\d{5}[\s\-]\d{4}'
x = re.findall(expressão, texto)
y = [re.sub(r'\(0','', i) for i in x]
nova = [re.sub(r'\D', '', i) for i in y]
formatados = [(f'({i[:2]}) {i[3:7]} {i[7:]}') for i in nova]
print(formatados)