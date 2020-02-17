import grpc
from concurrent import futures
import time

# import the generated classes :
import ML_example_pb2
import ML_example_pb2_grpc

# import the function we made :
import predict_sale_price as psp


# create a class to define the server functions, derived from
# usingSKlearn_pb2_grpc.PredictServicer :
class PredictServicer(ML_example_pb2_grpc.PredictServicer):
    def predict_sale_price(self, request, context):
        # define the buffer of the response :
        response = ML_example_pb2.Prediction()
        # get the value of the response by calling the desired function :
        response.salePrice = psp.predict_sale_price(request.MSSubClass,request.LotArea, request.YearBuilt, request.BedroomAbvGr, request.TotRmsAbvGrd)
        return response


# creat a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))

ML_example_pb2_grpc.add_PredictServicer_to_server(PredictServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
