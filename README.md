# Cloudflare DDNS
## Usage
### Create virtual Python environment and install pip packages
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
### API key/token
https://dash.cloudflare.com/profile/api-tokens
### Credentials as environment variables
* Create a file named `.env` and add the following contents:
```
# Only set this if using key
export CF_API_EMAIL=''
# Token or key
export CF_API_KEY=''
```
## Example crontab
```
#         Cloudflare auth                       Name of record to update  Script for updating records
0 0 * * * source /scripts/cloudflare-ddns/.env; export CF_RECORD_NAME=''; /scripts/cloudflare-ddns/env/bin/python /scripts/cloudflare-ddns/ddns.py
```
## Troubleshooting
* Try using API key instead of token
