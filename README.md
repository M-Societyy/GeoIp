# 📡 Geolocalizador de IPs Avanzado - M-Society Tool

**Herramienta profesional para el análisis completo de direcciones IP y dominios**

## 🔍 Descripción

Este script en Python proporciona información detallada sobre cualquier dirección IP o dominio, incluyendo:
- Ubicación geográfica precisa (país, ciudad, coordenadas)
- Datos del proveedor de servicios (ISP, organización)
- Información técnica (proxy, VPN, hosting)
- Características especiales (si es móvil, pertenece a la UE)
- Y mucho más...

## 🚀 Características Principales

- ✅ **Sin API keys requeridas** - Funciona inmediatamente
- ✅ **Consulta múltiples fuentes** para máxima información
- ✅ **Soporte para dominios** - Resuelve automáticamente a IP
- ✅ **Interfaz con colores** para mejor legibilidad
- ✅ **Opciones personalizables** para filtrar información

## ⚙️ Instalación

1. **Requisitos previos**:
   - Python 3.6 o superior
   - Módulos requeridos: `requests`, `argparse`

2. **Instalar dependencias**:
   ```bash
   pip install requests argparse
   ```

3. **Descargar el script**:
   ```bash
   git clone https://github.com/M-Societyy/GeoIp.git
   cd GeoIp
   ```

## 🖥️ Uso Básico

```bash
python3 geoip.py [IP o DOMINIO] [OPCIONES]
```

### Ejemplos:

1. **Información básica de una IP**:
   ```bash
   python3 geoip.py 8.8.8.8
   ```

2. **Información completa (todas las opciones)**:
   ```bash
   python3 geoip.py google.com -a
   ```

3. **Solo información técnica y de red**:
   ```bash
   python3 geoip.py 192.168.1.1 -n -t
   ```

4. **Mostrar en formato JSON**:
   ```bash
   python3 geoip.py facebook.com -j
   ```

## 🛠️ Opciones Disponibles

| Opción       | Descripción                                      |
|--------------|--------------------------------------------------|
| `-a, --all`  | Muestra TODA la información disponible          |
| `-n, --network` | Información de red (ISP, ASN, organización)    |
| `-l, --location` | Datos geográficos extendidos                   |
| `-t, --tech` | Información técnica (proxy, VPN, hosting)      |
| `-e, --extra` | Datos adicionales (móvil, UE, hostname)       |
| `-m, --map`  | Muestra enlace a Google Maps con las coordenadas|
| `-j, --json` | Salida en formato JSON para procesamiento      |

## 📊 Campos de Información Disponibles

### 🌍 Ubicación Geográfica
- País, región, ciudad
- Código postal, distrito
- Coordenadas GPS (latitud/longitud)
- Zona horaria, hora local
- Continente, código de continente
- Moneda local

### 🌐 Información de Red
- Dirección IP consultada
- Proveedor de servicios (ISP)
- Organización registrada
- Número AS y nombre de dominio AS
- Tipo de conexión

### 🔧 Datos Técnicos
- Uso de proxy (Sí/No)
- Conexión VPN (Sí/No)
- Nodo TOR (Sí/No)
- Servidor de hosting (Sí/No)
- DNS inverso (reverse DNS)

### 📌 Información Adicional
- Código móvil (celular)
- Pertenencia a la Unión Europea
- Nombre de host (hostname)
- Fecha y hora local

## � Ejemplo de Salida

```
DATOS DE LA IP: 8.8.8.8
--------------------------------------------------
📍 Ubicación:
  País: United States (US)
  Región: California (CA)
  Ciudad: Mountain View
  Código Postal: 94043
  Distrito: Desconocido
  Coordenadas: 37.4056, -122.0775
  Mapa: https://www.google.com/maps?q=37.4056,-122.0775

🌐 Información de Red:
  IP: 8.8.8.8
  ISP: Google LLC
  Organización: Google Public DNS
  ASN: AS15169 Google LLC
  Dominio: GOOGLE
  Tipo: business

🗺️ Información Geográfica Extendida:
  Zona Horaria: America/Los_Angeles
  Hora Local: 2023-05-15 14:30:22
  Código Continente: NA
  Continente: North America
  Moneda: USD

🔧 Información Técnica:
  Proxy: No
  VPN: No
  TOR: No
  Hosting: Sí
  Reverse DNS: dns.google

📊 Datos Adicionales:
  Código Móvil: No
  Código EU: No
  Hostname: dns.google

Herramienta creada por M-Society
GitHub: github.com/M-Societyy
Discord: https://discord.gg/9QRngbrMKS
Web: guns.lol/msociety
```

## 📌 Notas Importantes

1. **Precisión de datos**: La exactitud de la información geográfica depende de las bases de datos utilizadas por los servicios gratuitos.

2. **Limitaciones**:
   - Algunos campos pueden aparecer como "Desconocido" para ciertas IPs
   - Las IPs privadas (192.168.x.x, 10.x.x.x) no tendrán información geográfica

3. **Uso responsable**: Esta herramienta es solo para fines educativos y de investigación legítima.

## 🤝 Créditos y Contacto

**Desarrollado por M-Society**  
🔗 GitHub: [github.com/M-Societyy](https://github.com/M-Societyy)  
💬 Discord: [https://discord.gg/9QRngbrMKS](https://discord.gg/9QRngbrMKS)  
🌐 Web: [guns.lol/msociety](https://guns.lol/msociety)  

![Demo de GeoIP Tool](geoip.gif)
