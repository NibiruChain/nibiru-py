"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.auth.v1beta1.auth_pb2
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryAccountsRequest(google.protobuf.message.Message):
    """QueryAccountsRequest is the request type for the Query/Accounts RPC method.

    Since: cosmos-sdk 0.43
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
        pass
    def __init__(self,
        *,
        pagination: typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination",b"pagination"]) -> None: ...
global___QueryAccountsRequest = QueryAccountsRequest

class QueryAccountsResponse(google.protobuf.message.Message):
    """QueryAccountsResponse is the response type for the Query/Accounts RPC method.

    Since: cosmos-sdk 0.43
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNTS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """accounts are the existing accounts"""
        pass
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
        pass
    def __init__(self,
        *,
        accounts: typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
        pagination: typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts",b"accounts","pagination",b"pagination"]) -> None: ...
global___QueryAccountsResponse = QueryAccountsResponse

class QueryAccountRequest(google.protobuf.message.Message):
    """QueryAccountRequest is the request type for the Query/Account RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    address: typing.Text
    """address defines the address to query for."""

    def __init__(self,
        *,
        address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address"]) -> None: ...
global___QueryAccountRequest = QueryAccountRequest

class QueryAccountResponse(google.protobuf.message.Message):
    """QueryAccountResponse is the response type for the Query/Account RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> google.protobuf.any_pb2.Any:
        """account defines the account of the corresponding address."""
        pass
    def __init__(self,
        *,
        account: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account",b"account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account",b"account"]) -> None: ...
global___QueryAccountResponse = QueryAccountResponse

class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> cosmos.auth.v1beta1.auth_pb2.Params:
        """params defines the parameters of the module."""
        pass
    def __init__(self,
        *,
        params: typing.Optional[cosmos.auth.v1beta1.auth_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params",b"params"]) -> None: ...
global___QueryParamsResponse = QueryParamsResponse