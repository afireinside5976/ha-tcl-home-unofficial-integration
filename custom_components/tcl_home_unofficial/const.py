"""Constants for the TCL Home - Unofficial integration."""


def get_device_data_storege_key(device_id: str) -> str:
    """Get the storage key for a device."""
    return f"{DOMAIN}.device_data_storage.{device_id}"


def get_device_self_dignose_storege_key(device_id: str) -> str:
    """Get the storage key for a device."""
    return f"{DOMAIN}.device_self_dignose_storage.{device_id}"


def get_internal_settings_storege_key() -> str:
    """Get the storage key for a device."""
    return f"{DOMAIN}.internal_settings_storage"

DOMAIN = "tcl_home_unofficial"


DEFAULT_APP_LOGI_URL = "https://pa.account.tcl.com/account/login?clientId=54148614"
DEFAULT_APP_CLOUD_URL = "https://prod-center.aws.tcljd.com/v3/global/cloud_url_get"

DEFAULT_APP_ID = "wx6e1af3fa84fbe523"

DEFAULT_USER = ""
DEFAULT_PW = ""

# How often (in seconds) to poll the TCL cloud for device state.
# Applies to power, mode, temperature, fan speed, eco, sleep.
# Note: energy/power consumption sensors always refresh hourly regardless.
# Default upstream was 60s. 30s gives snappier state updates without hammering the API.
DEFAULT_SCAN_INTERVAL = 30
MIN_SCAN_INTERVAL = 10

# External temperature sensor override.
# Set to an HA sensor entity_id to show a room sensor's reading as current_temperature
# instead of the AC's built-in internal sensor.
# Leave as "" to use the AC's own sensor (upstream default).
EXTERNAL_TEMP_SENSOR = "sensor.family_room_average_temperature"

# Unit of the external sensor above: "F" for Fahrenheit, "C" for Celsius.
# The TCL climate entity internally uses Celsius, so if your sensor reports
# in Fahrenheit (most US Zigbee/ESPHome sensors) set this to "F" and the
# value will be automatically converted before being stored.
EXTERNAL_TEMP_SENSOR_UNIT = "F"
