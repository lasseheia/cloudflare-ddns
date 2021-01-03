from dotenv import load_dotenv, find_dotenv
import os
import requests
import CloudFlare

def main():
    # Load environment variables from .env file
    load_dotenv(find_dotenv())
    
    # Get current IP address
    try:
        r = requests.get('https://api.ipify.org')
        ip = r.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Connect to Cloudflare
    cf = CloudFlare.CloudFlare(email=os.getenv('email'), token=os.getenv('token'), debug=True)

    # Get zone
    try:
        zone = cf.zones.dns_records.get(os.getenv('zone_id'))
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit(e)
    
    # Update A records with new IP
    for record in zone:
        if record['type'] == 'A':
            if record['content'] != ip:
                try:
                    cf.zones.dns_records.put(zone[0]['id'], record['zone_id'], data={'content': ip})
                except CloudFlare.exceptions.CloudFlareAPIError as e:
                    exit(e)

if __name__ == '__main__':
    main() 
