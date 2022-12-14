

import re
texto = input('Informe a str: ')
x = re.findall(r'\(?\d{2,3}\)?[\s\-]?\d{5}[\s\-]\d{4}', texto)
z = [re.sub(r'^\(?0|\D', '', i) for i in x]
formatados = [(f'({i[:2]}) {i[3:7]} {i[7:]}') for i in z]
print(formatados)