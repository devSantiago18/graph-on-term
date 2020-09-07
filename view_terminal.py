from pynput import keyboard



selector, pos_selector = "->", 0


def view_main_menu():
    options = ["New Graph", "New Nodo", "New Edge", "Show Graph", "Exit"]
    # print(chr(27) + "[2J") #clear cli
    print("=" * 30)
    print("=" * 10, "  Menu  ", "=" * 10)
    for indx in range(len(options)):
        flat_pos = selector if pos_selector == indx else ""
        print("{:2} {}".format(flat_pos, options[indx]))
    print("="*30)

