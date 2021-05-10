from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '3af4c7ffa3a8535c31b827643a9ca2a63cab8291'
meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()

for org in orgs:
    if org['name'] == 'Cleveland Metropolitan School District':
      orgId = org['id']

params = {}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params)


pprint(orgs)
pprint(networks)
