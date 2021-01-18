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
# ID of Zone
export CF_ZONE=''
# Name of records
export CF_RECORDS='domain.com, sub.domain.com, extra.sub.domain.com'
```
## Example crontab
```
#         Cloudflare auth                    Script for updating records
0 * * * * source /path/cloudflare-ddns/.env; /path/cloudflare-ddns/env/bin/python /path/cloudflare-ddns/ddns.py &> /dev/null
```
## Multiple zones
* Add another crontab entry with another `.env` file
## Troubleshooting
* API error
  * Use API key instead of token
