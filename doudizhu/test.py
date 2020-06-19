from doudizhu import Card, new_game
cards_groups = new_game()
cards_groups

for cards_group in cards_groups:
    Card.print_pretty_cards(cards_group)


