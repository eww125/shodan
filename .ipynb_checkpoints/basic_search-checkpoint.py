import shodan

# Configuration
import os
f = open(os.path.expanduser('~') + '/api_keys/shodan_api', 'r')
API_KEY = f.readline().splitlines()[0]
print(API_KEY)

api = shodan.Shodan(API_KEY)

# Search Shodan
results = api.search('apache')

# Show the results
print('Results found: %s' % results['total'])
x = 1
for result in results['matches']:
    print("x=" + str(x))
    print('IP: %s' % result['ip_str'])
    print(result['data'])
    print('')
    x += 1
    if x == 5:
        break