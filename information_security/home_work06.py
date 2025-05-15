import nmap

def scan_ports(host, ports):
    # Создаём экземпляр класса PortScanner
    scanner = nmap.PortScanner()
    # Сканируем указанный хост и порты
    scanner.scan(host, ports)
    # Выводим статус отсканированных портов
    for port in scanner[host]['tcp']:
        state = scanner[host]['tcp'][port]['state']
        print(f"Порт {port} — {state}")

if __name__ == '__main__':
    host = input("Введите IP хоста: ")
    ports = input("Введите диапазон портов (например, 1–100): ")
    scan_ports(host, ports)