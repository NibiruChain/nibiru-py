"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.46"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BIP44Params(google.protobuf.message.Message):
    """BIP44Params is used as path field in ledger item in Record."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PURPOSE_FIELD_NUMBER: builtins.int
    COIN_TYPE_FIELD_NUMBER: builtins.int
    ACCOUNT_FIELD_NUMBER: builtins.int
    CHANGE_FIELD_NUMBER: builtins.int
    ADDRESS_INDEX_FIELD_NUMBER: builtins.int
    purpose: builtins.int
    """purpose is a constant set to 44' (or 0x8000002C) following the BIP43 recommendation"""
    coin_type: builtins.int
    """coin_type is a constant that improves privacy"""
    account: builtins.int
    """account splits the key space into independent user identities"""
    change: builtins.bool
    """change is a constant used for public derivation. Constant 0 is used for external chain and constant 1 for internal
    chain.
    """
    address_index: builtins.int
    """address_index is used as child index in BIP32 derivation"""
    def __init__(
        self,
        *,
        purpose: builtins.int = ...,
        coin_type: builtins.int = ...,
        account: builtins.int = ...,
        change: builtins.bool = ...,
        address_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account", "address_index", b"address_index", "change", b"change", "coin_type", b"coin_type", "purpose", b"purpose"]) -> None: ...

global___BIP44Params = BIP44Params