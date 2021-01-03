from dotenv import load_dotenv, find_dotenv
import os
import CloudFlare

def main():
    load_dotenv(find_dotenv())
    
    cf = CloudFlare.CloudFlare(email=os.getenv('email'), token=os.getenv('token'))
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print(zone_id, zone_name)
if __name__ == '__main__':
    main() 
