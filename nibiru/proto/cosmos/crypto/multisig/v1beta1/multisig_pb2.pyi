"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MultiSignature(google.protobuf.message.Message):
    """MultiSignature wraps the signatures from a multisig.LegacyAminoPubKey.
    See cosmos.tx.v1betata1.ModeInfo.Multi for how to specify which signers
    signed and with which modes.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIGNATURES_FIELD_NUMBER: builtins.int
    @property
    def signatures(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self,
        *,
        signatures: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["signatures",b"signatures"]) -> None: ...
global___MultiSignature = MultiSignature

class CompactBitArray(google.protobuf.message.Message):
    """CompactBitArray is an implementation of a space efficient bit array.
    This is used to ensure that the encoded data takes up a minimal amount of
    space after proto encoding.
    This is not thread safe, and is not intended for concurrent usage.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTRA_BITS_STORED_FIELD_NUMBER: builtins.int
    ELEMS_FIELD_NUMBER: builtins.int
    extra_bits_stored: builtins.int
    elems: builtins.bytes
    def __init__(self,
        *,
        extra_bits_stored: builtins.int = ...,
        elems: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elems",b"elems","extra_bits_stored",b"extra_bits_stored"]) -> None: ...
global___CompactBitArray = CompactBitArray
