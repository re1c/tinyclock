# tinyclock

A production-ready, highly optimized Terminal UI (TUI) digital clock. Built purely with Python's built-in `curses` library to ensure a pristine terminal history and zero flicker during window resizes.

## Features
- **Alternate Screen Buffer**: Uses curses to render in an alternate screen, ensuring your terminal history remains perfectly clean after exit.
- **Zero-Flicker Rendering**: Implements differential redraws via curses. It beautifully adapts to dynamic window resizing and split-screen operations without screen tearing or visual artifacts.
- **Ultra Lightweight**: Polling loop specifically tailored to effectively sleep and consume near 0% CPU on modern hardware.
- **The Font Matrix**: A unique, mathematical 5x3 semi-block matrix font (`▀`, `█`, `▄`) creates visually striking digital characters that maintain a perfectly flat baseline.
- **Configurability**: Toggleable 12-hour / 24-hour formats and fully customizable text colors using ANSI sequences.

## Installation

You can install `tinyclock` directly from source as a standalone executable.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/USERNAME/tinyclock.git
   cd tinyclock
   ```

2. **Make it executable:**
   ```bash
   chmod +x tinyclock.py
   ```

3. **Install globally (optional but recommended):**
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

Change the clock's active color index (0-7) using the `-c` or `--color` flag:

- `0`: Default Terminal Foreground

- `1`: Red

- `2`: Green

- `3`: Yellow

- `4`: Blue

- `5`: Magenta

- `6`: Cyan

- `7`: White



*Example: Run the clock in green:*

```bash

tinyclock -c 2

```

### Exiting
Press `q` or `Ctrl+C` to cleanly exit the clock. Your terminal will be immediately restored to its exact previous state.

## License
Published under the MIT License. See [LICENSE](LICENSE) for more details.
