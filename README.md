#Dockerized Model GRPC

gRPC Basics – Python
This tutorial provides a basic Python programmer’s introduction to working with gRPC.
By walking through this example you’ll learn how to:
•	Define a service in a .proto file.
•	Generate server and client code using the protocol buffer compiler.
•	Use the Python gRPC API to write a simple client and server for your service.
It assumes that you have read the Overview and are familiar with protocol buffers. You can find out more in the proto3 language guide and Python generated code guide.

Why use gRPC?
This example is a Machine Learning Regression example that lets clients get the sales prediction based on choosen attributes.
With gRPC you can define your service once in a .proto file and implement clients and servers in any of gRPC’s supported languages, which in turn can be run in environments ranging from servers inside Google to your own tablet - all the complexity of communication between different languages and environments is handled for you by gRPC. You also get all the advantages of working with protocol buffers, including efficient serialization, a simple IDL, and easy interface updating.

Steps
1.	Write the service to be served.
2.	Make a proto file to define the messages and services.
3.	Use the proto file to generate gRPC classes for Python
4.	Create the server.
5.	Create the client.
6.	Prepare the docker file and run the docker.

Generate gRPC classes for Python using the below commands:

python3 -m pip install grpcio
python3 -m pip install grpcio-tools googleapis-common-protos
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ML_example.proto

The files generated will be as follows:

ML_example_pb2.py — contains message classes
•	ML_example_pb2.Features for the input features
•	ML_example_pb2.Prediction for the prediction price

ML_example_pb2_grpc.py — contains server and client classes
•	ML_example_pb2_grpc.PredictServicer will be used by the server
•	ML_example_pb2_grpc.PredictStub the client will use it




