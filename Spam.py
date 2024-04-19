#Dubby66


import requests
import json
import time

# URL del webhook 
webhook_url = 'Metti il webhook qui a cui vuoi spammare '

# Inserisci il testo dopo content:
payload = {
    'content': 'Inserisci il testo qui da spammare' #OCCHIO AL LIMETE DI di caratteri da inserire
}

# Numero di invio
numero_invii = 50

# Ritardo minimo tra ogni invio (in secondi)
ritardo_minimo = 0.01

# Loop 
for _ in range(numero_invii):
    # Invio della richiesta POST al webhook
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    
    # Verifica dello stato della richiesta
    if response.status_code == 200:
        print("Messaggio inviato con successo!")# risposta nella console 
    elif response.status_code == 429:
        retry_after = response.json()['retry_after']
        print(f"Rate limit raggiunto. Ritardo di {retry_after} secondi.")
        time.sleep(retry_after + ritardo_minimo)
    else:
        print(f"Messaggio inviato con successo!")
        print(response.text)
    
    
    time.sleep(ritardo_minimo)
