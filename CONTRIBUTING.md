# Contributing

Submit a pull request to add a new board, display, or peripheral.

## Requirements

1. Follow the structure in `TEMPLATE.md`
2. One `.md` file per component in the correct directory (`boards/`, `displays/`, `sensors/`, etc.) -- create a new directory if none fits
3. Include the source image link (manufacturer pinout diagram URL) at the top of the file
4. ASCII diagrams must match the physical layout shown in the source image
5. Do not commit images to the repo

## Checklist

- [ ] Source image link included (e.g. `Source image: https://...`)
- [ ] Follows `TEMPLATE.md` structure
- [ ] ASCII pinout matches source image
- [ ] USB north for boards, pins at top for peripherals
- [ ] Position notation matches `WIRING_FORMAT.md` (L1-L7, R1-R7, etc.)
- [ ] Bus defaults listed
- [ ] Variant differences noted if applicable
