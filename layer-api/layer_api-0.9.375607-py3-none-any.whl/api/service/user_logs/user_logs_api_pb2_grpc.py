# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layerapi.api.service.user_logs import user_logs_api_pb2 as api_dot_service_dot_user__logs_dot_user__logs__api__pb2


class UserLogsAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPipelineRunLogs = channel.unary_unary(
                '/api.UserLogsAPI/GetPipelineRunLogs',
                request_serializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsResponse.FromString,
                )
        self.GetPipelineRunLogsPerEntity = channel.unary_unary(
                '/api.UserLogsAPI/GetPipelineRunLogsPerEntity',
                request_serializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsPerEntityRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsPerEntityResponse.FromString,
                )
        self.GetPipelineRunLogsStreaming = channel.unary_stream(
                '/api.UserLogsAPI/GetPipelineRunLogsStreaming',
                request_serializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsStreamingRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsStreamingResponse.FromString,
                )


class UserLogsAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPipelineRunLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPipelineRunLogsPerEntity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPipelineRunLogsStreaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserLogsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPipelineRunLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPipelineRunLogs,
                    request_deserializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsRequest.FromString,
                    response_serializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsResponse.SerializeToString,
            ),
            'GetPipelineRunLogsPerEntity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPipelineRunLogsPerEntity,
                    request_deserializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsPerEntityRequest.FromString,
                    response_serializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsPerEntityResponse.SerializeToString,
            ),
            'GetPipelineRunLogsStreaming': grpc.unary_stream_rpc_method_handler(
                    servicer.GetPipelineRunLogsStreaming,
                    request_deserializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsStreamingRequest.FromString,
                    response_serializer=api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsStreamingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.UserLogsAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserLogsAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPipelineRunLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserLogsAPI/GetPipelineRunLogs',
            api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsRequest.SerializeToString,
            api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPipelineRunLogsPerEntity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserLogsAPI/GetPipelineRunLogsPerEntity',
            api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsPerEntityRequest.SerializeToString,
            api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsPerEntityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPipelineRunLogsStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.UserLogsAPI/GetPipelineRunLogsStreaming',
            api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsStreamingRequest.SerializeToString,
            api_dot_service_dot_user__logs_dot_user__logs__api__pb2.GetPipelineRunLogsStreamingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
