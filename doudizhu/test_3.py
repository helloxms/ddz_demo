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
        if dic[poker] == 1:
            # 单张
            combs.append({'type':COMB_TYPE.SINGLE, 'main':poker, 'component':[poker]})

        if dic[poker] == 2:
            # 对子
            combs.append({'type':COMB_TYPE.DOUBLE, 'main':poker, 'component':[poker, poker]})
        if dic[poker] == 4:
            # 炸弹
            combs.append({'type':COMB_TYPE.BOMB, 'main':poker, 'component': [poker, poker, poker, poker]})

    combs.append(HAND_PASS)
    # 返回所有可能的出牌类型
    return combs

def get_max_flags(pokers):

    maxflag = {}
    maxflag[COMB_TYPE.PASS] = -1
    maxflag[COMB_TYPE.BOMB] = -1
    maxflag[COMB_TYPE.SINGLE] = -1
    maxflag[COMB_TYPE.DOUBLE] = -1
    if not pokers:
        return maxflag

    # 获取每个点数的数目
    dic = counter(pokers)
    # 王炸
    if black_joker in pokers and color_joker in pokers:
        maxflag[COMB_TYPE.BOMB] = color_joker
    # 非顺子, 非王炸
    for poker in dic:
        if dic[poker] == 1 and poker > maxflag[COMB_TYPE.SINGLE]:
            maxflag[COMB_TYPE.SINGLE] = poker

        if dic[poker] == 2 and poker > maxflag[COMB_TYPE.DOUBLE]:
            maxflag[COMB_TYPE.DOUBLE] = poker

        if dic[poker] == 4 and poker > maxflag[COMB_TYPE.BOMB]:
                maxflag[COMB_TYPE.BOMB] = poker
    return maxflag

def get_single_card(poker):
    return {'type':COMB_TYPE.SINGLE, 'main':poker, 'component':[poker] }


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
    if comb0['type'] == COMB_TYPE.PASS and comb1['type'] == COMB_TYPE.PASS:
        return True

    if comb0['type'] != COMB_TYPE.PASS and comb1['type'] == COMB_TYPE.PASS:
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

def isFriends(ipos1, ipos2):
    if ipos1 ==0  or ipos2 == 0:
        return False
    if ipos1>0 and ipos2 >0:
        return True

# 1 - 9
openloglevel = 6
def printlog(level, *args):
    if level >= openloglevel:
        print(*args)
    
# 
def strategy_func(cards, curplayerpos, curhand, last_hand, last_last_hand):

    maxflags = []
    for i in range(3):
        maxflag = get_max_flags(cards[i])
        maxflags.append(maxflag)


    ilast_player = getBeforPlayer(curplayerpos)
    ilast_last_player = getBeforPlayer(ilast_player)

    bFriends = isFriends(curplayerpos, ilast_player)

    #首出，只剩两张单牌，还有一个绝对大牌的话，先出绝对大牌，再出小
    '''
    if len(cards[curplayerpos]) == 2 and \
        (max(cards[curplayerpos]) >= max(cards[ilast_player])) and \
        (max(cards[curplayerpos]) >= max(cards[ilast_last_player])):
        if max(cards[curplayerpos]) > curhand['main']:
            printlog(5, "strategy", 0)
            return False
    '''

    #残局里基本上不需要pass了，能大过就大
    if maxflags[curplayerpos][last_hand['type']] > last_hand['main'] and curhand['type'] == COMB_TYPE.PASS:
        printlog(5, 1)
        return False
    #当前玩家p0，之前p1出牌，p2 pass时，如果p0 有大牌，尽量压牌
    #当前玩家p2, 之前p0出牌，p1 pass时，如果p2 有大牌，尽量压牌
    if curplayerpos != 1 and last_hand['type']==COMB_TYPE.PASS and \
    (maxflags[curplayerpos][last_last_hand['type']] > last_last_hand['main'] ):
        if curhand['type'] == COMB_TYPE.PASS:
            printlog(4,"strategy",  2)
            return False       

    #残局里，有对手报单了，自己只有单牌的话，从大出起
    #大不过的时候，出pass 也是可以的，否则流程会断掉
    #大不过的时候 curhand['main'] == 0 ,  maxflags[curplayerpos][curhand['type']] == -1
    if (curplayerpos == 0 and len(cards[1]) == 1 ) or \
        (curplayerpos == 0 and len(cards[2]) == 1 ) or \
        (curplayerpos == 2 and len(cards[0]) == 1 ) :
        if curhand['main'] < maxflags[curplayerpos][curhand['type']] :
            printlog(5,"strategy",  3)
            return False
        # curhand['main'] 可以为0，即pass action，
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

    printlog(3, "curplayer: ", curplayerpos)
    # 从缓存中读取数据
    key = str((cards[0], cards[1], cards[2], getBeforPlayer(curplayerpos), last_hand['component']))
    printlog(3, "key: ",key)
    #if key in cache:
    #    return cache[key]

    # 模拟出牌过程, 深度优先搜索, 找到赢的分支则返回 True
    printlog(3, cards[curplayerpos])
    combs = get_all_hands(cards[curplayerpos])
    for current_hand in combs:
        # 转换出牌权有两种情况: 
        printlog(3, "cur player: ", curplayerpos, "current_hand: ", current_hand)
        if bForce and current_hand['type'] == COMB_TYPE.PASS:
            #printlog("continue")
            continue
        tempkey = str((cards[0], cards[1], cards[2], curplayerpos, current_hand['component']))
        if tempkey in cache:
            #printlog("find key:", tempkey)
            continue

        if strategy_func(cards, curplayerpos, current_hand, last_hand, last_last_hand) == False:
            #printlog("fail action")
            continue

        # 当前手胜出, 则轮到下一个玩家选择出牌
        if can_beat(last_last_hand, last_hand, current_hand) or \
        (last_hand['type'] == COMB_TYPE.PASS and current_hand['type'] == COMB_TYPE.PASS) or \
        (last_hand['type'] != COMB_TYPE.PASS and current_hand['type'] == COMB_TYPE.PASS):
            #printlog("can beat: current hand:{}".format(current_hand['component']))
            iResult = hand_out(make_hand(cards, curplayerpos, current_hand), getNextPlayer(curplayerpos), current_hand, last_hand, cache)
            if iResult >= 0 :
                print(iResult,' :', key)
                cache[key] = iResult
                return iResult

        printlog(3, "looping ...")
    printlog(3, "loop over")
    return -1


# todo:
# 1. 用出牌列表作为 last_hand 的值, 方便调用函数

'''
    pCards[0] = [3,8,12]
    pCards[1] = [4,5,6]
    pCards[2] = [7,8,9]
    curplayerpos = 1
    targetPlayer = [1]    
'''

'''
    pCards[0] = [11,12]
    pCards[1] = [4,10,10,11]
    pCards[2] = [4,4,5,12]   
    curplayerpos = 1
    targetPlayer = [1]
'''
if __name__ == '__main__':
    import time
    start = time.clock()

    pCards=[[],[],[]]
    pCards[0] = [11,12]
    pCards[1] = [4,10,10,11]
    pCards[2] = [4,4,5,12]   
    curplayerpos = 1
    targetPlayer = [1]
    cache={}
    result = -1
    for i in range(10):
        print("\nstart a new round:")
        cards = copy.copy(pCards)
        print(cards)
        result = hand_out(cards, curplayerpos,  None, None, cache)
        #if result in targetPlayer:
        #    break;



    elapsed = (time.clock() - start)

    print("Result:", result)
    print("Elapsed:", elapsed)