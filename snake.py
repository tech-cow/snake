import random
import curses

direction_option = [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]

"""Initialize Terminal Screen.

:api initscr(): Initialize the library.
:api curs_set(): Set the cursor state to invisible
:api getmaxyx(): return a tuple of screen height and screen Width
:api newwin(): create a new window with 4 corner coordinate.
:api keypad(): accept keypad input
:api timeout(): refresh the screen every input ms.
"""
init = curses.initscr()
curses.curs_set(0)
screen_h, screen_w = init.getmaxyx()
window = curses.newwin(screen_h, screen_w, 0, 0)
window.keypad(1)
window.timeout(100)

"""Initialize Snake Initial Position and Direction"""
snk_x = screen_w/4
snk_y = screen_h/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

"""Initialize Food Initial Position"""
food = [screen_h/2, screen_w/2]
window.addch(food[0], food[1], curses.ACS_DIAMOND)

key = curses.KEY_RIGHT

"""Logic"""
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, screen_h] or snake[0][1]  in [0, screen_w] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, screen_h-1),
                random.randint(1, screen_w-1)
            ]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], curses.ACS_CKBOARD)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
