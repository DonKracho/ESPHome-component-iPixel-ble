import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display
from esphome.const import CONF_LAMBDA, CONF_PAGES

from . import CONF_IPIXEL_BLE, IPixelBLE

DEPENDENCIES = ["ipixel_ble"]

CONF_WIDTH = "width"
CONF_HEIGHT = "height"

CONFIG_SCHEMA = cv.All (
    display.FULL_DISPLAY_SCHEMA.extend(
        {
            cv.GenerateID(CONF_IPIXEL_BLE): cv.use_id(IPixelBLE),
            cv.Optional(CONF_WIDTH,  default = 0): cv.All(cv.uint16_t, cv.Range(min = 0, max = 512)),
            cv.Optional(CONF_HEIGHT, default = 0): cv.All(cv.uint16_t, cv.Range(min = 0, max = 512)),
        }
    ),
    cv.has_at_most_one_key(CONF_PAGES, CONF_LAMBDA),
)


async def to_code(config):
    var = await cg.get_variable(config[CONF_IPIXEL_BLE])

    if CONF_LAMBDA in config:
        displayRef = display.DisplayRef
        lambda_ = await cg.process_lambda(
            config[CONF_LAMBDA], [(displayRef, "it")], return_type=cg.void
        )
        cg.add(var.set_writer(lambda_))

    # Set custom variables.
    if cfg := config.get(CONF_WIDTH):
        cg.add(var.set_display_width(cfg))
    if cfg := config.get(CONF_HEIGHT):
        cg.add(var.set_display_height(cfg))
