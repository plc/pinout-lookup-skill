# Pinout Lookup

Look up component pinouts and generate wiring tables for PCB projects.

## Wiring Query

When the user asks how to wire two components together:

1. Search `boards/`, `displays/`, and any other directories in this repo for `.md` files matching the requested components (match on filename or H1 heading, case-insensitive)
2. Read the matched files to get pinouts and bus defaults
3. Read `WIRING_FORMAT.md` for the canonical output format
4. If the display/peripheral file already has a "Wiring to <board>" section for the requested board, use those pin assignments
5. Otherwise, use the board's "Bus Defaults" section (I2C, SPI, UART pin assignments) to determine correct wiring based on the peripheral's interface type
6. Output a wiring table following `WIRING_FORMAT.md` -- peripheral on left, board on right, table only, no ASCII pinout diagrams unless the user asks
7. Do not modify files in the pcb-wiring-skill repo. Only write to the user's project `WIRING.md`

## Project Wiring File

After outputting a wiring table, save it to a `WIRING.md` file in the user's current project directory. This file is the single reference for all wiring in that project.

If `WIRING.md` does not exist yet, create it with this structure:

```markdown
# Wiring

## Components

| Component | Type | Interface |
|-----------|------|-----------|
| <name>    | board / display / sensor | I2C / SPI / UART (peripherals) or -- (boards) |

## <Peripheral> to <Board>

<wiring table from WIRING_FORMAT.md>
```

If `WIRING.md` already exists, append the new wiring section and update the components table. Do not duplicate entries.

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
3. When the file is ready:
   - Create a branch: `git checkout -b add-<component-name>`
   - Commit the file
   - Push and open a PR with `gh pr create`
