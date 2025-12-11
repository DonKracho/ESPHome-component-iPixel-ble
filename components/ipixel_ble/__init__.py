import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display, light, ble_client
from esphome.const import CONF_ID
from esphome.const import __version__ as ESPHOME_VERSION

CODEOWNERS = ["@donkracho"]

CONF_IPIXEL_BLE = "ipixel_ble"

ipixel_ble_ns = cg.esphome_ns.namespace("ipixel_ble")
IPixelBLE = ipixel_ble_ns.class_("IPixelBLE", cg.Component, display.DisplayBuffer, light.LightOutput, ble_client.BLEClientNode)

CONFIG_SCHEMA = (
    cv.Schema({cv.GenerateID(): cv.declare_id(IPixelBLE)})
    .extend(cv.COMPONENT_SCHEMA)
    .extend(ble_client.BLE_CLIENT_SCHEMA)
)

async def to_code(config):
    if cv.Version.parse(ESPHOME_VERSION) < cv.Version.parse("2025.11.0"):
        raise ValueError('Use at leat esphome Version 2025.11.0.')
    
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await ble_client.register_ble_node(var, config)
