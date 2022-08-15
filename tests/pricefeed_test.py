# pricefeed_test.py
from datetime import datetime, timedelta

import tests
from nibiru import common

from . import CONFIG


class TestPricefeed(tests.ModuleTest):
    def test_post_prices(self):
        """
        Open a position and ensure output is correct
        """
        self.oracle = self.create_new_agent_with_funds(
            [common.Coin(10000, "unibi")], CONFIG.ORACLE_MNEMONIC
        )

        # Check queries
        markets_output = self.oracle.query.pricefeed.markets()

        self.assertIsInstance(markets_output, dict)
        self.assertTrue(
            any(
                [
                    market["pair_id"] == "unibi:unusd"
                    for market in markets_output["markets"]
                ]
            )
        )

        unibiunusd_pair = [
            market
            for market in markets_output["markets"]
            if market["pair_id"] == "unibi:unusd"
        ][0]

        self.assertIn(self.oracle.address, unibiunusd_pair["oracles"])

        # Post price
        tx_output = self.oracle.tx.pricefeed.post_price(
            self.oracle.address,
            token0="unibi",
            token1="unusd",
            price=10,
            expiry=datetime.utcnow() + timedelta(hours=1),
        )
        self.validate_tx_output(tx_output)

        # Post price price again so we are sure we waited 1 block for price to be set before next queries.
        tx_output = self.oracle.tx.pricefeed.post_price(
            self.oracle.address,
            token0="unibi",
            token1="unusd",
            price=10,
            expiry=datetime.utcnow() + timedelta(hours=1),
        )
        self.validate_tx_output(tx_output)

        # Query raw prices
        raw_prices = self.oracle.query.pricefeed.raw_prices("unibi:unusd")["raw_prices"]

        self.assertGreaterEqual(len(raw_prices), 1)
        self.assertCountEqual(
            raw_prices[0].keys(), ['expiry', 'oracle_address', 'pair_id', 'price']
        )

        # Query pricefeed params
        params = self.oracle.query.pricefeed.params()["params"]
        self.assertCountEqual(params.keys(), ['pairs', 'twap_lookback_window'])

        # Query price for unibi:unusd
        price = self.oracle.query.pricefeed.price("unibi:unusd")["price"]
        self.assertCountEqual(price.keys(), ["pair_id", "price"])

        # Query prices
        prices = self.oracle.query.pricefeed.prices()["prices"]
        self.assertTrue(any([price["pair_id"] == "unibi:unusd" for price in prices]))

        unibiprice = [price for price in prices if price["pair_id"] == "unibi:unusd"][0]
        self.assertCountEqual(unibiprice.keys(), ["pair_id", "price"])
