import socket
import datetime

def main():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	server_socket.bind(('0.0.0.0', 1303))
	
	server_socket.listen(5)
	print("Сервер запущен и ожидает подключений...")

	try:
	 while True:
                client_socket, client_address = server_socket.accept()
                print("Подключение от:", client_address)

                current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

                client_socket.send(current_time.encode())
                client_socket
	except KeyboardInterrupt:
		print("Сервер остановлен.")
		server_socket.close()

if __name__ == "__main__":
	main()
