"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.auth.v1beta1.auth_pb2
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class QueryAccountsRequest(google.protobuf.message.Message):
    """QueryAccountsRequest is the request type for the Query/Accounts RPC method.

    Since: cosmos-sdk 0.43
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> None: ...

global___QueryAccountsRequest = QueryAccountsRequest

@typing_extensions.final
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
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts", "pagination", b"pagination"]) -> None: ...

global___QueryAccountsResponse = QueryAccountsResponse

@typing_extensions.final
class QueryAccountRequest(google.protobuf.message.Message):
    """QueryAccountRequest is the request type for the Query/Account RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """address defines the address to query for."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address"]) -> None: ...

global___QueryAccountRequest = QueryAccountRequest

@typing_extensions.final
class QueryAccountResponse(google.protobuf.message.Message):
    """QueryAccountResponse is the response type for the Query/Account RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> google.protobuf.any_pb2.Any:
        """account defines the account of the corresponding address."""
    def __init__(
        self,
        *,
        account: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account", b"account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account"]) -> None: ...

global___QueryAccountResponse = QueryAccountResponse

@typing_extensions.final
class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

@typing_extensions.final
class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> cosmos.auth.v1beta1.auth_pb2.Params:
        """params defines the parameters of the module."""
    def __init__(
        self,
        *,
        params: cosmos.auth.v1beta1.auth_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing_extensions.final
class QueryModuleAccountsRequest(google.protobuf.message.Message):
    """QueryModuleAccountsRequest is the request type for the Query/ModuleAccounts RPC method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryModuleAccountsRequest = QueryModuleAccountsRequest

@typing_extensions.final
class QueryModuleAccountsResponse(google.protobuf.message.Message):
    """QueryModuleAccountsResponse is the response type for the Query/ModuleAccounts RPC method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts"]) -> None: ...

global___QueryModuleAccountsResponse = QueryModuleAccountsResponse

@typing_extensions.final
class QueryModuleAccountByNameRequest(google.protobuf.message.Message):
    """QueryModuleAccountByNameRequest is the request type for the Query/ModuleAccountByName RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___QueryModuleAccountByNameRequest = QueryModuleAccountByNameRequest

@typing_extensions.final
class QueryModuleAccountByNameResponse(google.protobuf.message.Message):
    """QueryModuleAccountByNameResponse is the response type for the Query/ModuleAccountByName RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        account: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account", b"account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account"]) -> None: ...

global___QueryModuleAccountByNameResponse = QueryModuleAccountByNameResponse

@typing_extensions.final
class Bech32PrefixRequest(google.protobuf.message.Message):
    """Bech32PrefixRequest is the request type for Bech32Prefix rpc method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Bech32PrefixRequest = Bech32PrefixRequest

@typing_extensions.final
class Bech32PrefixResponse(google.protobuf.message.Message):
    """Bech32PrefixResponse is the response type for Bech32Prefix rpc method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BECH32_PREFIX_FIELD_NUMBER: builtins.int
    bech32_prefix: builtins.str
    def __init__(
        self,
        *,
        bech32_prefix: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bech32_prefix", b"bech32_prefix"]) -> None: ...

global___Bech32PrefixResponse = Bech32PrefixResponse

@typing_extensions.final
class AddressBytesToStringRequest(google.protobuf.message.Message):
    """AddressBytesToStringRequest is the request type for AddressString rpc method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_BYTES_FIELD_NUMBER: builtins.int
    address_bytes: builtins.bytes
    def __init__(
        self,
        *,
        address_bytes: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_bytes", b"address_bytes"]) -> None: ...

global___AddressBytesToStringRequest = AddressBytesToStringRequest

@typing_extensions.final
class AddressBytesToStringResponse(google.protobuf.message.Message):
    """AddressBytesToStringResponse is the response type for AddressString rpc method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_STRING_FIELD_NUMBER: builtins.int
    address_string: builtins.str
    def __init__(
        self,
        *,
        address_string: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_string", b"address_string"]) -> None: ...

global___AddressBytesToStringResponse = AddressBytesToStringResponse

@typing_extensions.final
class AddressStringToBytesRequest(google.protobuf.message.Message):
    """AddressStringToBytesRequest is the request type for AccountBytes rpc method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_STRING_FIELD_NUMBER: builtins.int
    address_string: builtins.str
    def __init__(
        self,
        *,
        address_string: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_string", b"address_string"]) -> None: ...

global___AddressStringToBytesRequest = AddressStringToBytesRequest

@typing_extensions.final
class AddressStringToBytesResponse(google.protobuf.message.Message):
    """AddressStringToBytesResponse is the response type for AddressBytes rpc method.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_BYTES_FIELD_NUMBER: builtins.int
    address_bytes: builtins.bytes
    def __init__(
        self,
        *,
        address_bytes: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_bytes", b"address_bytes"]) -> None: ...

global___AddressStringToBytesResponse = AddressStringToBytesResponse

@typing_extensions.final
class QueryAccountAddressByIDRequest(google.protobuf.message.Message):
    """QueryAccountAddressByIDRequest is the request type for AccountAddressByID rpc method

    Since: cosmos-sdk 0.46.2
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    id: builtins.int
    """Deprecated, use account_id instead

    id is the account number of the address to be queried. This field
    should have been an uint64 (like all account numbers), and will be
    updated to uint64 in a future version of the auth query.
    """
    account_id: builtins.int
    """account_id is the account number of the address to be queried.

    Since: cosmos-sdk 0.47
    """
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        account_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id", b"account_id", "id", b"id"]) -> None: ...

global___QueryAccountAddressByIDRequest = QueryAccountAddressByIDRequest

@typing_extensions.final
class QueryAccountAddressByIDResponse(google.protobuf.message.Message):
    """QueryAccountAddressByIDResponse is the response type for AccountAddressByID rpc method

    Since: cosmos-sdk 0.46.2
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ADDRESS_FIELD_NUMBER: builtins.int
    account_address: builtins.str
    def __init__(
        self,
        *,
        account_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_address", b"account_address"]) -> None: ...

global___QueryAccountAddressByIDResponse = QueryAccountAddressByIDResponse

@typing_extensions.final
class QueryAccountInfoRequest(google.protobuf.message.Message):
    """QueryAccountInfoRequest is the Query/AccountInfo request type.

    Since: cosmos-sdk 0.47
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """address is the account address string."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address"]) -> None: ...

global___QueryAccountInfoRequest = QueryAccountInfoRequest

@typing_extensions.final
class QueryAccountInfoResponse(google.protobuf.message.Message):
    """QueryAccountInfoResponse is the Query/AccountInfo response type.

    Since: cosmos-sdk 0.47
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> cosmos.auth.v1beta1.auth_pb2.BaseAccount:
        """info is the account info which is represented by BaseAccount."""
    def __init__(
        self,
        *,
        info: cosmos.auth.v1beta1.auth_pb2.BaseAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___QueryAccountInfoResponse = QueryAccountInfoResponse