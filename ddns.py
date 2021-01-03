import os
import requests
import json
import CloudFlare

def main():
    # Get current IP address
    try:
        r = requests.get('https://api.ipify.org')
        ip = r.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Connect to Cloudflare
    cf = CloudFlare.CloudFlare()

    # Get zone
    zone_id = os.environ['CF_ZONE_ID']
    try:
        records = cf.zones.dns_records.get(zone_id)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.get %d %s - api call failed' % (e, e))
    
    # Update A records with new IP
    for record in records:
        if record['type'] == 'A':
            if record['content'] != ip:
                data = {'name': record['name'], 'type': record['type'], 'content': ip, 'proxied': record['proxied']}
                try:
                    cf.zones.dns_records.put(record['zone_id'], record['id'], data=data)
                except CloudFlare.exceptions.CloudFlareAPIError as e:
                    exit('/zones/dns_records.put %d %s - api call failed' % (e, e))

if __name__ == '__main__':
    main() 
