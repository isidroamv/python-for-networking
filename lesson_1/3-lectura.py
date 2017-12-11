import os

n1 = raw_input("Escribe n2:")
n2 = raw_input("Escribe n2:")
print("total", int(n1) + int(n2))

# ping
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)
print(response==0)