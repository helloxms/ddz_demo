# -*- coding: UTF-8 -*-
# Author: xumingsheng
# Author: 
import copy

# 牌型枚举
class COMB_TYPE:
    PASS, SINGLE, DOUBLE, BOMB = range(4)


# 0-14 分别代表 3-10, J, Q, K, A, 2, BJ, CJ
black_joker, color_joker = 13, 14
# 定义 HAND_PASS 为过牌

HAND_PASS = {'type':COMB_TYPE.PASS, 'main': 0, 'component':[]}


# 根据当前手牌，获取此牌所有可能出的牌型
# 牌型数据结构为 {牌类型，主牌，包含的牌}
# 同种牌类型可以通过主牌比较大小
# 当前只处理单牌，对子，+ 王，王炸，2 的情况
def get_all_hands(pokers):
    if not pokers:
        return []

    # 过牌
    combs = []

    # 获取每个点数的数目
    dic = counter(pokers)

    # 王炸
    if black_joker in pokers and color_joker in pokers:
        combs.append({'type':COMB_TYPE.BOMB, 'main': color_joker, 'component': [black_joker, color_joker]})

    # 非顺子, 非王炸
    for poker in dic:
        if dic[poker] >= 1:
            # 单张
            combs.append({'type':COMB_TYPE.SINGLE, 'main':poker, 'component':[poker]})

        if dic[poker] >= 2:
            # 对子
            combs.append({'type':COMB_TYPE.DOUBLE, 'main':poker, 'component':[poker, poker]})

        if dic[poker] == 4:
            # 炸弹
            combs.append({'type':COMB_TYPE.BOMB, 'main':poker, 'component': [poker, poker, poker, poker]})

    combs.append(HAND_PASS)
    # 返回所有可能的出牌类型
    return combs





# 统计列表中每个元素的个数
def counter(pokers):
    dic = {}
    for poker in pokers:
        dic[poker] = pokers.count(poker)
    return dic




def can_beat2(comb1, comb2):
    if not comb2 or comb2['type'] == COMB_TYPE.PASS:
        return False

    if not comb1 or comb1['type'] == COMB_TYPE.PASS:
        return True

    if comb1['type'] == comb2['type']:
        return comb2['main'] > comb1['main']
    elif comb2['type'] == COMB_TYPE.BOMB:
        return True
    else:
        return False

# comb0  last_last_hand
# comb1  last_hand
# comb2  cur_hand
# 1. 同种牌型比较 main 值, main 值大的胜
# 2. 炸弹大过其他牌型
# 3. 牌型不同, 后出为负
def can_beat(comb0, comb1, comb2):

    if not comb2 or comb2['type'] == COMB_TYPE.PASS:
        return False

    if not comb1 or comb1['type'] == COMB_TYPE.PASS:
        return can_beat2(comb0, comb2)

    if comb1['type'] == comb2['type']:
        return comb2['main'] > comb1['main']
    elif comb2['type'] == COMB_TYPE.BOMB:
        return True
    else:
        return False



# 给定 cards，curplayerpos 求打出手牌 hand 后的牌
# 用 component 字段标志打出的牌, 可以方便地统一处理
def make_hand(cards, curplayerpos, hand):

    #print("curplyaerpos: ", curplayerpos)
    #print("cards{}: {}".format(curplayerpos,  cards[curplayerpos]) )
    #print("hand: ", hand)
    pokers = cards[curplayerpos]
    poker_clone = copy.copy(pokers)
    for poker in hand['component']:
        poker_clone.remove(poker)
    cards_clone = copy.copy(cards)
    cards_clone[curplayerpos] = poker_clone
    return cards_clone

def getBeforPlayer(iCur):
    if iCur >= 1:
        return iCur-1
    if iCur == 0:
        return 2

def getNextPlayer(iCur):
    if iCur < 2:
        return iCur+1
    if iCur == 2:
        return 0

