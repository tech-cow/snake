import random
import curses as window

"""
initscr(): Initialize the library. Return a WindowObject which represents the whole screen.
curs_set(): Set the cursor state. visibility can be set to 0, 1, or 2, for invisible,
"""
s = window.initscr()
window.curs_set(0)
sh, sw = s.getmaxyx()

w = window.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)


# Snake initial position
snk_x = sw/4
snk_y = sh/2

# Snake Bodyparts
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Food starting place
food = [sh/2, sw/2]
# Add food to the screen
w.addch(food[0], food[1], window.ACS_DIAMOND)
# Snake initial moving direction
key = window.KEY_RIGHT
#
key_option = [window.KEY_DOWN, window.KEY_UP, window.KEY_LEFT, window.KEY_RIGHT]

while True:
    # Variable to store our next key input, return -1 if no inputs
    next_key = w.getch()
    # Edge to set the next key.
    if next_key is not -1 and next_key in key_option:
        key = next_key

    # Ternimating condition
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        window.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # This should be improving
    if key == window.KEY_DOWN:
        new_head[0] += 1
    if key == window.KEY_UP:
        new_head[0] -= 1
    if key == window.KEY_LEFT:
        new_head[1] -= 1
    if key == window.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], window.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], window.ACS_CKBOARD)
