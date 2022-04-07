import nacl.utils

a=nacl.utils.random(128)
print(len(a))
x=''
for i in range(len(a)):
    x+="%02x " % (a[i])
print()
print(x)