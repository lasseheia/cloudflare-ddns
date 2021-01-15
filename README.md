# Cloudflare DDNS
## Prerequisites
### API key/token
https://dash.cloudflare.com/profile/api-tokens
### Credentials as environment variables
* Create a file called `.env` and add the following contents:
```
# Only set this if using key
export CF_API_EMAIL=''
# Token or key
export CF_API_KEY=''
```
### Zone
Set CF_ZONE_ID in the crontab to the Zone you want to update.
## Example crontab
```
#         Cloudflare auth                       Zone to update        Script for updating records
0 0 * * * source /scripts/cloudflare-ddns/.env; export CF_ZONE_ID=''; /scripts/cloudflare-ddns/env/bin/python /scripts/cloudflare-ddns/ddns.py
```
