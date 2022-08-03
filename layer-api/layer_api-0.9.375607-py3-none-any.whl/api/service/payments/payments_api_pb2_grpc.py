# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layerapi.api.service.payments import payments_api_pb2 as api_dot_service_dot_payments_dot_payments__api__pb2


class PaymentsAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStripeCustomer = channel.unary_unary(
                '/api.PaymentsAPI/CreateStripeCustomer',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeCustomerRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeCustomerResponse.FromString,
                )
        self.CreateStripeSetupIntentId = channel.unary_unary(
                '/api.PaymentsAPI/CreateStripeSetupIntentId',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeSetupIntentIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeSetupIntentIdResponse.FromString,
                )
        self.SaveStripePaymentMethodId = channel.unary_unary(
                '/api.PaymentsAPI/SaveStripePaymentMethodId',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.SaveStripePaymentMethodIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.SaveStripePaymentMethodIdResponse.FromString,
                )
        self.GetStripeBillingInfo = channel.unary_unary(
                '/api.PaymentsAPI/GetStripeBillingInfo',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripeBillingInfoRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripeBillingInfoResponse.FromString,
                )
        self.GetStripePaymentMethodId = channel.unary_unary(
                '/api.PaymentsAPI/GetStripePaymentMethodId',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentMethodIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentMethodIdResponse.FromString,
                )
        self.DeleteStripePaymentMethod = channel.unary_unary(
                '/api.PaymentsAPI/DeleteStripePaymentMethod',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.DeleteStripePaymentMethodRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.DeleteStripePaymentMethodResponse.FromString,
                )
        self.GetStripePaymentsList = channel.unary_unary(
                '/api.PaymentsAPI/GetStripePaymentsList',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentsListRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentsListResponse.FromString,
                )
        self.UpdateStripeBillingInfo = channel.unary_unary(
                '/api.PaymentsAPI/UpdateStripeBillingInfo',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.UpdateStripeBillingInfoRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.UpdateStripeBillingInfoResponse.FromString,
                )
        self.GetLastPaymentInfo = channel.unary_unary(
                '/api.PaymentsAPI/GetLastPaymentInfo',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetLastPaymentInfoRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetLastPaymentInfoResponse.FromString,
                )
        self.ChargeCustomer = channel.unary_unary(
                '/api.PaymentsAPI/ChargeCustomer',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.ChargeCustomerRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.ChargeCustomerResponse.FromString,
                )
        self.CreateCheckoutSessionLink = channel.unary_unary(
                '/api.PaymentsAPI/CreateCheckoutSessionLink',
                request_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateCheckoutSessionLinkRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateCheckoutSessionLinkResponse.FromString,
                )


class PaymentsAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateStripeCustomer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateStripeSetupIntentId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveStripePaymentMethodId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStripeBillingInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStripePaymentMethodId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStripePaymentMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStripePaymentsList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStripeBillingInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastPaymentInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChargeCustomer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCheckoutSessionLink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PaymentsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStripeCustomer': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStripeCustomer,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeCustomerRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeCustomerResponse.SerializeToString,
            ),
            'CreateStripeSetupIntentId': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStripeSetupIntentId,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeSetupIntentIdRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeSetupIntentIdResponse.SerializeToString,
            ),
            'SaveStripePaymentMethodId': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveStripePaymentMethodId,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.SaveStripePaymentMethodIdRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.SaveStripePaymentMethodIdResponse.SerializeToString,
            ),
            'GetStripeBillingInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStripeBillingInfo,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripeBillingInfoRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripeBillingInfoResponse.SerializeToString,
            ),
            'GetStripePaymentMethodId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStripePaymentMethodId,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentMethodIdRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentMethodIdResponse.SerializeToString,
            ),
            'DeleteStripePaymentMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStripePaymentMethod,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.DeleteStripePaymentMethodRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.DeleteStripePaymentMethodResponse.SerializeToString,
            ),
            'GetStripePaymentsList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStripePaymentsList,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentsListRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentsListResponse.SerializeToString,
            ),
            'UpdateStripeBillingInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateStripeBillingInfo,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.UpdateStripeBillingInfoRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.UpdateStripeBillingInfoResponse.SerializeToString,
            ),
            'GetLastPaymentInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastPaymentInfo,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetLastPaymentInfoRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.GetLastPaymentInfoResponse.SerializeToString,
            ),
            'ChargeCustomer': grpc.unary_unary_rpc_method_handler(
                    servicer.ChargeCustomer,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.ChargeCustomerRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.ChargeCustomerResponse.SerializeToString,
            ),
            'CreateCheckoutSessionLink': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCheckoutSessionLink,
                    request_deserializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateCheckoutSessionLinkRequest.FromString,
                    response_serializer=api_dot_service_dot_payments_dot_payments__api__pb2.CreateCheckoutSessionLinkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.PaymentsAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PaymentsAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateStripeCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/CreateStripeCustomer',
            api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeCustomerRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeCustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateStripeSetupIntentId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/CreateStripeSetupIntentId',
            api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeSetupIntentIdRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.CreateStripeSetupIntentIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveStripePaymentMethodId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/SaveStripePaymentMethodId',
            api_dot_service_dot_payments_dot_payments__api__pb2.SaveStripePaymentMethodIdRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.SaveStripePaymentMethodIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStripeBillingInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/GetStripeBillingInfo',
            api_dot_service_dot_payments_dot_payments__api__pb2.GetStripeBillingInfoRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.GetStripeBillingInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStripePaymentMethodId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/GetStripePaymentMethodId',
            api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentMethodIdRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentMethodIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStripePaymentMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/DeleteStripePaymentMethod',
            api_dot_service_dot_payments_dot_payments__api__pb2.DeleteStripePaymentMethodRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.DeleteStripePaymentMethodResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStripePaymentsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/GetStripePaymentsList',
            api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentsListRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.GetStripePaymentsListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStripeBillingInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/UpdateStripeBillingInfo',
            api_dot_service_dot_payments_dot_payments__api__pb2.UpdateStripeBillingInfoRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.UpdateStripeBillingInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastPaymentInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/GetLastPaymentInfo',
            api_dot_service_dot_payments_dot_payments__api__pb2.GetLastPaymentInfoRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.GetLastPaymentInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChargeCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/ChargeCustomer',
            api_dot_service_dot_payments_dot_payments__api__pb2.ChargeCustomerRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.ChargeCustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCheckoutSessionLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.PaymentsAPI/CreateCheckoutSessionLink',
            api_dot_service_dot_payments_dot_payments__api__pb2.CreateCheckoutSessionLinkRequest.SerializeToString,
            api_dot_service_dot_payments_dot_payments__api__pb2.CreateCheckoutSessionLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
