import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1': '100.24.45.46:5000', # <insert ip address:port of first EC2 instance>, 
		'ip_address2': '18.205.157.193:5000', # <insert ip address:port of second EC2 instance>,
		'load_balancer' : 'mp2-lb-1832289332.us-east-1.elb.amazonaws.com/', # <insert address of load balancer>,
		'submitterEmail': '<insert your account email>', # <insert your coursera account email>,
		'secret': '2yZhS51x5UFpCKCO' # <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)