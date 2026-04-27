# Templates

Structure for adding new files. USB port always faces NORTH in board diagrams.
Display/peripheral pins at TOP unless otherwise noted.

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

## Display / Peripheral (`displays/`)

```markdown
# <Display Name>

<Resolution, interface, driver IC, voltage range. One line.>

## Pinout (<orientation note>)

<ASCII diagram showing pin header and display outline>

## Pin Description

- <pin> -- <function>

## <Interface details>

- Address, mode, frequency, etc.

## Wiring to <Board Name>

<ASCII wiring table for each board in boards/>
```

## How to Populate

1. Get the pinout from the manufacturer page or product listing images
2. Read the images to get exact pin order and labels
3. Build ASCII art matching the physical layout
4. For displays/peripherals, add a wiring section for each board in `boards/`
