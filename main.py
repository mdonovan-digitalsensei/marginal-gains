import sys,os
import curses


def draw_ui(stdscr):
    k = 0
    cursor_x = 1
    cursor_y = 1

    height, width = stdscr.getmaxyx()

    main_window = curses.newwin(height, width)
    command_window = main_window.subwin(5, width, height - 5, 0)

    mw_height, mw_width = main_window.getmaxyx()

    curses.noecho()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.refresh()
    main_window.refresh()
    command_window.refresh()

    while k != 'q':
        main_window.erase()
        command_window.erase()
        if k == "KEY_DOWN":
            cursor_y = cursor_y + 1
        elif k == "KEY_UP":
            cursor_y = cursor_y - 1
        elif k == "KEY_LEFT":
            cursor_x = cursor_x - 1
        elif k == "KEY_RIGHT":
            cursor_x = cursor_x + 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(mw_width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(mw_height-1, cursor_y)

        # Declaration of strings

        title = "An Example"[:width-1]
        subtitle = "A subtitle"[:width-1]
        keystr = "Last Key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        string1 = "main window"[:width-1]
        string2 = "sub window"[:width-1]

        main_window.addstr(1, int(mw_width / 2 - (len(string1)/2)), string1)
        command_window.addstr(2, 2, string2)
        command_window.addstr(3, 2, keystr)
        command_window.addstr(4, 2, statusbarstr)

        stdscr.refresh()
        main_window.refresh()
        command_window.refresh()

        k = stdscr.getkey()


def main():
    curses.wrapper(draw_ui)


if __name__ == "__main__":
    main()


