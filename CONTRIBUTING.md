# Contributing

Submit a pull request to add a new board or peripheral.

## Requirements

1. Follow the structure in `pinout_template.md`
2. One `.md` file per component in the correct directory (`boards/`, `displays/`, `sensors/`, etc.) -- create a new directory if none fits
3. Include a source link at the top of the file (manufacturer pinout diagram, datasheet, or product page URL). Use `Source: TODO` if you can't find one
4. ASCII diagrams must match the physical layout shown in the source
5. Do not commit images to the repo

## Checklist

- [ ] Source link included (e.g. `Source: https://...` or `Source: TODO`)
- [ ] Follows `pinout_template.md` structure
- [ ] ASCII pinout matches source
- [ ] USB north for boards, pin header at top of diagram for peripherals
- [ ] Position notation matches `WIRING_FORMAT.md` (L1-L7, R1-R7, etc.)
- [ ] Variant differences noted if applicable
