# Copyright (c) 2021 Hombrelab <me@hombrelab.com>
# Sensor for the Watermeter Reader component.

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.helpers.restore_state import RestoreEntity

import json
import logging

from . import WatermeterReaderDevice
from .const import (
    DOMAIN,
    UUID,
    TOPIC,
    ENTITIES
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry, async_add_entities):
    """Set up entities based on a config entry."""

    # Add MQTT library
    mqtt = hass.components.mqtt

    # Generate device entities
    entities = [WatermeterEntity(
        name, icon, unit, element) for name, icon, unit, element in ENTITIES]

    # Set up the sensor platform
    async_add_entities(entities)

    def update_entities_reader(payload):
        _LOGGER.debug(payload)

        # Make all device entities aware of new payload
        for entity in entities:
            entity.setAttributes(payload)

            hass.async_create_task(entity.async_update_ha_state())

    # Call MQTT subscribe function
    def reader_callback(message):
        # Call callback
        if message is not None:
            update_entities_reader(message.payload)

    hass.async_create_task(mqtt.async_subscribe(entry.data[TOPIC], reader_callback, 0))


class WatermeterEntity(WatermeterReaderDevice, RestoreEntity):
    def __init__(self, name, icon, unit, element):
        # Initialize the sensor
        self._name = name
        self._icon = icon
        self._unit = unit
        self._element = element

        self._attributes = {}
        self._state = '-'

    def setAttributes(self, payload):
        self._attributes = json.loads(payload)

    @property
    def unique_id(self) -> str:
        """Return the unique ID for this switch."""
        return f"{UUID}.sensor.{self._name}"

    @property
    def device_state_attributes(self):
        return self._attributes

    @property
    def name(self):
        # Return the name of the sensor
        return self._name

    @property
    def icon(self):
        # Icon to use in the frontend, if any
        return self._icon

    @property
    def unit_of_measurement(self):
        # Return the unit of measurement
        return self._unit

    @property
    def state(self):
        # Return the state of the sensor
        return self._state

    def update(self):
        # Fetch new state data for the sensor
        if self._attributes and self._element in self._attributes:
            self._state = self._attributes[self._element]

    async def async_added_to_hass(self):
        await super().async_added_to_hass()

        state = await self.async_get_last_state()

        if state:
            try:
                self._attributes = state.attributes
                self._state = state.state
            except ValueError as err:
                _LOGGER.warning("Could not restore last state: %s", err)
