"""
Script: manipulacao_strings.py
Descrição:
Demonstra o uso de métodos importantes para manipulação de strings em Python:
upper, lower, title, strip, lstrip, rstrip, center e join.

Autor: Ronaldo Rhoney (exemplo)
"""

# String de exemplo com espaços extras
texto = "   python é incrível   "

# ==============================
# 1. upper() -> Converte todos os caracteres para MAIÚSCULOS
# ==============================
texto_upper = texto.upper()
print("upper():", texto_upper)

# ==============================
# 2. lower() -> Converte todos os caracteres para minúsculos
# ==============================
texto_lower = texto.lower()
print("lower():", texto_lower)

# ==============================
# 3. title() -> Converte a primeira letra de cada palavra para maiúscula
# ==============================
texto_title = texto.title()
print("title():", texto_title)

# ==============================
# 4. strip() -> Remove espaços do início e do fim da string
# ==============================
texto_strip = texto.strip()
print("strip():", texto_strip)

# ==============================
# 5. lstrip() -> Remove espaços apenas do lado esquerdo (início)
# ==============================
texto_lstrip = texto.lstrip()
print("lstrip():", texto_lstrip)

# ==============================
# 6. rstrip() -> Remove espaços apenas do lado direito (final)
# ==============================
texto_rstrip = texto.rstrip()
print("rstrip():", texto_rstrip)

# ==============================
# 7. center() -> Centraliza a string em um espaço definido
# Parâmetros:
# - largura total
# - caractere de preenchimento (opcional)
# ==============================
texto_centralizado = texto.strip().center(30, "-")
print("center():", texto_centralizado)

# ==============================
# 8. join() -> Junta elementos de uma lista em uma única string
# O separador é a string que chama o método
# ==============================
palavras = ["Python", "é", "muito", "poderoso"]

texto_join = " ".join(palavras)
print("join():", texto_join)

# ==============================
# Exemplo prático combinando métodos
# ==============================
resultado = "-".join(texto.strip().title().split())
print("Combinação de métodos:", resultado)