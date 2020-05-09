"""
Constants for the Watermeter Reader component
"""

DOMAIN = "watermeter_reader"
UUID = "ad926e34-7f56-4bb1-9d03-36593d1f8066"

SW_MANUFACTURER = "Hombrelab"
SW_NAME = "Watermeter Reader"
SW_VERSION = "1.0.2"

TITLE = "Home"

# labels
TOPIC = "topic"

# default values
DEFAULT_TOPIC = "home-assistant/watermeter-reader"

# list of entities
ENTITIES = [
    [
        'Watermeter Liter Consumed',
        'mdi:water',
        'm3',
        'litersConsumed'
    ],
    [
        'Watermeter Liter Timestamp',
        'mdi:history',
        None,
        'litersTimestamp'
    ],
    [
        'Watermeter Last Consumed',
        'mdi:water',
        'm3',
        'lastConsumed'
    ],
    [
        'Watermeter Last Timestamp',
        'mdi:history',
        None,
        'lastTimestamp'
    ],
    [
        'Watermeter Pulse',
        'mdi:pulse',
        None,
        'pulse'
    ],
    [
        'Watermeter Consumed',
        'mdi:water',
        'm3',
        'consumed'
    ],
    [
        'Watermeter Timestamp',
        'mdi:update',
        None,
        'timestamp'
    ]
]
