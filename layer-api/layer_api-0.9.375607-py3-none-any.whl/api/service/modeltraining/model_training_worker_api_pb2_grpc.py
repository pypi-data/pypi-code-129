# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layerapi.api.service.modeltraining import model_training_worker_api_pb2 as api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2


class ModelTrainingWorkerAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartExecution = channel.unary_unary(
                '/api.ModelTrainingWorkerAPI/StartExecution',
                request_serializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartExecutionRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartExecutionResponse.FromString,
                )
        self.StartHyperparameterTuningExecution = channel.unary_unary(
                '/api.ModelTrainingWorkerAPI/StartHyperparameterTuningExecution',
                request_serializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartHyperparameterTuningExecutionRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartHyperparameterTuningExecutionResponse.FromString,
                )


class ModelTrainingWorkerAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartHyperparameterTuningExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelTrainingWorkerAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartExecution': grpc.unary_unary_rpc_method_handler(
                    servicer.StartExecution,
                    request_deserializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartExecutionRequest.FromString,
                    response_serializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartExecutionResponse.SerializeToString,
            ),
            'StartHyperparameterTuningExecution': grpc.unary_unary_rpc_method_handler(
                    servicer.StartHyperparameterTuningExecution,
                    request_deserializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartHyperparameterTuningExecutionRequest.FromString,
                    response_serializer=api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartHyperparameterTuningExecutionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.ModelTrainingWorkerAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelTrainingWorkerAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.ModelTrainingWorkerAPI/StartExecution',
            api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartExecutionRequest.SerializeToString,
            api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartHyperparameterTuningExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.ModelTrainingWorkerAPI/StartHyperparameterTuningExecution',
            api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartHyperparameterTuningExecutionRequest.SerializeToString,
            api_dot_service_dot_modeltraining_dot_model__training__worker__api__pb2.StartHyperparameterTuningExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
