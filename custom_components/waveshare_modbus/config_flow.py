from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class WaveshareModbusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)

        schema = vol.Schema({
            vol.Required("name"): str,
            vol.Required("host"): str,
            vol.Required("model"): vol.In(["1CH", "2CH", "8CH"]),
            vol.Optional("base_port", default=502): int,
            vol.Optional("timeout", default=5): int,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
