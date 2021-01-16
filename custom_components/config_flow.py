#  Copyright (c) 2021 Hombrelab <me@hombrelab.com>

# Config flow for the Watermeter Reader component.

import logging

import voluptuous as vol

from homeassistant import config_entries, exceptions
from homeassistant.config_entries import ConfigFlow

from .const import (
    DOMAIN,
    TITLE,
    TOPIC,
    DEFAULT_TOPIC
)

_LOGGER = logging.getLogger(__name__)


class WatermeterConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    CONNECTION_CLASS = config_entries.CONN_CLASS_UNKNOWN

    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is None:
            return await self._show_setup_form(user_input)

        errors = {}

        try:
            await is_valid(user_input)
        except ValidationError:
            errors["base"] = "variables_error"
            return await self._show_setup_form(errors)

        data = {
            TOPIC: user_input[TOPIC],
        }

        return self.async_create_entry(
            title=TITLE,
            data=data,
        )

    async def _show_setup_form(self, errors=None):
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(TOPIC, default=DEFAULT_TOPIC): str,
                }
            ),
            errors=errors or {},
        )


async def is_valid(user_input):
    if not user_input[TOPIC].strip():
        raise ValidationError


class ValidationError(exceptions.HomeAssistantError):
    """Error to indicate that data is not valid"""
