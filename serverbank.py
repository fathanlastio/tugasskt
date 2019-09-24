import zerorpc

class Bank(object):
    def client(self, topup, saldo):
        jumlah = saldo - topup
        return "Saldo Rekening: %d" % saldo, "Menjadi: %d" % jumlah

    def market(self, topup, saldo):
        jumlah = saldo + topup
        return "Saldo Marketplace: %d" % saldo, "Menjadi: %d" % jumlah
        
server = zerorpc.Server(Bank())
server.bind("tcp://0.0.0.0:4444")
server.run()