# tinyclock

A simple, lightweight Terminal UI (TUI) digital clock written in Python.

> **Note:** This project is currently a **Work In Progress (WIP)**. It is an experimental weekend project, not yet fully production-ready, and may still have some rendering bugs or edge cases across different terminal emulators. Contributions and feedback are welcome!

## Features
- **Alternate Screen Buffer**: Uses the built-in `curses` library to render the clock in an alternate screen, keeping your terminal history clean.
- **Custom Block Font**: Uses a minimal 5x3 ASCII/Unicode block matrix to display the time.
- **Configurable Colors**: Supports changing the text color using basic ANSI sequences.

## Installation

You can run `tinyclock` directly as a standalone Python script.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/USERNAME/tinyclock.git
   cd tinyclock
   ```

2. **Make it executable:**
   ```bash
   chmod +x tinyclock.py
   ```

3. **Install globally (optional):**
   ```bash
   sudo mv tinyclock.py /usr/local/bin/tinyclock
   ```

## Usage

Simply run the clock using the command:
```bash
tinyclock
```

### Options

**Custom Colors:**
Change the clock's color index (0-7) using the `-c` or `--color` flag:
- `0`: Default Terminal Foreground
- `1`: Red
- `2`: Green
- `3`: Yellow
- `4`: Blue
- `5`: Magenta
- `6`: Cyan
- `7`: White

*Example: Run the clock in cyan:*
```bash
tinyclock -c 6
```

### Exiting
Press `q` or `Ctrl+C` to exit the clock and restore your terminal.

## License
Published under the MIT License. See [LICENSE](LICENSE) for more details.
