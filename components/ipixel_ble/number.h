#pragma once

#include "esphome/components/number/number.h"
#include "esphome/core/component.h"

#include "ipixel_ble.h"

namespace esphome {
namespace ipixel_ble {

class ClockStyleNumber : public number::Number, public Parented<IPixelBLE> {
 public:
  ClockStyleNumber() = default;

 protected:
  void control(float value) override { this->parent_->on_clock_style_number(value); }
};

class LambdaSlotNumber : public number::Number, public Parented<IPixelBLE> {
 public:
  LambdaSlotNumber() = default;

 protected:
  void control(float value) override { this->parent_->on_lambda_slot_number(value); }
};

class AnimationModeNumber : public number::Number, public Parented<IPixelBLE> {
 public:
  AnimationModeNumber() = default;

 protected:
  void control(float value) override { this->parent_->on_animation_mode_number(value); }
};

class AnimationSpeedNumber : public number::Number, public Parented<IPixelBLE> {
 public:
  AnimationSpeedNumber() = default;

 protected:
  void control(float value) override { this->parent_->on_animation_speed_number(value); }
};

class FontFlagNumber : public number::Number, public Parented<IPixelBLE> {
 public:
  FontFlagNumber() = default;

 protected:
  void control(float value) override { this->parent_->on_font_flag_number(value); }
};

class TextModeNumber : public number::Number, public Parented<IPixelBLE> {
 public:
  TextModeNumber() = default;

 protected:
  void control(float value) override { this->parent_->on_text_mode_number(value); }
};

}  // namespace ipixel_ble
}  // namespace esphome
