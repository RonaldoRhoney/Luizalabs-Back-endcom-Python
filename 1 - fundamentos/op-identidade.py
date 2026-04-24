# Verifica se um determinado valor ocupa um espaço de memória específico
saldo = 1000
limite = 500

print(saldo is limite)  # False, pois são objetos diferentes    
print(saldo is not limite)  # True, pois são objetos diferentes
