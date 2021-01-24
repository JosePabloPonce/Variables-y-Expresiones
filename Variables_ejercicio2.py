#Sebastian Garcia, 19683
#Jose Pablo Ponce, 19092
#7/2/2019
#Variables_ejercicio2
#Programa para completar historia 

print('Ingrese datos: ')
np = input('Ingrese nombre: ')
np1 = input('Ingrese pronombre: ')
np2 = input('Ingrese primer digito de la edad: ')
npa = input('Ingrese segundo digito de la edad: ')
np3 = input('Ingrese nombre de familiar o amigo del protagonista: ')
np4 = input('Ingrese relación: ')
np5 = input('Ingrese animal: ')
np6 = input('Ingrese color: ')
np7 = input('Ingrese un material: ')
np8 = input('Ingrese otro color: ')
print()
npp = np2 + npa

np2 = float(np2)
npa = float(npa)
npp = float(npp)

np9 = np2 + npa
np10 = npp / 2
np11 = np9 / 100 * 60
np12 = np10 / 100 * 60
np13 = np9 - np11
np14 = np10 - np12

print('En un día soleado de febrero,', np, 'decidió visitar a su', np4, ',', np3, '.', np1, 'le llevaba', "{: .0f}".format(np9), 'galletas y', "{: .0f}".format(np10), 'dulces.')
print(np, 'no recordaba muy bien el camino y luego de cierto tiempo se perdió. Inesperadamente', np1, 'vio un', np5, 'con un chaleco')
print(np6, 'caminando muy apresuradamente.')
print(np, 'decidió seguir al', np5, 'por un bosque que se encontraba en el lugar. Al cabo de poco tiempo llegó a un claro donde se')
print('encontraba una casa hecha de', np7, ', donde el', np5, 'entró.')
print(np, 'entró también a la casa, pero al estar adentro notó que se había teletransportado a un lugar diferente, parecía ser otro')
print('mundo, u otra dimensión.')
print('¡Debo volver a casa! dijo', np, 'y empezó a preocuparse. En ese momento apareció el', np5, 'y le dijo: Yo puedo ayudarte a volver')
print('a casa, te indicaré por qué puerta debes volver pero deberás pagarme', "{: .0f}".format(npp), 'monedas de oro.')
print('¡No tengo monedas! dijo', np, ', lo único que tengo son', "{: .0f}".format(np9), 'galletas y', "{: .0f}".format(np10), 'dulces. Ok entonces tomaré el 60% de tus')
print('pertenencias dijo el', np5, '.', np, 'entonces le dio al', np5, "{: .0f}".format(np11), 'galletas y', "{: .0f}".format(np12), 'dulces.')
print('Regresa por la puerta de color', np8, ',dijo el', np5, '.', np, 'fue corriendo hacia la puerta indicada y al salir por ella se encontró')
print('frente a la casa de su', np4, ', a quien pudo llevarle únicamente', "{: .0f}".format(np13), 'galletas y', "{: .0f}".format(np14), 'dulces.')
print('Fin')


