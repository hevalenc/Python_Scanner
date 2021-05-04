import socket

ip = input("Digite o Host ou o IP a ser verificado: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input("Digite a porta a ser verificada: ")))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # conexão TCP/IP
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))
    # code = client.connect_ex(("google.com", 80)) #o número indica a porta de conexão

    if code == 0:
        print(str(port), " -> Porta aberta")
    else:
        print(str(port), " -> Porta fechada")

print("Scan Finalizado")
