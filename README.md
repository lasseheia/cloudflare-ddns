# Cloudflare DDNS
## Prerequisites
### Read this before deciding between key or token
https://github.com/cloudflare/python-cloudflare#providing-cloudflare-username-and-api-key
### Credentials as environment variables
* .env must contain:
```
export CF_API_EMAIL=''
export CF_API_KEY=''
```
### Zone
Set CF_ZONE_ID in the crontab to the Zone you want to update.
## Example crontab
```
#         Cloudflare auth                       Zone to update        Script for updating records
0 0 * * * source /scripts/cloudflare-ddns/.env; export CF_ZONE_ID=''; /scripts/cloudflare-ddns/env/bin/python /scripts/cloudflare-ddns/ddns.py
```
