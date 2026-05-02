"""
Script: fatiamento_strings.py
Descrição:
Demonstra o uso de fatiamento (slicing) de strings em Python.

Autor: Ronaldo Rhoney (exemplo)
"""

# ==============================
# String de exemplo
# ==============================
texto = "Ronaldo Rhoney Martins"

# Índices da string:
#  P  y  t  h  o  n     é     p  o  d  e  r  o  s  o
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

print("\nTexto original:", texto)

# ==============================
# 1. Acessando um único caractere
# ==============================
print("\nPrimeira letra:", texto[0])     # 'P'
print("Última letra:", texto[-1])       # 'o' (índice negativo começa do final)

# ==============================
# 2. Fatiamento básico [início:fim]
# O caractere do índice 'fim' NÃO é incluído
# ==============================
print("\nPrimeira palavra:", texto[0:6])   # 'Python'
print("Segunda palavra:", texto[7:])      # do índice 7 até o final

# ==============================
# 3. Omitindo índices
# ==============================
print("\nDo início até índice 5:", texto[:6])  # mesmo que [0:6]
print("Do índice 7 até o final:", texto[7:])  # mesmo que [7:len(texto)]

# ==============================
# 4. Fatiamento com passo [início:fim:passo]
# ==============================
print("\nPulando de 2 em 2:", texto[0:17:2])  # pega de 2 em 2 caracteres

# ==============================
# 5. Invertendo a string
# ==============================
print("\nTexto invertido:", texto[::-1])

# ==============================
# 6. Usando índices negativos
# ==============================
print("\nÚltimos 3 caracteres:", texto[-3:])   # 'oso'
print("Removendo último caractere:", texto[:-1])

# ==============================
# 7. Aplicação prática
# ==============================
print("\n--- Aplicação prática ---")

# Exemplo: extraindo domínio de um e-mail
email = "usuario@gmail.com"

# Encontrando posição do '@'
posicao_arroba = email.index("@")

# Pegando o domínio após o '@'
dominio = email[posicao_arroba + 1:]

print("Email:", email)
print("Domínio:", dominio)

# ==============================
# 8. Outro exemplo prático
# ==============================
# Formatando uma data
data = "2026-05-02"

ano = data[0:4]
mes = data[5:7]
dia = data[8:10]

print("\nData original:", data)
print("Data formatada:", f"{dia}/{mes}/{ano}")

# ==============================
# Conclusão
# ==============================
"""
Resumo:

texto[início:fim] -> pega uma parte da string
texto[início:fim:passo] -> controla o intervalo
índices negativos -> começam do final
[::-1] -> inverte a string

Muito usado em:
✔ tratamento de dados
✔ análise de strings
✔ manipulação de textos e arquivos
"""