import socket
import asyncio

host, port = ('localhost',5569) 
host2, port2 = ('localhost', 5561)
socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

async def start_serveur():
	#adresse ip
	socket.bind((host, port))
	print("le serveur est demarer....")

	while True:
		socket.listen(5)#nombre de test avant echec de connexion
		conn, address = socket.accept()#conn c'est le host et adress le port
		print("En ecoute ......")

		data = conn.recv(1024)
		data = data.decode('utf8')
		print(data)


async def get_message():
	try:
		socket.connect((host2, port2))
		print("client connecter")

		data='bonjour je suis le client'
		data = data.encode('utf8')
		socket.sendall(data)

	except :
		print("connexion au server echouer")
	finally:
		socket.close()

asyncio.run(start_serveur())
asyncio.run(get_message())
