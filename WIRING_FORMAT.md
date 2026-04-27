# Wiring Output Format

When showing how to wire two components together, use this format.
Do not show full ASCII pinout diagrams unless explicitly asked.

## Format

```
<Left component>: <position notation explanation>
<Right component>: <position notation explanation>

| <Left Name> | #  | <Right Name> | #  |
|-------------|----|--------------|----|
| <pin>       | <pos> | <pin>     | <pos> |
```

## Position Notation

- **Boards (XIAO etc):** L1-L7 left side, R1-R7 right side, top to bottom, USB at top. BL/BR for bottom pads.
- **Pin headers (OLEDs, sensors etc):** 1-N left to right, component facing you.

## Example

```
OLED: pins 1-4 left to right, display facing you.
XIAO: L1-L7 left, R1-R7 right, top to bottom, USB at top.

| OLED | #  | XIAO ESP32-S3 | #  |
|------|----|---------------|----|
| GND  | 1  | GND           | R2 |
| VCC  | 2  | 3V3           | R3 |
| SCL  | 3  | D5 (GPIO6)    | L6 |
| SDA  | 4  | D4 (GPIO5)    | L5 |
```
