import os
import requests
import json
import CloudFlare

def get_ip():
  try:
    r = requests.get('https://api.ipify.org')
    return r.text
  except requests.exceptions.RequestException as e:
    raise SystemExit(e)
  return None

def get_zone(cf, zone_name):
  try:
    zones = cf.zones.get()
    for zone in zones:
      if zone['name'] == zone_name:
        return zone
  except CloudFlare.exceptions.CloudFlareAPIError as e:
      exit('/zones/zones.get %d %s - api call failed' % (e, e))
  return None

def get_record(cf, zone, record_name):
  zone_id = zone['id']
  try:
    zone = cf.zones.dns_records.get(zone_id)
    for record in zone:
      if record['name'] == record_name:
        return record
  except CloudFlare.exceptions.CloudFlareAPIError as e:
    exit('/zones/dns_records.get %d %s - api call failed' % (e, e)) 
  return None

def update_record(cf, record, ip):
  if record['type'] == 'A':
    if record['content'] != ip:
      data = {'name': record['name'], 'type': record['type'], 'content': ip, 'proxied': record['proxied']}
      try:
        cf.zones.dns_records.put(record['zone_id'], record['id'], data=data)
        print("Updated A record for", record['name'])
      except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.put %d %s - api call failed' % (e, e))
    else:
      print("No need to update", record['name'])

def main():
  # Get current IP address
  ip = get_ip()
  # Connect to Cloudflare
  cf = CloudFlare.CloudFlare()

  # Get zones
  record_name = os.environ['CF_RECORD_NAME']
  zone_name = record_name.split(".")[-2:]
  zone_name = zone_name[0] + '.' + zone_name[1]
  zone = get_zone(cf, zone_name)
  
  # Get records
  if zone:
    record = get_record(cf, zone, record_name)
  else:
    print("No zones found for", zone_name)
    exit(1)

  # Update A records with new IP
  if record and ip:
    update_record(cf, record, ip)
  else:
    print("No records found for", record_name)
    exit(1)

if __name__ == '__main__':
    main() 
