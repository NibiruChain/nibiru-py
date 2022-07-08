"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MsgMintStable(google.protobuf.message.Message):
    """
    MsgMintStable: Msg to mint NUSD. A user deposits NIBI and collateral and gets 
    NUSD in return. The amount of NUSD received depends on the current price set 
    by the pricefeed library and the current collateral ratio for the protocol.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CREATOR_FIELD_NUMBER: builtins.int
    STABLE_FIELD_NUMBER: builtins.int
    creator: typing.Text
    @property
    def stable(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(self,
        *,
        creator: typing.Text = ...,
        stable: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["stable",b"stable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["creator",b"creator","stable",b"stable"]) -> None: ...
global___MsgMintStable = MsgMintStable

class MsgMintStableResponse(google.protobuf.message.Message):
    """MsgMintStableResponse specifies the amount of NUSD token the user will receive after their
    mint transaction
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STABLE_FIELD_NUMBER: builtins.int
    USED_COINS_FIELD_NUMBER: builtins.int
    FEES_PAYED_FIELD_NUMBER: builtins.int
    @property
    def stable(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def used_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def fees_payed(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        stable: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        used_coins: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        fees_payed: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["stable",b"stable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fees_payed",b"fees_payed","stable",b"stable","used_coins",b"used_coins"]) -> None: ...
global___MsgMintStableResponse = MsgMintStableResponse

class MsgBurnStable(google.protobuf.message.Message):
    """
    MsgBurnStable allows users to burn NUSD in exchange for NIBI and collateral. 
    The amount of NIBI and Collateral received depends on the current price set by 
    the x/pricefeed library and the current collateral ratio.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CREATOR_FIELD_NUMBER: builtins.int
    STABLE_FIELD_NUMBER: builtins.int
    creator: typing.Text
    @property
    def stable(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(self,
        *,
        creator: typing.Text = ...,
        stable: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["stable",b"stable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["creator",b"creator","stable",b"stable"]) -> None: ...
global___MsgBurnStable = MsgBurnStable

class MsgBurnStableResponse(google.protobuf.message.Message):
    """MsgBurnStableResponse specifies the amount of collateral and governance 
    token the user will receive after their burn transaction.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COLLATERAL_FIELD_NUMBER: builtins.int
    GOV_FIELD_NUMBER: builtins.int
    FEES_PAYED_FIELD_NUMBER: builtins.int
    @property
    def collateral(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def gov(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def fees_payed(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        collateral: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        gov: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        fees_payed: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["collateral",b"collateral","gov",b"gov"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["collateral",b"collateral","fees_payed",b"fees_payed","gov",b"gov"]) -> None: ...
global___MsgBurnStableResponse = MsgBurnStableResponse

class MsgRecollateralize(google.protobuf.message.Message):
    """MsgRecollateralize"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CREATOR_FIELD_NUMBER: builtins.int
    COLL_FIELD_NUMBER: builtins.int
    creator: typing.Text
    @property
    def coll(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(self,
        *,
        creator: typing.Text = ...,
        coll: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["coll",b"coll"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coll",b"coll","creator",b"creator"]) -> None: ...
global___MsgRecollateralize = MsgRecollateralize

class MsgRecollateralizeResponse(google.protobuf.message.Message):
    """MsgRecollateralizeResponse is the output of a successful 'Recollateralize'"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GOV_FIELD_NUMBER: builtins.int
    @property
    def gov(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Gov (sdk.Coin): Tokens rewarded to the caller in exchange for her collateral."""
        pass
    def __init__(self,
        *,
        gov: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gov",b"gov"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gov",b"gov"]) -> None: ...
global___MsgRecollateralizeResponse = MsgRecollateralizeResponse

class MsgBuyback(google.protobuf.message.Message):
    """MsgBuyback"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CREATOR_FIELD_NUMBER: builtins.int
    GOV_FIELD_NUMBER: builtins.int
    creator: typing.Text
    @property
    def gov(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Gov (sdk.Coin): Tokens the caller wants to sell to the protocol in exchange 
        for collateral.
        """
        pass
    def __init__(self,
        *,
        creator: typing.Text = ...,
        gov: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gov",b"gov"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["creator",b"creator","gov",b"gov"]) -> None: ...
global___MsgBuyback = MsgBuyback

class MsgBuybackResponse(google.protobuf.message.Message):
    """MsgBuybackResponse is the output of a successful 'Buyback'"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COLL_FIELD_NUMBER: builtins.int
    @property
    def coll(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Coll (sdk.Coin): Tokens sold to the caller in exchange for her collateral."""
        pass
    def __init__(self,
        *,
        coll: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["coll",b"coll"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coll",b"coll"]) -> None: ...
global___MsgBuybackResponse = MsgBuybackResponse