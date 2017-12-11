import pyping

r = pyping.ping('google.com')

if r.ret_code == 0:
    print("Success")
else:
    print("Fail")