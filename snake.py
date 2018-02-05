import random
import curses

direction_option = [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]

screen_h = screen_w = 0

def init_screen(screen_h, screen_w):
    """Initialize Terminal Screen.

    :param screen_h: Height of the Terminal Screen.
    :param screen_w: Width of the Terminal Screen.

    :api initscr(): Initialize the library.
    :api curs_set(): Set the cursor state to invisible
    :api getmaxyx(): return a tuple of screen height and screen Width
    :api newwin(): create a new window with 4 corner coordinate.
    :api keypad(): accept keypad input
    :api timeout(): refresh the screen every input ms.
    """
    init = window.initscr()
    curses.curs_set(0)
    screen_h, screen_w = init.getmaxyx()
    window = window.newwin(screen_h, screen_w, 0, 0)
    window.keypad(1)
    window.timeout(100)

def init_snake(screen_h, screen_w):
    # Snake initial position
    # Snake Bodyparts
    snk_x = screen_w/4
    snk_y = screen_h/2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    # Snake initial moving direction
    direction = window.KEY_RIGHT

def init_food():
    # Food starting place
    food = [sh/2, sw/2]
    # Add food to the screen
    w.addch(food[0], food[1], curses.ACS_DIAMOND)
# While loop isn't the most optimal decision here..
while True:
    # Variable to store our next key input, return -1 if no inputs
    next_key = w.getch()
    # Edge to set the next key.
    if next_key is not -1 and next_key in key_option:
        direction = next_key

    # Ternimating condition
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        window.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # This should be improving
    if direction is curses.KEY_DOWN:
        new_head[0] += 1
    if direction is curses.KEY_UP:
        new_head[0] -= 1
    if direction is curses.KEY_LEFT:
        new_head[1] -= 1
    if direction is curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] is food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


def main():
    init_screen()
    init_snake()
    init_food()

main()
