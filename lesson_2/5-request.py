import requests

#https://bitso.com/api_info/v2#ticker

l = requests.get('https://api.bitso.com/v3/ticker?book=eth_mxn')
ether = l.json()


precio = ether['payload']['last']

precio_bajo = ether['payload']['low']
print 'Este es el precio'
print precio
print 'Este es el ultimo precio'
print precio_bajo

if precio >= precio_bajo:
    print("vende ahora")
else:
    print("Espera no vendas aun")
