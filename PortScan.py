import socket
top_ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 162, 389, 443, 445, 1433, 1434, 1521, 2049, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 9000, 10000]
portas_fechadas = []

print("\033[92m _____           _    _____                 \033[0m")
print("\033[92m|  __ \         | |  / ____|                \033[0m")
print("\033[92m| |__) |__  _ __| |_| (___   ___ __ _ _ __  \033[0m")
print("\033[92m|  ___/ _ \| '__| __|\___ \ / __/ _` | '_ \ \033[0m")
print("\033[92m| |  | (_) | |  | |_ ____) | (_| (_| | | | |\033[0m")
print("\033[92m|_|   \___/|_|   \__|_____/ \___\__,_|_| |_|\033[0m")
print("")
print("[>] Scanner de portas simples")
print("[>] Escolha o modo de escaneamento:")
print("    1 - Principais portas (Top Ports)")
print("    2 - Intervalo personalizado de portas")
print("[!] TopPorts = \033[1;33m 20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 162, 389, 443, 445, 1433, 1434, 1521, 2049, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 9000, 10000 \033[0m ")

def inicio():
    escolha = input("[>] Digite a opção (1 ou 2): ")
    if escolha == "1":
        e_topports()
    elif escolha == "2":
        intervalo_i = (int(input("[?] Digite a porta inicial: ")))
        intervalo_f = (int(input("[?] Digite a porta final: ")))
        e_intervalo(intervalo_i, intervalo_f)
    else:
        print("[x] Opção Invalida:")
        inicio()

def e_topports():
    portas_fechadas.clear()
    ip = input((str("[?] Digite o ip desejado: ")))
    print (" \033[1;33m [*] Escaneando ",ip,"... \033[0m")
    def testar_porta(ip,p):
        try:
            s = socket.create_connection((ip, p), timeout=1)
            servico = socket.getservbyport(p, "tcp")
            print(f" \033[1;92m [+] Porta {p} aberta \033[0m","- Serviço rodando:", servico)
            s.close()
        except Exception:
            portas_fechadas.append(p)
        
    def testar_topports(ip, top_ports): 
        total = len(top_ports)
        for i, p in enumerate(top_ports, start=1):
            progresso = (i / total) * 100
            testar_porta(ip,p)
            print(f"\033[1;33m  [*] Progresso: {progresso:.0f}% concluído\033[0m", end="\r")
    testar_topports(ip,top_ports)
    print(" \033[1;91m [!] Portas fechadas: \033[0m \033[K")
    for p in portas_fechadas:
        print(f" \033[1;91m [-] Porta {p} fechada \033[0m")


def e_intervalo(intervalo_i, intervalo_f):
    intervalo = list(range(intervalo_i,intervalo_f+1))
    total = len(intervalo)
    print("[!] Portas Selecionadas = \033[1;33m",intervalo,"\033[0m ")
    portas_fechadas.clear()
    ip = input((str("[?] Digite o ip desejado: ")))
    print (" \033[1;33m [*] Escaneando ",ip,"... \033[0m")
    for i, p in enumerate(intervalo, start=1):
        progresso = (i / total) * 100
        try:
            s = socket.create_connection((ip, p), timeout=1)
            try:
                servico = socket.getservbyport(p, "tcp")
            except OSError:
                servico = "desconhecido"
            print(f" \033[1;92m [+] Porta {p} aberta \033[0m","- Serviço rodando:", servico)
            s.close()
        except Exception:
            portas_fechadas.append(p)
        print(f"\033[1;33m  [*] Progresso: {progresso:.0f}% concluído\033[0m", end="\r")
    print(" \033[1;91m [!] Portas fechadas: \033[0m \033[K")
    for p in portas_fechadas:
        print(f" \033[1;91m [-] Porta {p} fechada \033[0m")


inicio()
input("\nPressione ENTER para sair...")
