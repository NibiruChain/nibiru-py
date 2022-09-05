import time
from typing import List

import nibiru
import nibiru.msg
from nibiru import Network, common
from nibiru.event_specs import EventCaptured
from nibiru.websocket import EventType, NibiruWebsocket
from tests import LOGGER


def test_websocket_listen(val_node: nibiru.Sdk, network: Network):
    """
    Open a position and ensure output is correct
    """
    pair = "ubtc:unusd"

    nibiru_websocket = NibiruWebsocket(
        network,
        [
            EventType.MarkPriceChanged,
            EventType.PositionChangedEvent,
        ],
    )
    nibiru_websocket.start()
    time.sleep(1)

    # Open a position from the validator node
    LOGGER.info("Opening position")
    val_node.tx.execute_msgs(
        nibiru.msg.MsgOpenPosition(
            sender=val_node.address,
            token_pair=pair,
            side=common.Side.BUY,
            quote_asset_amount=10,
            leverage=10,
            base_asset_amount_limit=0,
        )
    )

    # Give time for events to come
    LOGGER.info("Sent txs, waiting for websocket to pick it up")
    time.sleep(1)

    nibiru_websocket.queue.put(None)
    events: List[EventCaptured] = []
    event = 1
    while True:
        event = nibiru_websocket.queue.get()
        if event is None:
            break
        events.append(event)

    # Asserting for truth because test are running in parallel in the same chain and might result in
    # duplication of markpricechanged events.
    assert all(
        event in [event.event_type for event in events]
        for event in [
            EventType.MarkPriceChanged.value,
            EventType.PositionChangedEvent.value,
        ]
    )
