async def async_get_config_entry_diagnostics(hass, entry):
    return {
        "name": entry.data.get("name"),
        "host": entry.data.get("host"),
        "model": entry.data.get("model"),
        "base_port": entry.data.get("base_port"),
    }
