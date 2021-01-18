import os
import requests
import CloudFlare

def get_ip():
  try:
    r = requests.get('https://api.ipify.org')
    return r.text
  except requests.exceptions.RequestException as e:
    exit('Could not get IP address' % e)
  return None

def get_records(cf, zone_id, record_names):
  try:
    all_records = cf.zones.dns_records.get(zone_id)
    records = []
    for record in all_records:
      if record['name'] in record_names:
        records.append(record)
    return records
  except CloudFlare.exceptions.CloudFlareAPIError as e:
    exit('/zones/dns_records.get %d %s - api call failed' % (e, e)) 

def update_validation(records, record, ip):
  if record['type'] != 'A':
    print(record['name'], "is not an A record")
    return False
  if record['content'] == ip:
    print("No need to update", record['name'])
    return False
  return True

def update_record(cf, record, ip):
  data = {'name': record['name'], 'type': record['type'], 'content': ip, 'proxied': record['proxied']}
  try:
    cf.zones.dns_records.put(record['zone_id'], record['id'], data=data)
    print("Updated A record for", record['name'])
  except CloudFlare.exceptions.CloudFlareAPIError as e:
    exit('/zones/dns_records.put %d %s - api call failed' % (e, e))

def main():
  # Get current IP address
  ip = get_ip()
  # Connect to Cloudflare
  cf = CloudFlare.CloudFlare()

  # Get zones and records
  zone_id = os.environ['CF_ZONE']
  record_names = os.environ['CF_RECORDS'].split(", ")
  
  # Get records
  records = get_records(cf, zone_id, record_names)

  # Update A records with new IP
  for record in records:
    if update_validation(records, record, ip):
      update_record(cf, record, ip)

if __name__ == '__main__':
    main() 
