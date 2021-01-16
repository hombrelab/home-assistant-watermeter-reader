#  Copyright (c) 2021 Hombrelab <me@hombrelab.com>

# Constants for the Watermeter Reader component

DOMAIN = "watermeter_reader"
UUID = "ad926e34-7f56-4bb1-9d03-36593d1f8066"

SW_MANUFACTURER = "Hombrelab"
SW_NAME = "Watermeter Reader"
SW_VERSION = "2.0.000"

TITLE = "Home"

# labels
TOPIC = "topic"

# default values
DEFAULT_TOPIC = "home-assistant/watermeter/consumer"

# list of entities
ENTITIES = [
    [
        'Watermeter Consumed',
        'mdi:water',
        'm3',
        'pulsed'
    ],
    [
        'Watermeter Totals',
        'mdi:water',
        'm3',
        'totals'
    ],
    [
        'Watermeter Timestamp',
        'mdi:history',
        None,
        'timestamp'
    ]
]
