import zerorpc

market = zerorpc.Client()
bank = zerorpc.Client()

market.connect("tcp://127.0.0.1:8888")
bank.connect("tcp://127.0.0.1:4444")

saldo = 0
saldomarket = 50000
saldoclient = 5000

x = input("Masukkan Nominal: ")
masuk = int(x)

data = market.topup(masuk,saldo)
print (data)

data = bank.client(masuk,saldoclient)
print (data)

data = bank.market(masuk,saldomarket)
print (data)