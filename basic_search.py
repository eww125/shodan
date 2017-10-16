import shodan

# Configuration
import os
home_dir =  os.path.expanduser('~')
f = open(home_dir + '/api_keys/shodan_api', 'r')
API_KEY = f.readline().splitlines()[0]
print API_KEY

api = shodan.Shodan(API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print 'Results found: %s' % results['total']
        x = 1
        for result in results['matches']:
                print "x=" + str(x)
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
                x = x + 1
                if x == 5:
                        break
except shodan.APIError, e:
        print 'Error: %s' % e
