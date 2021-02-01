import redis
import json



# host the ip address where the redis resided
#in my case, it is my virtual box address
r = redis.Redis(host = '192.168.56.1', port = 6379)
print(r)
# r.set('dummy', 'hi')
#to set expiry to a key.....
# r.expire('dummy', 15)
#to set the string type value for a given key
#to set json also
r.set('dummy', json.dumps({1:2, 2:3, 4:5}))
#to set dictionary type value for a key
r.hmset('dummy1', {1:2, 2:3, 4:5})
du = r.get('dummy')
print(du)
du1 = r.hgetall('dummy1')
print(du1)
print(type(du))
print(type(du1))
print(r.keys())
#to check if key is present in redis cache --> 1 - present , 0 - not available
print(r.exists('dummy1'))
print(r.exists('dummy2'))

