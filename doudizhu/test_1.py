import itertools
import doudizhu
from doudizhu import Card
from doudizhu import Doudizhu
from doudizhu import CardStyle
from doudizhu import handCard
from doudizhu import SplitCards

import logging
logging.basicConfig(level=logging.INFO)


cards_group = doudizhu.new_game()
##
print("set cards for all player")
for i in range(4):  
    c = Card.get_rank_list(cards_group[i])
    c = Card.sort_cards_by_int(c)
    print(c)
    print(Card.cards_without_suit(cards_group[i]))



##
print("set game banker")
for i in cards_group[3]:
    cards_group[0].append(i)

rank_list = Card.get_rank_list(cards_group[0])
print(rank_list)

str_list = Card.cards_without_suit(cards_group[0])
print(str_list)





#rank_list = [0,0,0,1,3,4,5,6,7,7,7,8,8,9,9,11,11,12,14]
#rank_list = [3,4,5,6,7,7,7,8,8,9,9]
#rank_list = [3,3,4,4,5,5,6,7,7,8,8,9,9,9,9,10,10,11,11]
#rank_list = [3,4,5,6,7,7,7,7,8,8,9,9]
#rank_list = [6,6,7,7,8,8,9,10,10,11,11,12,12]
#rank_list = [6,6,7,7,8,8,9,10,10,11,11,12,12]
#rank_list = [11, 10, 9, 8, 7, 7, 6, 6, 5, 5, 5, 4, 2, 2, 1, 0, 0, 10, 9, 8]
#rank_list = [11, 11, 8, 8, 7, 6, 6, 5, 5, 4, 4, 3, 1, 1, 1, 0, 0, 12, 11, 5]
#rank_list = [12, 11, 11, 11, 10, 9, 8, 7, 7, 6, 6, 5, 4, 3, 2, 1, 0, 4, 2, 0]
#rank_list = [1, 1, 3, 4, 4, 4, 5, 6, 6, 7, 9, 9, 9, 10, 10, 10, 11, 11, 12, 12]
#rank_list = [0, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 10, 12]
#rank_list =  [0, 1, 1, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 9, 11, 12, 12, 12, 14]
#rank_list =  [0, 1, 1, 2, 2, 4, 5, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 12, 12]
#rank_list =  [1, 1, 2, 3, 3, 4, 4, 6, 7, 8, 8, 9, 10, 10, 11, 11, 11, 12, 13, 14]
#rank_list =  [0, 0, 4, 4, 4, 4, 6, 6, 7, 7, 7, 7, 9, 9, 10, 10, 11, 11, 12, 12]
#rank_list = [6,6,7,7,8,8,8,9,9,10,10]
print("\n\nrank list:", rank_list)
tmpSC = SplitCards()
tmpSC.SplitCards(rank_list)


rank_list.sort(reverse=False)
print("\n\nrank_list = ", rank_list)
# logging.info("test end")