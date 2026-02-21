import nmap
import json
from colorama import Fore, Style


def escanear_objetivo(ip):
    nm = nmap.PortScanner()
    print(Fore.CYAN + f"Escaneando {ip}..." + Style.RESET_ALL)

    nm.scan(ip, '1-1024')  # rango de puertos comunes

    resultados = {}
    for host in nm.all_hosts():
        resultados[host] = {}
        for proto in nm[host].all_protocols():
            resultados[host][proto] = {}
            puertos = nm[host][proto].keys()
            for puerto in puertos:
                estado = nm[host][proto][puerto]['state']
                resultados[host][proto][puerto] = estado
                print(f"Puerto {puerto}/{proto}: {estado}")

    # Guardar en JSON
    with open("reporte.json", "w") as f:
        json.dump(resultados, f, indent=4)
    print(Fore.GREEN + "Reporte guardado en reporte.json" + Style.RESET_ALL)


if __name__ == "__main__":
    objetivo = input("Introduce la IP o dominio a escanear: ")
    escanear_objetivo(objetivo)

