import re
texto = '(091)91234 5678 91 91234 5678 45565 91-91234-5678 cavalo (91) 91234-5678'
expressão = r'\(?\d{2,3}\)?[\s\-]?\d{5}[\s\-]\d{4}'
print(re.findall(expressão, texto))