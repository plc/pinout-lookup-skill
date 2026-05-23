---
name: pinout-lookup
version: 1
description: |
  Look up component pinouts and generate wiring tables for PCB projects.
  Use when the user asks how to wire boards, displays, sensors, or other
  electronic components together. Also handles missing components (issue
  creation or contribution) and pinout corrections.
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - WebFetch
  - WebSearch
---

# Pinout Lookup Skill

Look up component pinouts and generate wiring tables for PCB projects. Pinout data is stored in the GitHub repo `plc/pinout-lookup-skill`.

## Version Check

On first use in a session, fetch `https://raw.githubusercontent.com/plc/pinout-lookup-skill/main/VERSION` using WebFetch. Compare the number in that file to the `version:` field in this skill's frontmatter. If the remote version is higher, tell the user:

> A newer version of the pinout-lookup skill is available. Update with:
> ```
> curl -sL https://raw.githubusercontent.com/plc/pinout-lookup-skill/main/skill.md > ~/.claude/skills/pinout-lookup/SKILL.md
> ```

Then continue with the user's request normally.

## Fetching Pinout Data

Base URL: `https://raw.githubusercontent.com/plc/pinout-lookup-skill/main/`

- Read a file: use WebFetch with the raw URL (e.g. `https://raw.githubusercontent.com/plc/pinout-lookup-skill/main/boards/xiao-esp32s3.md`)
- List a directory: use Bash with `gh api repos/plc/pinout-lookup-skill/contents/boards --jq '.[].name'`

Component directories: `boards/`, `displays/`, `sensors/`, and any others present.

## Wiring Query

When the user asks how to wire two components together:

1. List the component directories in the repo and find `.md` files matching the requested components (match on filename, case-insensitive)
2. Fetch and read the matched files to get pinouts and bus defaults
3. Use the board's "Bus Defaults" section (I2C, SPI, UART pin assignments) to determine correct wiring based on the peripheral's interface type
4. Output a wiring table using the format below -- peripheral on left, board on right, table only, no ASCII pinout diagrams unless the user asks
5. Do not modify files in the `plc/pinout-lookup-skill` repo

### Wiring Table Format

```
<Peripheral name>: <position notation explanation>
<Board name>: <position notation explanation>

| <Peripheral> | #  | <Board> | #  |
|---------------|----|---------|------|
| <pin>         | <pos> | <pin> | <pos> |
```

Position notation:
- **Boards (XIAO etc):** L1-L7 left side, R1-R7 right side, top to bottom, USB at top. BL/BR for bottom pads.
- **Pin headers (peripherals):** 1-N left to right, component facing you.

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

<wiring table>
```

If `WIRING.md` already exists, append the new wiring section and update the components table. Do not duplicate entries.

## Component Not Found

When a requested component has no `.md` file in the repo:

1. Tell the user the component is not on file yet
2. Ask: "I can request this component be added (open an issue), or if you have a datasheet/pinout diagram I can contribute it now (open a PR). Which would you prefer?"

### Requesting a component (issue)

Open an issue to request pinout data for a specific device. This is the right path when no verified pinout source is available -- a request issue is always better than a PR with guessed pin positions. Use `gh issue create -R plc/pinout-lookup-skill` if available, otherwise give the user a link to `https://github.com/plc/pinout-lookup-skill/issues/new`.

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

  ## Important
  Pin layouts must come from a datasheet, manufacturer pinout diagram, or a clear photo of the physical board/module. Do not guess or infer pin positions -- incorrect pinouts cause hardware damage.
  ```

### Contributing a component (PR)

Open a PR to add a new pinout file. Only do this when a verified source is available.

1. Fetch `pinout_template.md` and `CONTRIBUTING.md` from the repo
2. Build the `.md` file following those guidelines, sourcing every pin label and position from the primary source
3. **Do not guess or generate pin positions from training data.** Every pin label and position must come from a datasheet, manufacturer diagram, or a photo of the physical board/module that the user provides or you fetch from a URL. If no source is available, stop and open an issue instead.
4. Open a PR with the new file. Include the source URL in the PR body. Use `gh` if available, otherwise guide the user to fork and submit manually

## Incorrect Pinout

If the user spots an error in an existing component file (wrong pin, wrong position, bad wiring):

1. Ask the user what's wrong and what the correct value should be
2. **If the correction can be verified** (user provides source, datasheet, or photo): open a PR proposing the fix. Include the error, the correction, and the source in the PR body. Use `gh` if available, otherwise guide the user to fork and submit manually.
3. **If the correction cannot be verified**: open an issue describing the reported error so someone with the physical board can confirm and fix it.
