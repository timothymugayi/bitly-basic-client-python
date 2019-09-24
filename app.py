import json

from bitly_api.api import BitlyBasicAuthClient

client = BitlyBasicAuthClient()

response = client.shorten_url('https://djangosimplified.s3.amazonaws.com/downloads/whitepaper.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2IHOYBOE4RXFBYVT/20190812/ap-southeast-1/s3/aws4_request&X-Amz-Date=20190812T164021Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d4d9bb851123e850fdadd3b9db1482dd901b11bde273724e9d51a45cd0638397', client.groups().get('groups')[0].get('guid'))

shortened_url = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

print(shortened_url)



