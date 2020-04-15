from concurrent import futures
import math
import grpc
import numpy as np
import computer_pb2 as cp
import computer_pb2_grpc as cgpg


class ComputerServicer(cgpg.ComputerServicer):

    def SquareRoot(self, request, context):
        return cp.Number(value=math.sqrt(request.value))
    
    def Primes(self, request, contex):
        d = 2
        n = request.value
        while d*d <= n:
            while (n % d) == 0:
                yield cp.Number(value=d)
                n //= d
            d+=1
        if n > 1:
            yield cp.Number(value=n)
    
    def STD(self, request_iterator, context):
        arr = []
        for n in request_iterator:
            arr.append(n.value)
        return cp.Number(value=np.std(np.array(arr), ddof=1))

    def MaxElem(self, request_iterator, context):
        max_num = None
        for num in request_iterator:
            if not max_num:
                max_num = num
            elif num.value > max_num.value:
                max_num = num
            yield max_num   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cgpg.add_ComputerServicer_to_server(
        ComputerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()