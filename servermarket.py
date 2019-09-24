import zerorpc

class Market(object):
    def topup(self, saldo, saldo_awal):
        jumlah = saldo + saldo_awal
        return "Saldo: %d" % saldo_awal, "Menjadi: %d" % jumlah

server = zerorpc.Server(Market())
server.bind("tcp://0.0.0.0:8888")
server.run()