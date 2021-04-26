import redis
import json, pickle



# host the ip address where the redis resided
#in my case, it is my virtual box address
r = redis.Redis(host = '127.0.0.1', port = 6379)
print(r)

#if database has password support that is securing redis 
r_with_pass = redis.Redis(host = '127.0.0.1', port = 6379, password = 'root')
print(r_with_pass)


# r.set('dummy', 'hi')
#to set expiry to a key.....
# r.expire('dummy', 15)
#to set the string type value for a given key

#to insert a dictionary into normal redis string,
#we have to convert it into json.
r_with_pass.set('dummy', json.dumps({1:2, 2:3, 4:5}))
#to set dictionary type value for a key
r_with_pass.hmset('dummy1', {1:2, 2:3, 4:5})
du = r_with_pass.get('dummy')
#after getting the binary string data.. convert into a dict using json load ..
#for regular usage.
du = json.loads(du.decode('utf-8'))
print(du['1'])
du1 = r_with_pass.hgetall("dummy1")
print(du1)
print(type(du1))
print(du1[b'1'])

print(r_with_pass.hget('dummy1', '1'))
print(r_with_pass.keys())
#to check if key is present in redis cache --> 1 - present , 0 - not available
print(r_with_pass.exists('dummy1'))
print(r_with_pass.exists('dummy2'))

