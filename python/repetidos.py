
texto = "aslkdalsdjkashdkjahsdkjahsdkja"
texto = list(texto)

repeticiones = {}

for _ in texto:
	if ' ' != _:
		repeticiones[_] = texto.count(_)

print(repeticiones)	
 



