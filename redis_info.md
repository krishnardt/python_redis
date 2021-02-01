




starting redis: sudo service redis-server start
restarting redis: sudo service redis-server restart

to get the redis cmd --> redis-cli
to authorize it --> auth "password"


to get the redis version --> redis-cli -v   or redis-server -v


where will be the config file: sudo nano /etc/redis/redis.conf


installing command to redis python -- pip install redis


https://stackoverflow.com/questions/19021765/redis-py-whats-the-difference-between-strictredis-and-redis


to check if a key is present in redis
EXISTS keyname
to delete DEL keyname
FLUSHALL to delete entire database/cache

EXPIRE keyname seconds --> seconds is no of seconds for a key to live
TTL keyname gives how much faraway a key to expire
to setup expiry and value ina single line - SETEX keyname duration(seconds) value
to remove expiry PERSIST keyname
