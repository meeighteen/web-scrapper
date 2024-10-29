import requests
import csv
from bs4 import BeautifulSoup

urlToScrap = 'https://angular.dev/overview'

# Realiza una solicitud GET a la página
response = requests.get(urlToScrap)

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    # Analiza el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encuentra el contenido a extraer
    # (Ejemplo: todos los encabezados h2)
    headers = soup.find_all('h2')

    with open('headers.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Header'])  # Escribe el encabezado

        for header in headers:
            writer.writerow([header.get_text()])  # Escribe cada encabezado en una nueva fila

else:
    print(f'Error al acceder a la página: {response.status_code}')
