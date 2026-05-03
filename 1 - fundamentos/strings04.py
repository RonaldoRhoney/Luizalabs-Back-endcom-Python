"""
Script: strings_multiplas_linhas.py
Descrição:
Demonstra o uso de strings de múltiplas linhas em Python com aplicações reais.

Autor: Ronaldo Rhoney (exemplo)
"""

# ==============================
# 1. String de múltiplas linhas com aspas triplas
# ==============================
# Podemos usar três aspas duplas (""" """) ou simples (''' ''')

mensagem = """Olá, cliente!

Seu pedido foi aprovado com sucesso.
Em breve você receberá mais informações.

Atenciosamente,
Equipe de Suporte
"""

print("\n--- Mensagem automática ---")
print(mensagem)

# ==============================
# 2. Aplicação real: Template de e-mail
# ==============================
# Muito comum em sistemas automatizados

nome = "Ronaldo"
produto = "Notebook"
preco = 3500.00

email = f"""
Olá, {nome}!

Obrigado pela sua compra 🎉

Produto: {produto}
Valor: R$ {preco:.2f}

Seu pedido já está sendo processado e será enviado em breve.

Atenciosamente,
Equipe de Vendas
"""

print("\n--- E-mail gerado ---")
print(email)

# ==============================
# 3. Aplicação real: SQL (muito usado em dados)
# ==============================
# Ideal para escrever queries grandes de forma legível

query = """
SELECT nome, idade, cidade
FROM clientes
WHERE idade > 18
ORDER BY nome ASC;
"""

print("\n--- Query SQL ---")
print(query)

# ==============================
# 4. Aplicação real: HTML (web)
# ==============================
# Muito usado em projetos web ou automações

html = """
<html>
    <head>
        <title>Página de Teste</title>
    </head>
    <body>
        <h1>Bem-vindo ao sistema</h1>
        <p>Este conteúdo foi gerado com Python.</p>
    </body>
</html>
"""

print("\n--- HTML gerado ---")
print(html)

# ==============================
# 5. Removendo indentação indesejada
# ==============================
# Às vezes a indentação do código afeta o texto final

import textwrap

texto_indentado = """
        Este texto possui
        espaços desnecessários
        no início das linhas.
"""

# textwrap.dedent remove essa indentação
texto_limpo = textwrap.dedent(texto_indentado)

print("\n--- Texto corrigido ---")
print(texto_limpo)

# ==============================
# 6. Aplicação real: Logs de sistema
# ==============================
# Muito útil para registrar eventos

usuario = "admin"
acao = "login realizado"

log = f"""
[LOG DO SISTEMA]
Usuário: {usuario}
Ação: {acao}
Status: SUCESSO
"""

print("\n--- Log gerado ---")
print(log)

# ==============================
# Conclusão
# ==============================
"""
Strings de múltiplas linhas são úteis para:

✔ E-mails automáticos
✔ Queries SQL
✔ HTML / templates web
✔ Logs de sistema
✔ Documentação interna

Dica:
Use f-strings com múltiplas linhas para deixar o código mais dinâmico e profissional 🚀
"""