def strategy_func(cards, curplayerpos, curhand, last_hand):
    if last_hand['type'] == COMB_TYPE.SINGLE and max(cards[curplayerpos] ) > last_hand['component'][0] :
        if curhand['type'] == COMB_TYPE.PASS:
            return False
            
    if curplayerpos == 2 and len(cards[0]) == 1 and curhand['type'] == COMB_TYPE.PASS:
        return False

    if curplayerpos == 2 and len(cards[0]) == 1 and curhand['type'] == COMB_TYPE.SINGLE:
        if curhand['component'][0] != max( cards[curplayerpos]):
            return False
            
    return True


# 模拟每次出牌, 
# cards 为所有玩家手牌
# curplayerpos 为当前出牌玩家的位置
# last_hand 为上一手对手出的牌, cache 用于缓存牌局与胜负关系
# last_last_hand 为上上一手玩家的出牌
def hand_out(cards,curplayerpos,  last_hand = None, last_last_hand = None, cache = {}):
    # 牌局终止的边界条件
    if not cards[0]:
        return 0

    if not cards[1]:
        return 1

    if not cards[2]:
        return 2
     

    # 如果上一手为空, 则将上一手赋值为 HAND_PASS
    if last_last_hand is None:
        last_last_hand = HAND_PASS
    if last_hand is None:
        last_hand = HAND_PASS

    bForce = False
    if last_last_hand['type'] == COMB_TYPE.PASS and last_hand['type'] == COMB_TYPE.PASS:
        bForce = True

    #print("curplayer: ", curplayerpos)
    # 从缓存中读取数据
    key = str((cards[0], cards[1], cards[2], getBeforPlayer(curplayerpos), last_hand['component']))
    #print("key: ",key)
    #if key in cache:
    #    return cache[key]

    # 模拟出牌过程, 深度优先搜索, 找到赢的分支则返回 True
    for current_hand in get_all_hands(cards[curplayerpos]):
        # 转换出牌权有两种情况: 
        #print("current_hand: ", current_hand)
        if bForce and current_hand['type'] == COMB_TYPE.PASS:
            #print("continue")
            continue
        tempkey = str((cards[0], cards[1], cards[2], curplayerpos, current_hand['component']))
        if tempkey in cache:
            #print("find key:", tempkey)
            continue

        if strategy_func(cards, curplayerpos, current_hand, last_hand) == False:
            continue

        # 当前手胜出, 则轮到下一个玩家选择出牌
        if can_beat(last_last_hand, last_hand, current_hand) or \
        (last_hand['type'] == COMB_TYPE.PASS and current_hand['type'] == COMB_TYPE.PASS) or \
        (last_hand['type'] != COMB_TYPE.PASS and current_hand['type'] == COMB_TYPE.PASS):
            #print("can beat: current hand:{}".format(current_hand['component']))
            iResult = hand_out(make_hand(cards, curplayerpos, current_hand), getNextPlayer(curplayerpos), current_hand, last_hand, cache)
            if iResult >= 0 :
                print(iResult,' :', key)
                cache[key] = iResult
                return iResult

        #print("looping ...")
    #print("loop over")
    return -1


# todo:
# 1. 用出牌列表作为 last_hand 的值, 方便调用函数


if __name__ == '__main__':
    import time
    start = time.clock()

    pCards=[[],[],[]]

    pCards[0] = [3,8,12]
    pCards[1] = [4,5,6]
    pCards[2] = [7,8,9]
    curplayerpos = 1
    targetPlayer = [1]
    cache={}
    result = -1
    for i in range(40):
        print("\nstart a new round:")
        cards = copy.copy(pCards)
        print(cards)
        result = hand_out(cards, curplayerpos,  None, None, cache)
        if result in targetPlayer:
            break;



    elapsed = (time.clock() - start)

    print("Result:", result)
    print("Elapsed:", elapsed)