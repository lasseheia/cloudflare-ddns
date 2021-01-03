# Cloudflare DDNS
## Prerequesites
* .env with: 
** 
```
export CF_API_EMAIL='ex@mple.org'
export CF_API_KEY='asdf2dsfg34gsdfg43'
```
## Example crontab
```
#         Cloudflare auth                	Zone to update                                        Script for updating records
0 0 * * * source /scripts/cloudflare-ddns/.env; export CF_ZONE_ID='1233454565675682343'; /scripts/cloudflare-ddns/env/bin/python /scripts/cloudflare-ddns/ddns.py
```
