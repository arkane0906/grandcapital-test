def calc_positions(menu_items):
    """
    Resets ranks from 0 to n, n being the number of items.
    """
    position = 0
    for menu_item in menu_items:
        menu_item.position = position
        menu_item.save()
        position += 1