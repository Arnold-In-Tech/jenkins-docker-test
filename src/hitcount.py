import redis
# connect to redis server
r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)

# increase the hit count for the usr
def hit(usr):
    r.incr(usr)
# get the hit count for the usr
def getHit(usr):
    return (r.get(usr))
    
# In the first line of this program, we are importing the redis driver, which is the connectivity driver of the redis database. 
# In the following line, we are connecting to the redis database, and then we continue to implement the hit and getHit function.
