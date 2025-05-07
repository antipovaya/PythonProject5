import requests


def check_ip_on_virustotal(ip_address, api_key):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_address}'

    headers = {
        'x-apikey': api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()

        if response.status_code == 200:
            data = response_json['data']

            if 'attributes' in data:
                attributes = data['attributes']
                country = attributes.get('country', 'Unknown')
                last_analysis_results = attributes.get('last_analysis_results')

                print("IP Address:", ip_address)
                print("Country:", country)
                print("Last Analysis Results:")

                for engine, result in last_analysis_results.items():
                    print(f"{engine}: {result['result']}")
            else:
                print("No information available for the IP address.")

        else:
            print("Error occurred while checking the IP address.")

    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", str(e))

        # Замените 'YOUR_API_KEY' на ваш действующий API-ключ от VirusTotal
        api_key = 'YOUR_API_KEY'
        ip_address = '8.8.8.8'  # Замените на IP-адрес, который вы хотите проверить

        check_ip_on_virustotal(ip_address, api_key)