---
name: pinout-lookup
description: |
  Look up component pinouts and generate wiring tables for PCB projects.
  Use when the user asks how to wire boards, displays, sensors, or other
  electronic components together. Also handles missing components (issue
  creation or contribution) and pinout corrections.
allowed-tools:
  - Read
  - Glob
  - Grep
  - Edit
  - Write
  - Bash
---

# Pinout Lookup Skill

Look up component pinouts and generate wiring tables for PCB projects.

This skill file lives in the root of the `pcb-wiring-skill` repo and is symlinked from `~/.claude/skills/pinout-lookup/SKILL.md`. To find the repo root, resolve the symlink: `readlink ~/.claude/skills/pinout-lookup/SKILL.md` and take the parent directory. All paths below are relative to that repo root.

## Wiring Query

When the user asks how to wire two components together:

1. Resolve the repo root (see above)
2. Search `boards/`, `displays/`, and any other directories in the repo for `.md` files matching the requested components (match on filename or H1 heading, case-insensitive)
3. Read the matched files to get pinouts and bus defaults
4. Read `WIRING_FORMAT.md` in the repo root for the canonical output format
5. If the display/peripheral file already has a "Wiring to <board>" section for the requested board, use those pin assignments
6. Otherwise, use the board's "Bus Defaults" section (I2C, SPI, UART pin assignments) to determine correct wiring based on the peripheral's interface type
7. Output a wiring table following `WIRING_FORMAT.md` -- peripheral on left, board on right, table only, no ASCII pinout diagrams unless the user asks
8. Do not modify files in the pcb-wiring-skill repo. Only write to the user's project `WIRING.md`

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

1. Read `TEMPLATE.md` and `CONTRIBUTING.md` from the repo root
2. Walk the user through creating the `.md` file following those guidelines
3. When the file is ready:
   - Create a branch: `git checkout -b add-<component-name>`
   - Commit the file
   - Push and open a PR with `gh pr create`

## Incorrect Pinout

If the user spots an error in an existing component file (wrong pin, wrong position, bad wiring):

1. Ask the user what's wrong and what the correct value should be
2. Open a PR proposing the fix on `plc/pcb-wiring-skill`:
   - Create a branch: `git checkout -b fix-<component-name>`
   - Make the correction
   - Commit with a message explaining what was wrong
   - Push and open a PR with `gh pr create`, describing the error and the source of the correction in the body
