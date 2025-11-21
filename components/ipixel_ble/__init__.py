import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import ble_client, sensor
from esphome.const import CONF_ID

CODEOWNERS = ["@donkracho"]
DEPENDENCIES = ["ble_client", "output"]

CONF_IPIXEL_BLE = "ipixel_ble"
CONF_WIDTH = "display_width"
CONF_HEIGHT = "display_height"

ipixel_ble_ns = cg.esphome_ns.namespace("ipixel_ble")
IPixelBLE = ipixel_ble_ns.class_("IPixelBLE", sensor.Sensor, cg.Component, ble_client.BLEClientNode)

CONFIG_SCHEMA = cv.All(
    cv.Schema({
        cv.GenerateID(): cv.declare_id(IPixelBLE),
        cv.Optional(CONF_WIDTH,  default = 32): cv.All(cv.uint8_t, cv.Range(min = 16, max = 256)),
        cv.Optional(CONF_HEIGHT, default = 32): cv.All(cv.uint8_t, cv.Range(min = 16, max = 256)),
    })
    .extend(cv.COMPONENT_SCHEMA)
    .extend(ble_client.BLE_CLIENT_SCHEMA),
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await ble_client.register_ble_node(var, config)

    cg.add(var.set_display_width(config[CONF_WIDTH])),
    cg.add(var.set_display_height(config[CONF_HEIGHT])),
