# Adafruit Metro ESP32-S3

Product ID: 5500

Sources:
- https://www.adafruit.com/product/5500
- https://learn.adafruit.com/adafruit-metro-esp32-s3/pinouts
- https://github.com/espressif/arduino-esp32/blob/master/variants/adafruit_metro_esp32s3/pins_arduino.h

## Pinout (USB North, Arduino Uno R3 form factor)

```
           +-------USB-C-------+
           |  [NEOPIXEL] [RST] |
           |                   |
           |   METRO ESP32-S3  |
           |                   |
     L1  TX  D0  GPIO40  o-----+-----o  NC           R1
     L2  RX  D1  GPIO41  o-----------o  IOREF        R2
     L3      D2  GPIO2   o-----------o  RST          R3
     L4      D3  GPIO3   o-----------o  3.3V         R4
     L5      D4  GPIO4   o-----------o  5V           R5
     L6      D5  GPIO5   o-----------o  GND          R6
     L7      D6  GPIO6   o-----------o  GND          R7
     L8      D7  GPIO7   o-----------o  VIN          R8
                         |           |
     L9      D8  GPIO8   o-----+ +---o  A0  GPIO14   R9
     L10     D9  GPIO9   o-----| |---o  A1  GPIO15   R10
     L11     D10 GPIO10  o-----| |---o  A2  GPIO16   R11
     L12     D11 GPIO11  o-----| |---o  A3  GPIO17   R12
     L13     D12 GPIO12  o-----| |---o  A4  GPIO18   R13
     L14 LED D13 GPIO13  o-----| |---o  A5  GPIO1    R14
     L15         GND     o-----+ +---+
     L16         AREF    o---------+
     L17 SDA     GPIO47  o---------+
     L18 SCL     GPIO48  o---------+
                         |         |
                         | [QT] QT |
                         +---------+
```

## Legend

- [NEOPIXEL] RGB LED on GPIO46
- [RST] Reset button
- [QT] STEMMA QT connectors (I2C with 10k pullups, SDA=GPIO47, SCL=GPIO48)
- LED: Red LED on GPIO13 (shared with D13)
- NC: Not connected
- IOREF: Output reference voltage (3.3V)
- VIN: Battery/external power input (3.5-6V)
- 3.3V logic, NOT 5V tolerant
- 3.3V regulator: 400mA max
- 5V rail: USB-powered only (not available when running on battery)

## Bus Defaults

- I2C: SDA=GPIO47 (L17), SCL=GPIO48 (L18)
- SPI: SCK=D13/GPIO13 (L14), MISO=D12/GPIO12 (L13), MOSI=D11/GPIO11 (L12)
  - Note: These are NOT the default ESP32-S3 SPI pins. Use explicit pin configuration.
- UART: TX=D0/GPIO40 (L1), RX=D1/GPIO41 (L2) -- Serial1; Serial0=USB CDC

## Additional Features

- MicroSD card SPI: SCK=GPIO39, MOSI=GPIO42, MISO=GPIO21, CS=GPIO45
  - This is the ESP32-S3 native SPI bus (FSPI)
  - Different from the Arduino header SPI pins (D11-D13)
- Battery monitor: MAX17048 on I2C at address 0x36
- USB-C: Native USB support via USB CDC
- LiPo charging: Built-in charger for single-cell LiPo batteries
- STEMMA QT: Shares I2C bus with header (GPIO47/GPIO48)

## Notes

When using SPI devices on the Arduino header (D11-D13), you must explicitly configure the pins via the GPIO matrix. The ESP32-S3 native SPI bus is routed to the SD card slot, not the header.

Example for Arduino framework:
```cpp
SPI.begin(13, 12, 11);  // SCK, MISO, MOSI
```
