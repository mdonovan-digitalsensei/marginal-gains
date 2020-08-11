import curses
import sys, os

class Game_Controller:
    def __init__(self, stdscr):
        height, width = stdscr.getmaxyx()
        main_window = curses.newwin(height, width)
        command_window = main_window.subwin(5, width, height - 5, 0)
        curses.noecho()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def render_ui(self):
        self.stdscr.refresh()
        self.main_window.refresh()
        self.command_window.refresh()

        # Instantiate player object
    def erase_ui(self):
        self.main_window.erase()
        self.

    marvin = Player("marvin", 1, 1, 1, 1, 5, 5)

    while key != "q":
        main_window.erase()
        command_window.erase()

        mw_height, mw_width = main_window.getmaxyx()
        marvin.set_max_yx(mw_height, mw_width)
        key_input(key, marvin)

        # Declaration of strings

        player_y, player_x = marvin.get_loc()

        main_window.addstr(player_y, player_x, "@", curses.color_pair(1))

        title = "An Example"[: width - 1]
        subtitle = "A subtitle"[: width - 1]
        keystr = "Last Key pressed: {}".format(key)[: width - 1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(
            cursor_x, cursor_y
        )
        if key == 0:
            keystr = "No key press detected..."[: width - 1]

        string1 = "main window"[: width - 1]
        string2 = "Command window"[: width - 1]

        main_window.addstr(1, int(mw_width / 2 - (len(string1) / 2)), string1)
        command_window.addstr(2, 2, string2)
        command_window.addstr(3, 2, keystr)
        command_window.addstr(4, 2, statusbarstr)

        stdscr.refresh()
        main_window.refresh()
        command_window.refresh()

        key = stdscr.getkey()