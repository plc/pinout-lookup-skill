# Pinout Lookup Skill

A Claude Code skill for looking up component pinouts and generating wiring tables.

## Supported Components

### Boards

- XIAO ESP32-S3
- XIAO nRF52840

### Displays

- SSD1306 0.96" OLED (I2C)

## Installation

Clone the repo anywhere:

```bash
git clone https://github.com/plc/pcb-wiring-skill.git
```

Symlink the skill file into Claude Code's skills directory:

```bash
mkdir -p ~/.claude/skills/pinout-lookup
ln -s /absolute/path/to/pcb-wiring-skill/skill.md ~/.claude/skills/pinout-lookup/SKILL.md
```

Use the absolute path to wherever you cloned the repo.

## Usage

Invoke with `/pinout-lookup` or just ask Claude a wiring question:

```
How do I wire an SSD1306 OLED to a XIAO ESP32-S3?
```

The skill outputs a wiring table with position notation so you know exactly which physical pin to use:

```
SSD1306: pins 1-4 left to right, display facing you.
XIAO: L1-L7 left, R1-R7 right, top to bottom, USB at top.

| SSD1306 | #  | XIAO ESP32-S3 | #  |
|---------|----|---------------|----|
| GND     | 1  | GND           | R2 |
| VCC     | 2  | 3V3           | R3 |
| SCL     | 3  | D5 (GPIO6)    | L6 |
| SDA     | 4  | D4 (GPIO5)    | L5 |
```

The wiring is saved to a `WIRING.md` in your current project directory, along with a components list.

### Missing components

If a component isn't on file, the skill will offer to:
- Open a GitHub issue requesting it
- Guide you through contributing it yourself via PR

### Incorrect pinouts

If you spot an error, tell Claude what's wrong and it will open a PR to fix it.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Use [pinout_template.md](pinout_template.md) for the file structure and [WIRING_FORMAT.md](WIRING_FORMAT.md) for the wiring table format.

## File Structure

```
boards/           Board pinouts
displays/         Display/peripheral pinouts
skill.md          Skill definition (symlink target)
WIRING_FORMAT.md  Canonical wiring table format
pinout_template.md       Template for new component files
CONTRIBUTING.md   Contribution guidelines
```
