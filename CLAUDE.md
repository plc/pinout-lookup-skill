# CLAUDE.md -- for developing this skill

This file is for Claude sessions working ON the skill itself (adding components, editing skill.md, fixing templates). It is NOT loaded by the skill at runtime -- users install skill.md directly into their Claude Code skills directory.

## Repo purpose

This repo stores component pinout data (boards, displays, sensors) and a Claude Code skill file (`skill.md`) that fetches that data from GitHub to generate wiring tables.

## How the skill is distributed

Users install with:
```bash
mkdir -p ~/.claude/skills/pinout-lookup
curl -sL https://raw.githubusercontent.com/plc/pcb-wiring-skill/main/skill.md \
  > ~/.claude/skills/pinout-lookup/SKILL.md
```

The skill fetches pinout files from this repo at runtime via raw GitHub URLs. There is no local clone. Changes to component files in this repo are immediately available to all users.

Changes to `skill.md` itself require users to re-run the curl command.

## Key files

- `skill.md` -- the skill definition. Has YAML frontmatter for Claude Code discovery. This is what users install.
- `WIRING_FORMAT.md` -- canonical wiring table format (also inlined in skill.md, keep both in sync)
- `pinout_template.md` -- template for new component files
- `CONTRIBUTING.md` -- contribution guidelines
- `boards/`, `displays/` -- component pinout files

## Gotchas learned the hard way

### Do not hardcode paths in skill.md

The skill runs on other people's machines. Early versions used `~/Documents/pcb-wiring-skill/` everywhere which only worked for one person. The skill must fetch from GitHub, not reference local paths.

### Do not put wiring tables in pinout files

Earlier versions had the peripheral template include a "Wiring to <Board>" section for every board. This doesn't scale -- every new board means updating every peripheral file. The skill computes wiring at runtime from the board's bus defaults.

### The wiring format in WIRING_FORMAT.md is also inlined in skill.md

When the skill fetches from GitHub, an extra fetch for the format spec is wasteful. The wiring table format is inlined in skill.md under "### Wiring Table Format". If you change WIRING_FORMAT.md, update skill.md too.

### Pinout files should describe components, not wiring

A pinout file's job is: what pins does this component have, where are they physically, what do they do. Wiring (which pin connects to which) is the skill's job at runtime.

### Source URLs can be TODO

Not every component has an obvious source URL. The SSD1306 is a generic module sold by dozens of manufacturers. `Source: TODO` is acceptable per CONTRIBUTING.md.

### The skill file needs YAML frontmatter

Claude Code discovers skills by reading `SKILL.md` files in `~/.claude/skills/`. The frontmatter `name` field becomes the `/slash-command`, and `description` is used for auto-invocation matching. Without frontmatter the skill won't load.

### Do not assume gh CLI is available

The skill uses `curl` for fetching pinout data (works everywhere). `gh` is optional and used for creating issues and PRs when available. If `gh` is missing, the skill gives the user a direct GitHub link instead.

### Position notation is physical, not logical

L1-L7 and R1-R7 refer to physical pin positions on the board (left side, right side, top to bottom with USB at top). They are not GPIO numbers or Arduino pin numbers. This is the whole point of the skill -- telling someone "connect to L6" is unambiguous when they're looking at the board.

## Adding a new component

1. Create a `.md` file in the right directory (`boards/`, `displays/`, `sensors/`)
2. Follow `pinout_template.md`
3. File naming: lowercase, dashes, include key identifiers (e.g. `ssd1306-096-i2c.md`)
4. Include `Source: <url>` or `Source: TODO`
5. Board files need Bus Defaults section (I2C, SPI, UART pin assignments)
6. Commit, push, and it's live immediately for all skill users
