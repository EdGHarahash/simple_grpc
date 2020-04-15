import grpc
import computer_pb2
import computer_pb2_grpc


def generate_nums(n):
    for i in range(n):
        yield computer_pb2.Number(value = i)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = computer_pb2_grpc.ComputerStub(channel)

        print("-------------- squareRoot --------------")
        print(stub.SquareRoot(computer_pb2.Number(value=4)).value)

        print("-------------- Primes --------------")
        a = stub.Primes(computer_pb2.Number(value=40))
        for aa in a:
            print(aa.value)
        
        print("-------------- STD --------------")
        print(stub.STD(generate_nums(10)).value)

        print("-------------- maxElem --------------")
        for a in stub.MaxElem(generate_nums(10)):
            print(a.value)

        print("-------------- maxElem --------------")
        aaaa = list(map(lambda x: computer_pb2.Number(value=x), [4,2,1,5,3,10,2,120,22,-1,32,900,2,2,2]))
        for a in stub.MaxElem(iter(aaaa)):
            print(a.value)


if __name__ == '__main__':
    run()