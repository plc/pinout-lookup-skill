# HC-SR501 PIR Motion Sensor

Source: TODO

Passive infrared motion detector. 5-20V input, 3.3V logic output. Adjustable sensitivity and trigger duration.

## Pinout (lens dome away, pins facing you)

```
                +------------------+
                |                  |
                |   [Lens Dome]    |
                |                  |
                |      ######      |
                |     ########     |
                |    ##########    |
                |                  |
                |  [IC]  [IC]      |
                |                  |
                |   (Sens) (Time)  |
                |    Pot    Pot    |
                |                  |
                |     [Jumper]     |
                |    H / L         |
                |                  |
                +------------------+
                |  o    o    o     |
                | GND  OUT  VCC    |
                +------------------+
                  1    2    3
```

## Pin Description

- Pin 1 (GND) -- Ground
- Pin 2 (OUT) -- Digital output. HIGH when motion detected, 3.3V logic level
- Pin 3 (VCC) -- Power input, 5-20V DC (typically 5V)

## Configuration

### Jumper (H/L)
- H (Repeat Trigger) -- Output stays HIGH while motion continues
- L (Single Trigger) -- One pulse per motion detection event

### Potentiometers
- Left (Sensitivity) -- Adjust detection range (up to 7m)
- Right (Time Delay) -- Adjust output pulse duration (approx 0.3s to 5min)

## Detection Characteristics

- Detection angle: ~120 degrees
- Detection range: up to 7 meters (adjustable)
- Output voltage: 3.3V logic (safe for 3.3V microcontrollers even with 5V power input)
- Recommended power: 5V DC

## Notes

Module requires 5V power for reliable operation. The output signal is 3.3V logic level regardless of input voltage, making it compatible with both 3.3V and 5V microcontrollers.

Reference verified from physical module photo showing component layout and pin labels.
