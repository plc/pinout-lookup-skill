# PCB Wiring Skill

Look up component pinouts and generate wiring tables for PCB projects.

## Wiring Query

When the user asks how to wire two components together:

1. Search `boards/`, `displays/`, `sensors/`, and any other directories in this repo for `.md` files matching the requested components (match on filename or heading)
2. Read the matched files to get pinouts and bus defaults
3. Read `WIRING_FORMAT.md` and output a wiring table in that exact format -- table only, no ASCII pinout diagrams unless the user asks for them
4. If the display/peripheral file already has a "Wiring to <board>" section, use those pin assignments directly
5. Otherwise, use the board's bus defaults (I2C, SPI, UART) to determine correct pin assignments

## Component Not Found

When a requested component has no `.md` file in the repo:

1. Tell the user the component is not on file yet
2. Ask: "Want me to open a GitHub issue requesting it, or would you like to contribute it yourself?"

### If the user wants an issue

Create an issue on `plc/pcb-wiring-skill` using `gh issue create`:

- **Title:** `Add <component type>: <component name>`
- **Labels:** `new-board`, `new-display`, or `new-sensor` (pick the appropriate one; create the label if it does not exist)
- **Body:**
  ```
  ## Component
  <name>

  ## Type
  board / display / sensor / other

  ## Manufacturer URL
  <url if known, otherwise "Unknown">
  ```

### If the user wants to contribute

1. Read `TEMPLATE.md` and `CONTRIBUTING.md`
2. Walk the user through creating the `.md` file following those guidelines
3. When the file is ready, open a PR on `plc/pcb-wiring-skill` with the new file
