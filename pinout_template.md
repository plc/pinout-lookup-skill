# Pinout Template

Structure for adding new pinout files.

- USB port always faces NORTH in board diagrams
- Pin headers at TOP of peripheral diagrams

## File Naming

- Lowercase, dashes instead of underscores or spaces
- Include key identifying info: `<model>-<variant>.md` or `<model>-<size>-<interface>.md`
- Examples: `xiao-esp32s3.md`, `ssd1306-096-i2c.md`, `bme280-i2c.md`

## Board (`boards/`)

```markdown
# <Board Name>

Source: <manufacturer wiki URL>

## Front (USB North)

<ASCII pinout diagram>
- Left pins: labels read right-to-left (outermost function first, pin name closest to board)
- Right pins: labels read left-to-right (pin name closest to board, outermost function last)
- Bottom pads below board outline if present

## Back (USB North, board flipped)

<ASCII diagram of back-only pads>

## Legend

- Key for diagram symbols ([R], [B], [ANT], etc.)
- LED pins and behavior
- Voltage levels
- Regulator current limit

## Bus Defaults

- I2C: SDA=??, SCL=??
- SPI: SCK=??, MISO=??, MOSI=??
- UART: TX=??, RX=??

## <Variant> Variant (if applicable)

- Pins used internally by the variant (not on headers)

## <Board-specific sections as needed>

- Battery ADC, pin numbering quirks, reserved GPIOs, etc.
```

## Peripheral (`displays/`, `sensors/`, etc.)

```markdown
# <Component Name>

Source: <manufacturer product page or datasheet URL>

<Resolution, interface, driver IC, voltage range. One line.>

## Pinout (<orientation note>)

<ASCII diagram showing pin header and component outline>

## Pin Description

- <pin> -- <function>

## <Interface details>

- Address, mode, frequency, etc.
```

## How to Populate

1. Get the pinout from the manufacturer page or product listing images
2. Read the images to get exact pin order and labels
3. Build ASCII art matching the physical layout
