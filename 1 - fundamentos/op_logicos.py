print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp01 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp01)    

exp02 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp02)
