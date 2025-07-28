import argparse
import json
import requests
import socket
import sys
from datetime import datetime
from urllib.parse import urlparse

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_ip_info(ip_address):
    try:
        if ip_address.startswith(('http://', 'https://')):
            domain = urlparse(ip_address).netloc
            try:
                ip_address = socket.gethostbyname(domain)
            except socket.gaierror:
                return None, f"No se pudo resolver la dirección: {domain}"
        
        response = requests.get(f"http://ip-api.com/json/{ip_address}?fields=66846719")
        if response.status_code != 200:
            return None, "Error al consultar la API de geolocalización"
        
        data = response.json()
        
        if data.get('status') == 'fail':
            return None, data.get('message', 'Error desconocido al consultar la IP')
    
        more_info = {}
        try:
            resp = requests.get(f"https://ipinfo.io/{ip_address}/json")
            if resp.status_code == 200:
                more_info = resp.json()
        except:
            pass
        
        combined_data = {**data, **more_info}
        return combined_data, None
    
    except Exception as e:
        return None, f"Error al procesar la solicitud: {str(e)}"

def format_output(data, args):
    output = []
    
    output.append(f"{Colors.HEADER}{Colors.BOLD}DATOS DE LA IP: {data.get('query', 'Desconocido')}{Colors.ENDC}")
    output.append("-" * 50)
    
    if 'country' in data:
        output.append(f"{Colors.OKBLUE}{Colors.BOLD}📍 Ubicación:{Colors.ENDC}")
        output.append(f"  País: {data.get('country', 'Desconocido')} ({data.get('countryCode', '?')})")
        output.append(f"  Región: {data.get('regionName', 'Desconocido')} ({data.get('region', '?')})")
        output.append(f"  Ciudad: {data.get('city', 'Desconocido')}")
        output.append(f"  Código Postal: {data.get('zip', 'Desconocido')}")
        output.append(f"  Distrito: {data.get('district', 'Desconocido')}")
    
    if 'lat' in data and 'lon' in data:
        output.append(f"  Coordenadas: {data.get('lat', '?')}, {data.get('lon', '?')}")
        if args.map:
            output.append(f"  {Colors.OKGREEN}Mapa: https://www.google.com/maps?q={data.get('lat', '')},{data.get('lon', '')}{Colors.ENDC}")
    
    if args.network or args.all:
        output.append(f"\n{Colors.OKCYAN}{Colors.BOLD}🌐 Información de Red:{Colors.ENDC}")
        output.append(f"  IP: {data.get('query', 'Desconocido')}")
        output.append(f"  ISP: {data.get('isp', 'Desconocido')}")
        output.append(f"  Organización: {data.get('org', 'Desconocido')}")
        output.append(f"  ASN: {data.get('as', 'Desconocido')}")
        output.append(f"  Dominio: {data.get('asname', 'Desconocido')}")
        output.append(f"  Tipo: {data.get('type', 'Desconocido')}")

    if args.location or args.all:
        output.append(f"\n{Colors.OKGREEN}{Colors.BOLD}🗺️ Información Geográfica Extendida:{Colors.ENDC}")
        output.append(f"  Zona Horaria: {data.get('timezone', 'Desconocido')}")
        if 'timezone' in data:
            local_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
            output.append(f"  Hora Local: {local_time}")
        output.append(f"  Código Continente: {data.get('continentCode', 'Desconocido')}")
        output.append(f"  Continente: {data.get('continent', 'Desconocido')}")
        output.append(f"  Moneda: {data.get('currency', 'Desconocido')}")
    
    if args.tech or args.all:
        output.append(f"\n{Colors.WARNING}{Colors.BOLD}🔧 Información Técnica:{Colors.ENDC}")
        output.append(f"  Proxy: {'Sí' if data.get('proxy', False) else 'No'}")
        output.append(f"  VPN: {'Sí' if data.get('vpn', False) else 'No'}")
        output.append(f"  TOR: {'Sí' if data.get('tor', False) else 'No'}")
        output.append(f"  Hosting: {'Sí' if data.get('hosting', False) else 'No'}")
        output.append(f"  Reverse DNS: {data.get('reverse', 'Desconocido')}")
    
    if args.extra or args.all:
        output.append(f"\n{Colors.FAIL}{Colors.BOLD}📊 Datos Adicionales:{Colors.ENDC}")
        output.append(f"  Código Móvil: {data.get('mobile', 'No')}")
        output.append(f"  Código EU: {'Sí' if data.get('eu', False) else 'No'}")
        if 'hostname' in data:
            output.append(f"  Hostname: {data.get('hostname', 'Desconocido')}")
    
    
    output.append(f"\n{Colors.HEADER}Herramienta creada por M-Society{Colors.ENDC}")
    output.append(f"{Colors.OKBLUE}GitHub: {Colors.UNDERLINE}github.com/M-Societyy{Colors.ENDC}")
    output.append(f"{Colors.OKGREEN}Discord: {Colors.UNDERLINE}https://discord.gg/9QRngbrMKS{Colors.ENDC}")
    output.append(f"{Colors.WARNING}Web: {Colors.UNDERLINE}guns.lol/msociety{Colors.ENDC}")
    
    return '\n'.join(output)

def main():
    parser = argparse.ArgumentParser(description='Herramienta avanzada de geolocalización de IPs')
    parser.add_argument('ip', help='Dirección IP o dominio a investigar')
    parser.add_argument('-a', '--all', action='store_true', help='Mostrar toda la información disponible')
    parser.add_argument('-n', '--network', action='store_true', help='Mostrar información de red')
    parser.add_argument('-l', '--location', action='store_true', help='Mostrar información geográfica extendida')
    parser.add_argument('-t', '--tech', action='store_true', help='Mostrar información técnica')
    parser.add_argument('-e', '--extra', action='store_true', help='Mostrar datos adicionales')
    parser.add_argument('-m', '--map', action='store_true', help='Mostrar enlace a Google Maps')
    parser.add_argument('-j', '--json', action='store_true', help='Mostrar salida en formato JSON')
    
    args = parser.parse_args()
    
    data, error = get_ip_info(args.ip)
    if error:
        print(f"{Colors.FAIL}Error: {error}{Colors.ENDC}")
        sys.exit(1)
    
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(format_output(data, args))

if __name__ == "__main__":
    main()
