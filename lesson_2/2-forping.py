import pyping

hosts = [
    "10.3.102.1",
    "www.cisco.com",
    "10.3.102.3",
    "10.3.102.4",
    "google.com",
    "10.3.102.5",
    "10.3.102.6",
    "10.3.102.7",
    "facebook.com",
    "10.3.102.8",
    "10.3.102.9",
    "10.3.102.10",
    "www.microsoft.com",
    "10.3.102.11",
    "10.3.102.20"
]

count_success = 0
for host in hosts:
    r = pyping.ping(host)
    if r.ret_code == 0:
	count_success = count_success + 1
        print(host, "Success")
    else:
        print(host, "Fail")
print count_success
