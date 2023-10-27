import socket

def main():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_ip = input("ВВедите IP-адрес сервера:")
	server_address = (server_ip, 1303)
	client_socket.connect(server_address)

	data = client_socket.recv(1024)
	print("Получено от сервера:", data.decode())

	client_socket.close()

if __name__ == "__main__":
	main()
