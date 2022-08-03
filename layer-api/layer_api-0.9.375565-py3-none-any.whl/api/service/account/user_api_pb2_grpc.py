# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layerapi.api.service.account import user_api_pb2 as api_dot_service_dot_account_dot_user__api__pb2


class UserAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/api.UserAPI/GetUser',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserResponse.FromString,
                )
        self.GetUserByAccountId = channel.unary_unary(
                '/api.UserAPI/GetUserByAccountId',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserByAccountIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserByAccountIdResponse.FromString,
                )
        self.GetUserOrganizations = channel.unary_unary(
                '/api.UserAPI/GetUserOrganizations',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserOrganizationsRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserOrganizationsResponse.FromString,
                )
        self.GetOrganizationByName = channel.unary_unary(
                '/api.UserAPI/GetOrganizationByName',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByNameRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByNameResponse.FromString,
                )
        self.GetOrganizationByAccountId = channel.unary_unary(
                '/api.UserAPI/GetOrganizationByAccountId',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByAccountIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByAccountIdResponse.FromString,
                )
        self.GetOrganizationMembers = channel.unary_unary(
                '/api.UserAPI/GetOrganizationMembers',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationMembersRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationMembersResponse.FromString,
                )
        self.UpdateOrganization = channel.unary_unary(
                '/api.UserAPI/UpdateOrganization',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.UpdateOrganizationRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.UpdateOrganizationResponse.FromString,
                )
        self.GetOrganizationInvites = channel.unary_unary(
                '/api.UserAPI/GetOrganizationInvites',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationInvitesRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationInvitesResponse.FromString,
                )
        self.CreateOrganizationInvite = channel.unary_unary(
                '/api.UserAPI/CreateOrganizationInvite',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.CreateOrganizationInviteRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.CreateOrganizationInviteResponse.FromString,
                )
        self.RevokeOrganizationInvite = channel.unary_unary(
                '/api.UserAPI/RevokeOrganizationInvite',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.RevokeOrganizationInviteRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.RevokeOrganizationInviteResponse.FromString,
                )
        self.RemoveUserFromOrganization = channel.unary_unary(
                '/api.UserAPI/RemoveUserFromOrganization',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.RemoveUserFromOrganizationRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.RemoveUserFromOrganizationResponse.FromString,
                )
        self.GetConnections = channel.unary_unary(
                '/api.UserAPI/GetConnections',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetConnectionsRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetConnectionsResponse.FromString,
                )
        self.EnableConnectionForOrganization = channel.unary_unary(
                '/api.UserAPI/EnableConnectionForOrganization',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.EnableConnectionForOrganizationRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.EnableConnectionForOrganizationResponse.FromString,
                )
        self.GetGuestAuthToken = channel.unary_unary(
                '/api.UserAPI/GetGuestAuthToken',
                request_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetGuestAuthTokenRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetGuestAuthTokenResponse.FromString,
                )


class UserAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByAccountId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserOrganizations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganizationByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganizationByAccountId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganizationMembers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrganization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganizationInvites(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrganizationInvite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeOrganizationInvite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUserFromOrganization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConnections(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableConnectionForOrganization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGuestAuthToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserResponse.SerializeToString,
            ),
            'GetUserByAccountId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByAccountId,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserByAccountIdRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserByAccountIdResponse.SerializeToString,
            ),
            'GetUserOrganizations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserOrganizations,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserOrganizationsRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetUserOrganizationsResponse.SerializeToString,
            ),
            'GetOrganizationByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganizationByName,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByNameRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByNameResponse.SerializeToString,
            ),
            'GetOrganizationByAccountId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganizationByAccountId,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByAccountIdRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByAccountIdResponse.SerializeToString,
            ),
            'GetOrganizationMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganizationMembers,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationMembersRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationMembersResponse.SerializeToString,
            ),
            'UpdateOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOrganization,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.UpdateOrganizationRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.UpdateOrganizationResponse.SerializeToString,
            ),
            'GetOrganizationInvites': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganizationInvites,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationInvitesRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationInvitesResponse.SerializeToString,
            ),
            'CreateOrganizationInvite': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrganizationInvite,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.CreateOrganizationInviteRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.CreateOrganizationInviteResponse.SerializeToString,
            ),
            'RevokeOrganizationInvite': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeOrganizationInvite,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.RevokeOrganizationInviteRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.RevokeOrganizationInviteResponse.SerializeToString,
            ),
            'RemoveUserFromOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUserFromOrganization,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.RemoveUserFromOrganizationRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.RemoveUserFromOrganizationResponse.SerializeToString,
            ),
            'GetConnections': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConnections,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetConnectionsRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetConnectionsResponse.SerializeToString,
            ),
            'EnableConnectionForOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableConnectionForOrganization,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.EnableConnectionForOrganizationRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.EnableConnectionForOrganizationResponse.SerializeToString,
            ),
            'GetGuestAuthToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGuestAuthToken,
                    request_deserializer=api_dot_service_dot_account_dot_user__api__pb2.GetGuestAuthTokenRequest.FromString,
                    response_serializer=api_dot_service_dot_account_dot_user__api__pb2.GetGuestAuthTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.UserAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetUser',
            api_dot_service_dot_account_dot_user__api__pb2.GetUserRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByAccountId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetUserByAccountId',
            api_dot_service_dot_account_dot_user__api__pb2.GetUserByAccountIdRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetUserByAccountIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserOrganizations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetUserOrganizations',
            api_dot_service_dot_account_dot_user__api__pb2.GetUserOrganizationsRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetUserOrganizationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganizationByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetOrganizationByName',
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByNameRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganizationByAccountId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetOrganizationByAccountId',
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByAccountIdRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationByAccountIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganizationMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetOrganizationMembers',
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationMembersRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/UpdateOrganization',
            api_dot_service_dot_account_dot_user__api__pb2.UpdateOrganizationRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.UpdateOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganizationInvites(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetOrganizationInvites',
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationInvitesRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetOrganizationInvitesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOrganizationInvite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/CreateOrganizationInvite',
            api_dot_service_dot_account_dot_user__api__pb2.CreateOrganizationInviteRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.CreateOrganizationInviteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeOrganizationInvite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/RevokeOrganizationInvite',
            api_dot_service_dot_account_dot_user__api__pb2.RevokeOrganizationInviteRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.RevokeOrganizationInviteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveUserFromOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/RemoveUserFromOrganization',
            api_dot_service_dot_account_dot_user__api__pb2.RemoveUserFromOrganizationRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.RemoveUserFromOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConnections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetConnections',
            api_dot_service_dot_account_dot_user__api__pb2.GetConnectionsRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetConnectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableConnectionForOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/EnableConnectionForOrganization',
            api_dot_service_dot_account_dot_user__api__pb2.EnableConnectionForOrganizationRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.EnableConnectionForOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGuestAuthToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserAPI/GetGuestAuthToken',
            api_dot_service_dot_account_dot_user__api__pb2.GetGuestAuthTokenRequest.SerializeToString,
            api_dot_service_dot_account_dot_user__api__pb2.GetGuestAuthTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
