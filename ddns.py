from dotenv import load_dotenv, find_dotenv
import os
import requests
import CloudFlare

def main():
    # Load environment variables from .env file
    load_dotenv(find_dotenv())
    
    # Get current IP address
    r = requests.get('https://api.ipify.org?format=json')
    ip = r.json()['ip']

    # Connect to Cloudflare
    cf = CloudFlare.CloudFlare(email=os.getenv('email'), token=os.getenv('token'))
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print(zone_id, zone_name)

if __name__ == '__main__':
    main() 
