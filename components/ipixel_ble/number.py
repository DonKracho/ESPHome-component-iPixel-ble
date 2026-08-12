import esphome.codegen as cg
from esphome.components import number
import esphome.config_validation as cv

from . import CONF_IPIXEL_BLE, IPixelBLE, ipixel_ble_ns

AUTO_LOAD = ["number"]

CONF_ANIMATION_MODE = "animation_mode"
AnimationModeNumber = ipixel_ble_ns.class_("AnimationModeNumber", number.Number)

CONF_ANIMATION_SPEED = "animation_speed"
AnimationSpeedNumber = ipixel_ble_ns.class_("AnimationSpeedNumber", number.Number)

CONF_CLOCK_STYLE = "clock_style"
ClockStyleNumber = ipixel_ble_ns.class_("ClockStyleNumber", number.Number)

CONF_FONT_FLAG = "font_flag"
FontFlagNumber = ipixel_ble_ns.class_("FontFlagNumber", number.Number)

CONF_LAMBDA_SLOT = "lambda_slot"
SlotNumberNumber = ipixel_ble_ns.class_("LambdaSlotNumber", number.Number)

CONF_TEXT_MODE = "text_mode"
TextModeNumber = ipixel_ble_ns.class_("TextModeNumber", number.Number)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_IPIXEL_BLE): cv.use_id(IPixelBLE),
        cv.Required(CONF_CLOCK_STYLE): number.number_schema(ClockStyleNumber),
        cv.Required(CONF_LAMBDA_SLOT): number.number_schema(SlotNumberNumber),
        cv.Required(CONF_ANIMATION_MODE): number.number_schema(AnimationModeNumber),
        cv.Required(CONF_ANIMATION_SPEED): number.number_schema(AnimationSpeedNumber),
        cv.Required(CONF_FONT_FLAG): number.number_schema(FontFlagNumber),
        cv.Required(CONF_TEXT_MODE): number.number_schema(TextModeNumber),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_IPIXEL_BLE])

    if conf := config.get(CONF_CLOCK_STYLE):
        b = await number.new_number(conf, min_value=1, max_value=9, step=1)
        await cg.register_parented(b, parent)
        cg.add(getattr(parent, f"set_{CONF_CLOCK_STYLE}_number")(b))
    if conf := config.get(CONF_LAMBDA_SLOT):
        b = await number.new_number(conf, min_value=0, max_value=15, step=1)
        await cg.register_parented(b, parent)
        cg.add(getattr(parent, f"set_{CONF_LAMBDA_SLOT}_number")(b))
    if conf := config.get(CONF_ANIMATION_MODE):
        b = await number.new_number(conf, min_value=0, max_value=6, step=1)
        await cg.register_parented(b, parent)
        cg.add(getattr(parent, f"set_{CONF_ANIMATION_MODE}_number")(b))
    if conf := config.get(CONF_ANIMATION_SPEED):
        b = await number.new_number(conf, min_value=0, max_value=100, step=1)
        await cg.register_parented(b, parent)
        cg.add(getattr(parent, f"set_{CONF_ANIMATION_SPEED}_number")(b))
    if conf := config.get(CONF_FONT_FLAG):
        b = await number.new_number(conf, min_value=0, max_value=4, step=1)
        await cg.register_parented(b, parent)
        cg.add(getattr(parent, f"set_{CONF_FONT_FLAG}_number")(b))
    if conf := config.get(CONF_TEXT_MODE):
        b = await number.new_number(conf, min_value=0, max_value=9, step=1)
        await cg.register_parented(b, parent)
        cg.add(getattr(parent, f"set_{CONF_TEXT_MODE}_number")(b))
