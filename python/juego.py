import random
import numpy as np 
import math

def create_table():
	tablero = [[],[],[]]
	for i in range(0,3):
		for j in range(len(tablero)):
			tablero[j].append('*')
	tablero = np.array(tablero)	
	return tablero

#TODO: este proceso debe ser iterativo


#TODO: CREAR UN ARREGLO DE MOVIMIENTOS GANADORES
#TODO: BUSCAR LA FORMA DE LOS MOVIMIENTOS INGRESADOS INGRESARLOS A UN CSV



#TODO: en esta funcion se deben registrar las jugadas ganaroas,
def validate_win():
	pass



def distance(player_move,available_moves):
	


	#TODO: se debe crear un diccionario con el nombre del movimiento y su 
	# valor 
	
	resultados = {}

	x1,y1 = player_move

	for k,v in available_moves.items():
		x2,y2 = v
		resultado = math.sqrt(((x2-x1)+(y2-y1))**2)
		resultados[k] = resultado
		
	#resultado = math.sqrt(((x2-x1)+ (y2-y1))**2)
	return resultados
	
def all_moves():
	dic_pos = {
		'A1' : [0,0],
		'A2' : [1,0],
		'A3' : [2,0],
		'B1' : [0,1],
		'B2' : [1,1],
		'B3' : [2,1],
		'C1' : [0,2],
		'C2' : [1,2],
		'C3' : [2,2]
	}	
	return dic_pos

def insert_both_pos():
	table = create_table()

	positions = all_moves()	
 
	#player_input = input('ingrese posicion >')

	#esto ayuda a mostrar las posiciones en cordenadas
	aux = 0
	for i in positions.keys():
		aux+=1
		print(i,end=',')
		if aux % 3 == 0:
			print('\n') 
		
	#solicitar el ingreso de la pos al usuario
	input_player = input('Ingrese la posicion disponible >> ')
	
	player_move = []
	

	#ingresar pos usuario
	for k,v in positions.items():
		if k.lower() == input_player:
			a,b = v
			table[a][b] = 'X'
			
			player_move.append(v)
	

	#validar movimientos disponibles
	disponibles = {}
	
	#print(positions.items())


	for k,v in positions.items():
	#	print(v)
		if player_move[0] != v:
			disponibles[k] = v

	
	cercanos = distance(player_move[0],disponibles)
	#print(cercanos)	
	

#   se guardo las claves de los cercanos
	posibles = [k for k,v in cercanos.items() if v < 2 ]
	k_insert = random.choice(posibles)
	print(k_insert)	
	
	for k,v in positions.items():
		ap,bp = v
		if k == k_insert:
			table[ap][bp] = 'O'
	
	print(table)
	
	#aca se insertara una posicion del juego a partir de la distancias calculadas 
	
		
def run_game():
	print('estamos jugando...')

if __name__ == '__main__':
	#run_game()
	print(create_table())
    
		
	#player_move,disponibles = insert_both_pos()
	
	insert_both_pos()	
	 
	#insert_both_pos()
	#print(all_moves())
