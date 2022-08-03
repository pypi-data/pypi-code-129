# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layerapi.api.service.credits import credits_api_pb2 as api_dot_service_dot_credits_dot_credits__api__pb2


class CreditsAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCreditLogV2 = channel.unary_unary(
                '/api.CreditsAPI/GetCreditLogV2',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Request.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Response.FromString,
                )
        self.RecordBillableActivity = channel.unary_unary(
                '/api.CreditsAPI/RecordBillableActivity',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityResponse.FromString,
                )
        self.SetBalanceToFreeAllowance = channel.unary_unary(
                '/api.CreditsAPI/SetBalanceToFreeAllowance',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.SetBalanceToFreeAllowanceRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.SetBalanceToFreeAllowanceResponse.FromString,
                )
        self.FundBalance = channel.unary_unary(
                '/api.CreditsAPI/FundBalance',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.FundBalanceRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.FundBalanceResponse.FromString,
                )
        self.RefillAllBalancesUpToFreeAllowance = channel.unary_unary(
                '/api.CreditsAPI/RefillAllBalancesUpToFreeAllowance',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.RefillAllBalancesUpToFreeAllowanceRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.RefillAllBalancesUpToFreeAllowanceResponse.FromString,
                )
        self.GetMonthlyBillingReport = channel.unary_unary(
                '/api.CreditsAPI/GetMonthlyBillingReport',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportResponse.FromString,
                )
        self.GetCreditsBalance = channel.unary_unary(
                '/api.CreditsAPI/GetCreditsBalance',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceResponse.FromString,
                )
        self.GetWeeklyUsageReport = channel.unary_unary(
                '/api.CreditsAPI/GetWeeklyUsageReport',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportResponse.FromString,
                )


class CreditsAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCreditLogV2(self, request, context):
        """v2
        if we were using packages we could use package versions:
        https://github.com/uber/prototool/blob/dev/style/README.md#directory-structure
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordBillableActivity(self, request, context):
        """Billable activities are reported progressively as they are performed.
        The reported activity duration, indicated by start and end times, is used to compute an interim credit balance.
        The total consumed credit balance for an activity will be the sum of all interim credit balances.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetBalanceToFreeAllowance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FundBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefillAllBalancesUpToFreeAllowance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMonthlyBillingReport(self, request, context):
        """v1
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCreditsBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWeeklyUsageReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CreditsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCreditLogV2': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCreditLogV2,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Request.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Response.SerializeToString,
            ),
            'RecordBillableActivity': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordBillableActivity,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityResponse.SerializeToString,
            ),
            'SetBalanceToFreeAllowance': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBalanceToFreeAllowance,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.SetBalanceToFreeAllowanceRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.SetBalanceToFreeAllowanceResponse.SerializeToString,
            ),
            'FundBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.FundBalance,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.FundBalanceRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.FundBalanceResponse.SerializeToString,
            ),
            'RefillAllBalancesUpToFreeAllowance': grpc.unary_unary_rpc_method_handler(
                    servicer.RefillAllBalancesUpToFreeAllowance,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.RefillAllBalancesUpToFreeAllowanceRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.RefillAllBalancesUpToFreeAllowanceResponse.SerializeToString,
            ),
            'GetMonthlyBillingReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMonthlyBillingReport,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportResponse.SerializeToString,
            ),
            'GetCreditsBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCreditsBalance,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceResponse.SerializeToString,
            ),
            'GetWeeklyUsageReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWeeklyUsageReport,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.CreditsAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CreditsAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCreditLogV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetCreditLogV2',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Request.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordBillableActivity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/RecordBillableActivity',
            api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetBalanceToFreeAllowance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/SetBalanceToFreeAllowance',
            api_dot_service_dot_credits_dot_credits__api__pb2.SetBalanceToFreeAllowanceRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.SetBalanceToFreeAllowanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FundBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/FundBalance',
            api_dot_service_dot_credits_dot_credits__api__pb2.FundBalanceRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.FundBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RefillAllBalancesUpToFreeAllowance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/RefillAllBalancesUpToFreeAllowance',
            api_dot_service_dot_credits_dot_credits__api__pb2.RefillAllBalancesUpToFreeAllowanceRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.RefillAllBalancesUpToFreeAllowanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMonthlyBillingReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetMonthlyBillingReport',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCreditsBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetCreditsBalance',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWeeklyUsageReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetWeeklyUsageReport',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
