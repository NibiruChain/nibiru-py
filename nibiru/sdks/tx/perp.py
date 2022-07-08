from nibiru.common import Side
from nibiru.composers.perp_composer import PerpComposer

from nibiru.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb

from .common import Tx

class Perp(Tx):
    def remove_margin(self, sender: str, token_pair: str, margin: coin_pb.Coin):
        msg = PerpComposer.remove_margin(sender = sender, token_pair = token_pair, margin = margin)
        return super().execute(msg)
    

    def add_margin(self, sender: str, token_pair: str, margin: coin_pb.Coin):
        msg = PerpComposer.add_margin(sender = sender, token_pair = token_pair, margin = margin)
        return super().execute(msg)

    def liquidate(self, sender: str, token_pair: str, trader: str):
        msg = PerpComposer.liquidate(sender = sender, token_pair = token_pair, trader = trader)
        return super().execute(msg)

    def open_position(self, sender: str, token_pair: str, side: Side, quote_asset_amount: str, leverage: str, base_asset_amount_limit: str):
        msg = PerpComposer.open_position(
            sender = sender,
            token_pair = token_pair,
            side = side,
            quote_asset_amount = quote_asset_amount,
            leverage = leverage,
            base_asset_amount_limit = base_asset_amount_limit,
        )
        return super().execute(msg)

    def close_position(self, sender: str, token_pair: str):
        msg = PerpComposer.close_position(
            sender = sender,
            token_pair = token_pair,
        )
        return super().execute(msg)