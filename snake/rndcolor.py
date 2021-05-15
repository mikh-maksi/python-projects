import random
def randomcolor():
    r = "%02x"%random.randint(0,255)
    g = "%02x"%random.randint(0,255)
    b = "%02x"%random.randint(0,255)
    res = "#"+str(r)+str(g)+str(b)
    return res

print(randomcolor())

