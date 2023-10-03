# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/perp/v2/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from nibiru_proto.nibiru.perp.v2 import state_pb2 as nibiru_dot_perp_dot_v2_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17nibiru/perp/v2/tx.proto\x12\x0enibiru.perp.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1anibiru/perp/v2/state.proto\"\xb1\x01\n\x0fMsgRemoveMargin\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12M\n\x04pair\x18\x02 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12\x37\n\x06margin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06margin\"\xe8\x01\n\x17MsgRemoveMarginResponse\x12>\n\nmargin_out\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\tmarginOut\x12W\n\x0f\x66unding_payment\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0e\x66undingPayment\x12\x34\n\x08position\x18\x03 \x01(\x0b\x32\x18.nibiru.perp.v2.PositionR\x08position\"\xae\x01\n\x0cMsgAddMargin\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12M\n\x04pair\x18\x02 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12\x37\n\x06margin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06margin\"\xa5\x01\n\x14MsgAddMarginResponse\x12W\n\x0f\x66unding_payment\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0e\x66undingPayment\x12\x34\n\x08position\x18\x02 \x01(\x0b\x32\x18.nibiru.perp.v2.PositionR\x08position\"\xf4\x01\n\x11MsgMultiLiquidate\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12Q\n\x0cliquidations\x18\x02 \x03(\x0b\x32-.nibiru.perp.v2.MsgMultiLiquidate.LiquidationR\x0cliquidations\x1at\n\x0bLiquidation\x12M\n\x04pair\x18\x01 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12\x16\n\x06trader\x18\x02 \x01(\tR\x06trader\"\xb6\x03\n\x19MsgMultiLiquidateResponse\x12\x61\n\x0cliquidations\x18\x01 \x03(\x0b\x32=.nibiru.perp.v2.MsgMultiLiquidateResponse.LiquidationResponseR\x0cliquidations\x1a\xb5\x02\n\x13LiquidationResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05\x65rror\x18\x02 \x01(\tR\x05\x65rror\x12\x46\n\x0eliquidator_fee\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x01R\rliquidatorFee\x12?\n\x0bperp_ef_fee\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x01R\tperpEfFee\x12\x16\n\x06trader\x18\x05 \x01(\tR\x06trader\x12M\n\x04pair\x18\x06 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\"\xb7\x03\n\x0eMsgMarketOrder\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12M\n\x04pair\x18\x02 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12-\n\x04side\x18\x03 \x01(\x0e\x32\x19.nibiru.perp.v2.DirectionR\x04side\x12\\\n\x12quote_asset_amount\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x10quoteAssetAmount\x12J\n\x08leverage\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x08leverage\x12\x65\n\x17\x62\x61se_asset_amount_limit\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x14\x62\x61seAssetAmountLimit\"\xe3\x05\n\x16MsgMarketOrderResponse\x12\x34\n\x08position\x18\x01 \x01(\x0b\x32\x18.nibiru.perp.v2.PositionR\x08position\x12h\n\x18\x65xchanged_notional_value\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x16\x65xchangedNotionalValue\x12\x66\n\x17\x65xchanged_position_size\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x15\x65xchangedPositionSize\x12W\n\x0f\x66unding_payment\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0e\x66undingPayment\x12Q\n\x0crealized_pnl\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0brealizedPnl\x12`\n\x14unrealized_pnl_after\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x12unrealizedPnlAfter\x12V\n\x0fmargin_to_vault\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\rmarginToVault\x12[\n\x11position_notional\x18\x08 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x10positionNotional\"y\n\x10MsgClosePosition\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12M\n\x04pair\x18\x02 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\"\xf2\x03\n\x18MsgClosePositionResponse\x12h\n\x18\x65xchanged_notional_value\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x16\x65xchangedNotionalValue\x12\x66\n\x17\x65xchanged_position_size\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x15\x65xchangedPositionSize\x12W\n\x0f\x66unding_payment\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0e\x66undingPayment\x12Q\n\x0crealized_pnl\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0brealizedPnl\x12X\n\x10margin_to_trader\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0emarginToTrader\"\xbc\x01\n\x0fMsgPartialClose\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12M\n\x04pair\x18\x02 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12\x42\n\x04size\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x04size\"\xf1\x03\n\x17MsgPartialCloseResponse\x12h\n\x18\x65xchanged_notional_value\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x16\x65xchangedNotionalValue\x12\x66\n\x17\x65xchanged_position_size\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x15\x65xchangedPositionSize\x12W\n\x0f\x66unding_payment\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0e\x66undingPayment\x12Q\n\x0crealized_pnl\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0brealizedPnl\x12X\n\x10margin_to_trader\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0emarginToTrader\"\x82\x01\n\x18MsgDonateToEcosystemFund\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12N\n\x08\x64onation\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"donation\"R\x08\x64onation\"\"\n MsgDonateToEcosystemFundResponse2\xa1\x05\n\x03Msg\x12Z\n\x0cRemoveMargin\x12\x1f.nibiru.perp.v2.MsgRemoveMargin\x1a\'.nibiru.perp.v2.MsgRemoveMarginResponse\"\x00\x12Q\n\tAddMargin\x12\x1c.nibiru.perp.v2.MsgAddMargin\x1a$.nibiru.perp.v2.MsgAddMarginResponse\"\x00\x12`\n\x0eMultiLiquidate\x12!.nibiru.perp.v2.MsgMultiLiquidate\x1a).nibiru.perp.v2.MsgMultiLiquidateResponse\"\x00\x12W\n\x0bMarketOrder\x12\x1e.nibiru.perp.v2.MsgMarketOrder\x1a&.nibiru.perp.v2.MsgMarketOrderResponse\"\x00\x12]\n\rClosePosition\x12 .nibiru.perp.v2.MsgClosePosition\x1a(.nibiru.perp.v2.MsgClosePositionResponse\"\x00\x12Z\n\x0cPartialClose\x12\x1f.nibiru.perp.v2.MsgPartialClose\x1a\'.nibiru.perp.v2.MsgPartialCloseResponse\"\x00\x12u\n\x15\x44onateToEcosystemFund\x12(.nibiru.perp.v2.MsgDonateToEcosystemFund\x1a\x30.nibiru.perp.v2.MsgDonateToEcosystemFundResponse\"\x00\x42/Z-github.com/NibiruChain/nibiru/x/perp/v2/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nibiru.perp.v2.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/NibiruChain/nibiru/x/perp/v2/types'
  _MSGREMOVEMARGIN.fields_by_name['pair']._options = None
  _MSGREMOVEMARGIN.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGREMOVEMARGIN.fields_by_name['margin']._options = None
  _MSGREMOVEMARGIN.fields_by_name['margin']._serialized_options = b'\310\336\037\000'
  _MSGREMOVEMARGINRESPONSE.fields_by_name['margin_out']._options = None
  _MSGREMOVEMARGINRESPONSE.fields_by_name['margin_out']._serialized_options = b'\310\336\037\000'
  _MSGREMOVEMARGINRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGREMOVEMARGINRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGADDMARGIN.fields_by_name['pair']._options = None
  _MSGADDMARGIN.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGADDMARGIN.fields_by_name['margin']._options = None
  _MSGADDMARGIN.fields_by_name['margin']._serialized_options = b'\310\336\037\000'
  _MSGADDMARGINRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGADDMARGINRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMULTILIQUIDATE_LIQUIDATION.fields_by_name['pair']._options = None
  _MSGMULTILIQUIDATE_LIQUIDATION.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE.fields_by_name['liquidator_fee']._options = None
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE.fields_by_name['liquidator_fee']._serialized_options = b'\310\336\037\001'
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE.fields_by_name['perp_ef_fee']._options = None
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE.fields_by_name['perp_ef_fee']._serialized_options = b'\310\336\037\001'
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE.fields_by_name['pair']._options = None
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGMARKETORDER.fields_by_name['pair']._options = None
  _MSGMARKETORDER.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGMARKETORDER.fields_by_name['quote_asset_amount']._options = None
  _MSGMARKETORDER.fields_by_name['quote_asset_amount']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _MSGMARKETORDER.fields_by_name['leverage']._options = None
  _MSGMARKETORDER.fields_by_name['leverage']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDER.fields_by_name['base_asset_amount_limit']._options = None
  _MSGMARKETORDER.fields_by_name['base_asset_amount_limit']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _MSGMARKETORDERRESPONSE.fields_by_name['exchanged_notional_value']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['exchanged_notional_value']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDERRESPONSE.fields_by_name['exchanged_position_size']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['exchanged_position_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDERRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDERRESPONSE.fields_by_name['realized_pnl']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['realized_pnl']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDERRESPONSE.fields_by_name['unrealized_pnl_after']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['unrealized_pnl_after']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDERRESPONSE.fields_by_name['margin_to_vault']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['margin_to_vault']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGMARKETORDERRESPONSE.fields_by_name['position_notional']._options = None
  _MSGMARKETORDERRESPONSE.fields_by_name['position_notional']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGCLOSEPOSITION.fields_by_name['pair']._options = None
  _MSGCLOSEPOSITION.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_notional_value']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_notional_value']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_position_size']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_position_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['realized_pnl']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['realized_pnl']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['margin_to_trader']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['margin_to_trader']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGPARTIALCLOSE.fields_by_name['pair']._options = None
  _MSGPARTIALCLOSE.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MSGPARTIALCLOSE.fields_by_name['size']._options = None
  _MSGPARTIALCLOSE.fields_by_name['size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGPARTIALCLOSERESPONSE.fields_by_name['exchanged_notional_value']._options = None
  _MSGPARTIALCLOSERESPONSE.fields_by_name['exchanged_notional_value']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGPARTIALCLOSERESPONSE.fields_by_name['exchanged_position_size']._options = None
  _MSGPARTIALCLOSERESPONSE.fields_by_name['exchanged_position_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGPARTIALCLOSERESPONSE.fields_by_name['funding_payment']._options = None
  _MSGPARTIALCLOSERESPONSE.fields_by_name['funding_payment']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGPARTIALCLOSERESPONSE.fields_by_name['realized_pnl']._options = None
  _MSGPARTIALCLOSERESPONSE.fields_by_name['realized_pnl']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGPARTIALCLOSERESPONSE.fields_by_name['margin_to_trader']._options = None
  _MSGPARTIALCLOSERESPONSE.fields_by_name['margin_to_trader']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MSGDONATETOECOSYSTEMFUND.fields_by_name['donation']._options = None
  _MSGDONATETOECOSYSTEMFUND.fields_by_name['donation']._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"donation\"'
  _MSGREMOVEMARGIN._serialized_start=156
  _MSGREMOVEMARGIN._serialized_end=333
  _MSGREMOVEMARGINRESPONSE._serialized_start=336
  _MSGREMOVEMARGINRESPONSE._serialized_end=568
  _MSGADDMARGIN._serialized_start=571
  _MSGADDMARGIN._serialized_end=745
  _MSGADDMARGINRESPONSE._serialized_start=748
  _MSGADDMARGINRESPONSE._serialized_end=913
  _MSGMULTILIQUIDATE._serialized_start=916
  _MSGMULTILIQUIDATE._serialized_end=1160
  _MSGMULTILIQUIDATE_LIQUIDATION._serialized_start=1044
  _MSGMULTILIQUIDATE_LIQUIDATION._serialized_end=1160
  _MSGMULTILIQUIDATERESPONSE._serialized_start=1163
  _MSGMULTILIQUIDATERESPONSE._serialized_end=1601
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE._serialized_start=1292
  _MSGMULTILIQUIDATERESPONSE_LIQUIDATIONRESPONSE._serialized_end=1601
  _MSGMARKETORDER._serialized_start=1604
  _MSGMARKETORDER._serialized_end=2043
  _MSGMARKETORDERRESPONSE._serialized_start=2046
  _MSGMARKETORDERRESPONSE._serialized_end=2785
  _MSGCLOSEPOSITION._serialized_start=2787
  _MSGCLOSEPOSITION._serialized_end=2908
  _MSGCLOSEPOSITIONRESPONSE._serialized_start=2911
  _MSGCLOSEPOSITIONRESPONSE._serialized_end=3409
  _MSGPARTIALCLOSE._serialized_start=3412
  _MSGPARTIALCLOSE._serialized_end=3600
  _MSGPARTIALCLOSERESPONSE._serialized_start=3603
  _MSGPARTIALCLOSERESPONSE._serialized_end=4100
  _MSGDONATETOECOSYSTEMFUND._serialized_start=4103
  _MSGDONATETOECOSYSTEMFUND._serialized_end=4233
  _MSGDONATETOECOSYSTEMFUNDRESPONSE._serialized_start=4235
  _MSGDONATETOECOSYSTEMFUNDRESPONSE._serialized_end=4269
  _MSG._serialized_start=4272
  _MSG._serialized_end=4945
# @@protoc_insertion_point(module_scope)