# Hosyond 3.5" IPS Capacitive Touch Display (ST7796U)

Source: https://www.amazon.com/Hosyond-320x480-Capacitive-ST7796U-Mega2560/dp/B0CMD7Y55M

320x480 pixels, IPS display, SPI interface (ST7796U driver) + I2C capacitive touch (FT6336U controller). 3.3V operation. Includes onboard SD card slot.

Verified against reference image and physical module in sticker-dispenser project (git log 330c359, 42a8082).

## Pinout (display facing you, pins at top)

```
  +-----------------------------------+
  | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 |
  | o  o  o  o  o  o  o  o  o  o  o  o  o  o |
  |                                         |
  |                                         |
  |                                         |
  |          3.5" IPS Display               |
  |          320 x 480 pixels               |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |  (O)                              (O)   |
  +-----------------------------------+
```

14-pin header, pins numbered 1-14 left to right.

## Pin Description

| # | Label | Function |
|---|-------|----------|
| 1 | VCC | Power, 3.3V |
| 2 | GND | Ground |
| 3 | LCD_CS | LCD chip select (active low) |
| 4 | LCD_RST | LCD reset (active low) |
| 5 | LCD_RS (DC) | Data/Command select |
| 6 | SDI (MOSI) | SPI data in |
| 7 | SCK | SPI clock |
| 8 | LED | Backlight, 3.3V |
| 9 | SDO (MISO) | SPI data out |
| 10 | CTP_SCL | Touch I2C clock |
| 11 | CTP_RST | Touch reset |
| 12 | CTP_SDA | Touch I2C data |
| 13 | CTP_INT | Touch interrupt (active low) |
| 14 | SD_CS | SD card chip select (active low, optional) |

## SPI Interface (LCD)

Pins 1-9 provide the SPI interface for the ST7796U LCD driver.

**Important:** This display uses a 4-wire SPI interface. On many boards (e.g., ESP32), the default SPI bus may be on different pins. Explicit pin configuration is required in your sketch.

Standard SPI signals:
- SCK (pin 7) -- SPI clock
- MOSI/SDI (pin 6) -- Master Out, Slave In
- MISO/SDO (pin 9) -- Master In, Slave Out
- LCD_CS (pin 3) -- Chip select (active low)

Additional control:
- LCD_RS/DC (pin 5) -- Data/Command select
- LCD_RST (pin 4) -- Hardware reset (active low)
- LED (pin 8) -- Backlight control (3.3V = on, can use PWM for dimming)

Driver IC: ST7796U
Resolution: 320x480 pixels
Colors: 16.7M (262K)

## I2C Interface (Capacitive Touch)

Pins 10-13 provide the I2C interface for the FT6336U capacitive touch controller.

- CTP_SDA (pin 12) -- I2C data
- CTP_SCL (pin 10) -- I2C clock
- CTP_INT (pin 13) -- Touch interrupt (active low, optional)
- CTP_RST (pin 11) -- Touch reset (optional)

**I2C Address:** 0x38 (FT6336U)

The touch controller supports up to 2 simultaneous touch points.

## SD Card Interface

Pin 14 (SD_CS) provides chip select for the optional onboard micro SD card slot. The SD card shares the same SPI bus as the LCD (pins 6, 7, 9).

If you don't use the SD card, you can leave pin 14 disconnected or tie it high.

## Wiring to Metro ESP32-S3

Hosyond ST7796U: pins 1-14 left to right, display facing you.
Metro ESP32-S3: L1-L18 left, R1-R14 right, top to bottom, USB at top.

| Hosyond ST7796U | #  | Metro ESP32-S3 | #   |
|-----------------|----|----------------|-----|
| VCC             | 1  | 3.3V           | R4  |
| GND             | 2  | GND            | R6  |
| LCD_CS          | 3  | D10 (GPIO10)   | L11 |
| LCD_RST         | 4  | D8 (GPIO8)     | L9  |
| LCD_RS (DC)     | 5  | D9 (GPIO9)     | L10 |
| SDI (MOSI)      | 6  | D11 (GPIO11)   | L12 |
| SCK             | 7  | D13 (GPIO13)   | L14 |
| LED             | 8  | 3.3V           | R4  |
| SDO (MISO)      | 9  | D12 (GPIO12)   | L13 |
| CTP_SCL         | 10 | SCL (GPIO48)   | L18 |
| CTP_RST         | 11 | D6 (GPIO6)     | L7  |
| CTP_SDA         | 12 | SDA (GPIO47)   | L17 |
| CTP_INT         | 13 | D7 (GPIO7)     | L8  |
| SD_CS           | 14 | (unassigned)   | --  |

## Notes

- This module includes an onboard level-shifting circuit and can be used with both 3.3V and 5V MCUs (VCC can be 3.3V or 5V).
- Backlight current: ~95mA at full brightness.
- For Arduino/ESP32 projects, use TFT_eSPI or LovyanGFX libraries with ST7796 driver.
- Touch library: FT6336U-compatible I2C touch library (often works with FT6206/FT6236 libraries).
