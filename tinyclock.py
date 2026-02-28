#!/usr/bin/env python3
import argparse
import curses
import locale
import sys
from datetime import datetime

# Configure locale to properly support system default language names for date format
locale.setlocale(locale.LC_ALL, '')

# The Font Matrix
MINIMAL_FONT = {
    '0': ("█▀█", "█ █", "▀▀▀"), '1': (" ▀█", "  █", "  ▀"),
    '2': ("▀▀█", "█▀▀", "▀▀▀"), '3': ("▀▀█", "▀▀█", "▀▀▀"),
    '4': ("█ █", "▀▀█", "  ▀"), '5': ("█▀▀", "▀▀█", "▀▀▀"),
    '6': ("█▀▀", "█▀█", "▀▀▀"), '7': ("▀▀█", "  █", "  ▀"),
    '8': ("█▀█", "█▀█", "▀▀▀"), '9': ("█▀█", "▀▀█", "▀▀▀"),
    ':': (" ▄ ", " ▄ ", "   "), ' ': ("   ", "   ", "   ")
}

def draw_clock(stdscr, color):
    # Hide cursor and make getch non-blocking
    curses.curs_set(0)
    stdscr.nodelay(True)
    
    # 100ms timeout for getch() ensures fast responsiveness to resize and quit events
    # while sleeping effectively to maintain near 0% CPU consumption
    stdscr.timeout(100)

    # State tracking to minimize absolutely any redundant redrawing 
    # and achieve true mathematically minimal CPU usage
    last_time_str = ""
    last_date_str = ""
    last_h = 0
    last_w = 0
    force_redraw = True
    
    while True:
        try:
            ch = stdscr.getch()
            if ch == curses.KEY_RESIZE:
                curses.update_lines_cols()
                force_redraw = True
            elif ch in (ord('q'), ord('Q')):
                break
                
            now = datetime.now().astimezone()
            
            time_str = now.strftime("%H:%M:%S")
                
            date_str = now.strftime("%A, %d %B %Y")

            # Check for terminal dimension changes that bypassed KEY_RESIZE
            h, w = stdscr.getmaxyx()
            if h != last_h or w != last_w:
                last_h = h
                last_w = w
                force_redraw = True

            # Efficiency core: Only recalculate and redraw if something actively changed
            if time_str == last_time_str and date_str == last_date_str and not force_redraw:
                continue

            last_time_str = time_str
            last_date_str = date_str
            force_redraw = False
            
            # Construct ASCII representations
            clock_lines = ["", "", ""]
            for char in time_str:
                font_char = MINIMAL_FONT.get(char, MINIMAL_FONT[' '])
                for i in range(3):
                    clock_lines[i] += font_char[i] + " "
                    
            # Remove trailing space string
            for i in range(3):
                clock_lines[i] = clock_lines[i].rstrip()
                
            clock_width = len(clock_lines[0])
            clock_height = 3
            date_width = len(date_str)
            
            total_height = clock_height + 1 # +1 for date string exactly one line below
            
            # Use erase() instead of clear() - clears the in-memory window.
            # Combined with refresh(), ncurses seamlessly redraws only what changed,
            # meaning absolutely zero flicker on the terminal alternate screen.
            stdscr.erase()
            
            # Center vertically
            start_y = (h - total_height) // 2
            
            # Draw Time
            for i, line in enumerate(clock_lines):
                y = start_y + i
                x = (w - len(line)) // 2
                
                # Boundary check before drawing
                if 0 <= y < h and 0 <= x < w:
                    try:
                        stdscr.addstr(y, x, line, color)
                    except curses.error:
                        # Ignore curses drawing out of bounds errors if terminal shrinks aggressively
                        pass
                        
            # Draw Date exactly one line below
            date_y = start_y + clock_height
            date_x = (w - date_width) // 2
            if 0 <= date_y < h and 0 <= date_x < w:
                try:
                    stdscr.addstr(date_y, date_x, date_str, color)
                except curses.error:
                    pass
                    
            stdscr.refresh()
            
        except KeyboardInterrupt:
            break
        except curses.error:
            # Catch overarching curses environment errors
            pass

def main():
    parser = argparse.ArgumentParser(description="tinyclock - A minimalistic, highly optimized TUI digital clock.")
    parser.add_argument("-c", "--color", type=int, default=0, choices=range(8), 
                        help="Color index (0-7): 0=Default, 1=Red, 2=Green, 3=Yellow, 4=Blue, 5=Magenta, 6=Cyan, 7=White")
    
    args = parser.parse_args()

    # The curses wrapper properly initializes and tears down the alternate screen buffer,
    # ensuring the previous terminal window context is beautifully restored on exit.
    def curses_app(stdscr):
        color = curses.A_NORMAL
        
        # Setup colors safely
        if curses.has_colors():
            try:
                curses.start_color()
                curses.use_default_colors()
                
                if args.color != 0:
                    # Pair 1, Foreground user color, Background default (-1)
                    curses.init_pair(1, args.color, -1)
                    color = curses.color_pair(1) | curses.A_BOLD
            except curses.error:
                # If terminal doesn't support color despite has_colors() returning true
                pass
                
        draw_clock(stdscr, color)

    try:
        curses.wrapper(curses_app)
    except KeyboardInterrupt:
        # Ignore Traceback from uncaught Ctrl+C
        pass
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    main()
