import doudizhu
from doudizhu import Card
from doudizhu import Doudizhu
import logging
logging.basicConfig(level=logging.INFO)


def CardStrListToCardIntList(cards):
    return [Card.new(card_str) for card_str in cards]


print(Card.CHAR_RANK_TO_INT_RANK)
print(Card.INT_RANK_TO_CHAR_RANK)



cards_min4 = CardStrListToCardIntList(
['3c', '3d', '3h', '3s'])

cards_min3 = CardStrListToCardIntList(
['3c', '3d', '3h'])

cards_min3_2 = CardStrListToCardIntList(
['3c', '3d', '3h', '4c', '4d'])

cards_min3_1 = CardStrListToCardIntList(
['3c', '3d', '3h', '4c'])



'''

ret = doudizhu.list_greater_cards(cards_target, cards_candidate)
print("ret: ", ret)



for card_type, cards_list in ret.items():
    ret[card_type] = [set(cards) for cards in cards_list]
    for cards in ret[card_type]:
        c = Card.get_rank_list(list(cards))
        c = Card.sort_cards_by_int(c)
        print(c)
'''


def output_dic_rank_info(cards_dict):
    print("dict rank info")
    for card_type, cards_list in cards_dict.items():
        cards_dict[card_type] = [set(cards) for cards in cards_list]
        for cards in cards_dict[card_type]:
            c = Card.get_rank_list(list(cards))
            c = Card.sort_cards_by_int(c)
            print(c)


def output_list_rank_info(cards_list):
    c = Card.get_rank_list(cards_list)
    c = Card.sort_cards_by_int(c)
    print("list rank info")
    print(c)




cards_group = doudizhu.new_game()

for i in range(4):  
    c = Card.get_rank_list(cards_group[i])
    c = Card.sort_cards_by_int(c)
    print(c)
    print(Card.cards_without_suit(cards_group[i]))

for i in cards_group[3]:
    cards_group[0].append(i)




rank_list = Card.get_rank_list(cards_group[0])
print(rank_list)

str_list = Card.cards_without_suit(cards_group[0])
print(str_list)


class CardStyle(object):
    max = 0
    min = 0
    m_value = 0
    id = 0
    m_ISprimary = False
    def print_Value(self):
        if self.m_value == 1:
            print("single:", self.max)
        if self.m_value == 2:
            print("double:", self.max)
        if self.m_value == 3:
            print("three:", self.max)
        if self.m_value == 5:
            print("link:{}--{}".format(self.min, self.max))
        if self.m_value == 6:
            print("doublelink:{}--{}".format(self.min, self.max))
        if self.m_value == 7:
            print("plane:{}--{}".format(self.min, self.max))
        if self.m_value >= 8:
            print("boom:", self.max)
        #print("max ", self.max, "min ", self.min, "value ", self.m_value)


# insert CardStyle
class handCard(object):
    _rocket = []
    _boom = []
    _three = []
    _plane = []
    _link = []
    _doublelink = []
    _double = []
    _single = []

    def __init__(self):
        self._rocket = []
        self._boom = []
        self._plane = []
        self._doublelink = []
        self._link = []
        self._three = []
        self._double = []
        self._single = []

    def setItems(self, rocket, boom, plane, doublelink, link, three, double, sigle):
        for i in range(len(rocket)):
            self._rocket.append(rocket[i])
        for i in range(len(boom)):
            self._boom.append(boom[i])
        for i in range(len(plane)):
            self._plane.append(plane[i])
        for i in range(len(doublelink)):
            self._doublelink.append(doublelink[i])
        for i in range(len(link)):
            self._link.append(link[i])
        for i in range(len(three)):
            self._three.append(three[i])
        for i in range(len(double)):
            self._double.append(double[i])
        for i in range(len(sigle)):
            self._single.append(sigle[i])


    def getShoushu(self):
        return len(self._rocket)+len(self._boom)+len(self._three)+len(self._plane)+len(self._link)+\
               len(self._doublelink)+len(self._double)+len(self._single)
    def getShoushuEx(self):
        tS = self.getShoushu()
        if len(self._three) == len(self._single) or len(self._three) == len(self._double):
            tS -= len(self._three)
        return tS

    def returnValue(self, vec):
        sum = 0
        for i in range(len(vec)):
            sum += vec[i].m_value
        return sum

    def getQuanzhi(self):
        return returnValue(self._rocket) + returnValue(self._boom) + returnValue(self._plane) + returnValue(self._link) + \
                returnValue(self._doublelink) + returnValue(self._double) + returnValue(self._single)

    def print_Value(self):
        for i in range(len(self._rocket)):
            self._rocket[i].print_Value()
        for i in range(len(self._boom)):
            self._boom[i].print_Value()
        for i in range(len(self._plane)):
            self._plane[i].print_Value()
        for i in range(len(self._doublelink)):
            self._doublelink[i].print_Value()
        for i in range(len(self._link)):
            self._link[i].print_Value()
        for i in range(len(self._three)):
            self._three[i].print_Value()
        for i in range(len(self._double)):
            self._double[i].print_Value()
        for i in range(len(self._single)):
            self._single[i].print_Value()

def JudgeFly( Cards_three, Cards_plane,  b):
    Cards_plane = []
    if len(Cards_three) >= 2:
        index = 0
        j = 0
        for i in range(len(Cards_three)-1):
            if Cards_three[i].max+1 == Cards_three[i+1].max and Cards_three[i+1].max <= 12:
                index += 1
                j = Cards_three[i].max+1
            else:
                if index >= 1:
                    temp = CardStyle()
                    temp.max = j
                    temp.min = j - index
                    temp.m_ISprimary = b
                    temp.m_value = 7
                    Cards_plane.append(temp)
                index = 0
        if index >= 1:
            temp = CardStyle()
            temp.max = j
            temp.min = j - index
            temp.m_ISprimary = b
            temp.m_value = 7
            Cards_plane.append(temp)
    return

def JudgeDoubleLink(Cards_double, Cards_doublelink, b):
    if len(Cards_double) >= 3:
        m_intArray = {}
        for i in range(15):
            m_intArray[i] = 0
        for i in range(len(Cards_double)):
            m_intArray[Cards_double[i].max] = 2
        print("JudgeDoubleLink func:")
        print(m_intArray)
        index = 0
        j = 0
        for i in range(12):
            if m_intArray[i] == m_intArray[i+1] == 2:
                index += 1
                j = i+1
            else:
                if index >= 2:
                    temp = CardStyle()
                    temp.max = j
                    temp.min = j - index
                    temp.m_ISprimary = b
                    temp.m_value = 6
                    Cards_doublelink.append(temp)
                index = 0
        if index >= 2:
            temp = CardStyle()
            temp.max = j
            temp.min = j - index
            temp.m_ISprimary = b
            temp.m_value = 6
            Cards_doublelink.append(temp)

def JudgeLink(intArray, Cards_link):

    index = 0
    j = 0
    for i in range(11):
        if intArray[i]>0 and intArray[i+1]>0:
            index += 1
            j=i+1
        else:
            if index >= 4:
                temp = CardStyle()
                temp.max = j
                temp.min = j - index
                temp.m_ISprimary = false
                temp.m_value = 5
                Cards_link.append(temp)
            index = 0
    if index >= 4:
        temp = CardStyle()
        temp.max = j
        temp.min = j - index
        temp.m_ISprimary=false
        temp.m_value = 5
        Cards_link.append(temp)

# delete des doublelink item, form src double array
# delete des plane from item, from src three array
def DeleteElement( src, des):
    deleteArray=[]
    if len(des) > 0:
        for i in range(len(des)):
            for j in range( des[i].min, des[i].max+1):
                for k in range(len(src)):
                    if src[k].max == j:
                        deleteArray.append(src[k].max)
    src_clean=[]
    if len(deleteArray)>0:
        print("delete Array:", deleteArray)
        for i in range(len(src)):
            if src[i].max not in  deleteArray:
                src_clean.append(src[i])
        return src_clean
    return src


def InsertElement(src, des):
    for i in range(len(des)):
        src.append(dex[i])

def returnValue(vec):
    sum = 0
    for i in range(len(vec)):
        sum += vec[i].m_value
    return sum

def ReviewCards(Cards, handCardBak, bBoom, bPlane, bDoublelink, bLink, bThree, bDouble):
    m_intArray = {}
    for i in range(15):
        m_intArray[i] = 0
    for i in range(len(Cards)):
        m_intArray[Cards[i]] += 1
    print("ReviewCards:")
    print(m_intArray)
    print("bBoom:{}, bPlane：{}, bDoublelink:{}, bLink:{}, bThree:{}, bDouble:{}".format(bBoom, bPlane, bDoublelink, bLink, bThree, bDouble))
    handCardTmp = handCard()
    if bBoom:
        for i in range(len(handCardBak._boom)):
            handCardTmp._boom.append(handCardBak._boom[i])
            m_intArray[handCardBak._boom[i].max] = 0
    if bPlane:
        for i in range(len(handCadBak._plane)):
            handCardTmp._plane.append(handCardBak._plane[i])
            imin = handCardBak._plane[i].min
            imax = handCardBak._plane[i].max
            for j in range(imin, imax+1):
                m_intArray[j] -= 3
    if bDoublelink:
        for i in range(len(handCardBak._doublelink)):
            handCardTmp._doublelink.append(handCardBak._doublelink[i])
            imin = handCardBak._doublelink[i].min
            imax = handCardBak._doublelink[i].max
            for j in range(imin, imax+1):
                m_intArray[j] -= 2
    if bLink:
        for i in range(len(handCardBak._link)):
            handCardTmp._link.append(handCardBak._link[i])
            imin = handCardBak._link[i].min
            imax = handCardBak._link[i].max
            print(imin, imax)
            for j in range(imin, imax+1):
                m_intArray[j] -= 1

    if bThree:
        for i in range(len(handCardBak._three)):
            handCardTmp._three.append(handCardBak._three[i])
            m_intArray[handCardBak._three[i].max] -= 3
        JudgeFly(handCardTmp._three, handCardTmp._doublelink, True)
        tmp = DeleteElement(handCardTmp._three, handCardTmp._doublelink)
        handCardTmp._three = tmp

    if bDouble:
        for i in range(len(handCardBak._double)):
            handCardTmp._double.append(handCardBak._double[i])
            m_intArray[handCardBak._double[i].max] -= 2

        index = 0
        #check double link
        #and remove duplicate double
        print("call JudgeDoubleLink")
        JudgeDoubleLink(handCardTmp._double, handCardTmp._doublelink, True)

        tmp = DeleteElement(handCardTmp._double, handCardTmp._doublelink)
        handCardTmp._double = tmp
        print("len doublelink is:", len(handCardTmp._doublelink))
        for i in range(len(handCardTmp._doublelink)):
            handCardTmp._doublelink[i].print_Value()
        '''
        for i in range(12):
            if m_intArray[i] > 1:
                index += 1
                print("double: {} num:{}".format(i, m_intArray[i]))
                if index == 3 :
                    cs = CardStyle()
                    cs.max = i
                    cs.min = cs.max-2
                    cs.m_value = 6
                    cs.m_ISprimary = True
                    handCardTmp._doublelink.append(cs)
                    for j in range(cs.min, cs.max+1):
                        m_intArray[j] -= 2
                    index = 0
            else:
                    index = 0
        '''
    index = 0
    #link
    for i in range(12):
        if m_intArray[i] > 0:
            index += 1
            print("index:{} value:{} num:{}".format(index, i, m_intArray[i]))
            if index == 5:
                cs = CardStyle()
                cs.max = i
                cs.min = cs.max-4
                cs.m_value = 5
                cs.m_ISprimary = True
                handCardTmp._link.append(cs)
                for j in range(cs.min, cs.max+1):
                    m_intArray[j] -= 1
                index = 0
        else:
                index = 0

    #check link
    if len(handCardTmp._link) > 0:
        for i in range(12):
            for j in range(len(handCardTmp._link)):
                if m_intArray[i] > 0:
                    if handCardTmp._link[j].max + 1 == i:
                        handCardTmp._link[j].max = i
                        m_intArray[i] -= 1

        del_array = []
        for i in range(len(handCardTmp._link)-1):
            if handCardTmp._link[i].max + 1 == handCardTmp._link[i+1].min:
                handCardTmp._link[i+1].min = handCardTmp._link[i].min
                del_array.append([handCardTmp._link[i].min, handCardTmp._link[i].max])

        #delete old link
        link_array = []
        for j in range(len(handCardTmp._link)):
            imin = handCardTmp._link[j].min
            imax = handCardTmp._link[j].max
            if [imin, imax] not in del_array:
                link_array.append(handCardTmp._link[j])
        handCardTmp._link = link_array

    #
    for i in range(15):
        if m_intArray[i] == 4:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 8
            cs.m_ISprimary = True
            handCardTmp._boom.append(cs)
        if m_intArray[i] == 3:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 3
            cs.m_ISprimary = True
            handCardTmp._three.append(cs)
        if m_intArray[i] == 2:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 2
            cs.m_ISprimary = True
            handCardTmp._double.append(cs)
        if m_intArray[i] == 1:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 1
            cs.m_ISprimary = True
            handCardTmp._single.append(cs)
            #print("add single card: ", cs.max)


    JudgeFly(handCardTmp._three, handCardTmp._plane, True)
    JudgeDoubleLink(handCardTmp._double, handCardTmp._doublelink, True)
    print("finish ReviewCards 1")
    tmp = DeleteElement(handCardTmp._double, handCardTmp._doublelink)
    for i in range(len(tmp)):
        tmp[i].print_Value()
    print("finish ReviewCards 2")
    for i in range(len(handCardTmp._doublelink)):
        handCardTmp._doublelink[i].print_Value()
    print("finish ReviewCards 3")
    handCardTmp._double = tmp
    tmp = DeleteElement(handCardTmp._three, handCardTmp._plane)
    handCardTmp._three = tmp

    handCardTmp.print_Value()

    return handCardTmp

def SplitCards(Cards):
    temp_rocket = []
    temp_boom = []
    temp_plane = []
    temp_doublelink = []
    temp_link = []
    temp_three = []
    temp_double = []
    temp_single = []
    m_intArray = {}
    for i in range(15):
        m_intArray[i] = 0
    for i in range(len(Cards)):
        m_intArray[Cards[i]] += 1
    print("intArray: ", m_intArray)
    handNum = []
    if m_intArray[13] == 1 and m_intArray[14] == 1:
        cs = CardStyle()
        cs.max = 15
        cs.min = 15
        cs.m_value = 8
        cs.m_ISprimary = True
        m_intArray[13] = 0
        m_intArray[14] = 0
        temp_rocket.append(cs)

    for i in range(15):
        if m_intArray[i] == 4:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 8
            cs.m_ISprimary = True
            m_intArray[i] = 0
            temp_boom.append(cs)
        if m_intArray[i] == 3:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 3
            cs.m_ISprimary = True
            m_intArray[i] = 0
            temp_three.append(cs)
        if m_intArray[i] == 2:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = 2
            cs.m_ISprimary = True
            m_intArray[i] = 0
            temp_double.append(cs)
    JudgeFly(temp_three, temp_plane, True)
    JudgeDoubleLink(temp_double, temp_doublelink, True)

    if(len(temp_doublelink)):
        tmp = DeleteElement(temp_double, temp_doublelink)
        temp_double = tmp
    if(len(temp_plane)):
        tmp = DeleteElement(temp_three, temp_plane)
        temp_three = tmp

    tempboom = 0
    tempplane = 0
    tempdoublelink = 0
    templink = 0
    tempthree = 0
    tempdouble = 0
    if len(temp_boom) > 0:
        tempboom = 1
    if len(temp_plane) > 0:
        tempplane = 1
    if len(temp_doublelink) > 0:
        tempdoublelink = 1
    if len(temp_link) > 0:
        templink = 1
    if len(temp_three) > 0:
        tempthree = 1
    if len(temp_double) > 0:
        tempdouble = 1

    hc = handCard()
    hc.setItems(temp_rocket, temp_boom, temp_plane, temp_doublelink, temp_link, temp_three, temp_double, temp_single)

    for i in range(tempboom+1):
        for j in range(tempplane+1):
            for k in range(tempdoublelink+1):
                for l in range(templink+1):
                    for f in range(tempthree+1):
                        for h in range(tempdouble+1):
                            hc_review = ReviewCards(Cards, hc, i, j, k, l, f, h)
                            handNum.append(hc_review)

    if len(handNum)>0:
        tS_min = handNum[0].getShoushuEx()
        tS_max = handNum[0].getShoushuEx()
        handNum_tmp = []
        handNum_bak = []
        for i in range(1, len(handNum)):
            tS = handNum[i].getShoushuEx()
            if tS <= tS_min:
                tS_min = tS
            if tS >= tS_max:
                tS_max = tS
        for i in range(len(handNum)):
            tS = handNum[i].getShoushuEx()
            if tS == tS_min:
                handNum_tmp.append(handNum[i])

        tValue_min = handNum_tmp[0].getQuanzhi()
        for i in range(len(handNum_tmp)):
            tValue = handNum_tmp[i].getQuanzhi()
            if tValue <= tValue_min:
                tValue_min = tValue
        for i in range(len(handNum_tmp)):
            tValue = handNum_tmp[i].getQuanzhi()
            if tValue == tValue_min:
                handNum_bak.append(handNum_tmp[i])

        for i in range(len(handNum)):
            print("handNum {}/{}, Shoushu={} ,Value={} ".format(i+1, len(handNum), handNum[i].getShoushuEx(), handNum[i].getQuanzhi()))
            handNum[i].print_Value()

        for i in range(len(handNum_tmp)):
            print("handNum_tmp {}/{}, Shoushu={} ,Value={} ".format(i+1, len(handNum_tmp), handNum_tmp[i].getShoushuEx(), handNum_tmp[i].getQuanzhi()))

        for i in range(len(handNum_bak)):
            print("handNum_bak {}/{}, Shoushu={} ,Value={} ".format(i+1, len(handNum_bak), handNum_bak[i].getShoushuEx(), handNum_bak[i].getQuanzhi()))
            #handNum_bak[i].print_Value()




#rank_list = [0,0,0,1,3,4,5,6,7,7,7,8,8,9,9,11,11,12,14]
#rank_list = [3,4,5,6,7,7,7,8,8,9,9]
#rank_list = [3,4,5,6,7,7,8,8,9,9]
rank_list = [3,4,5,6,7,7,7,8,8,9,9]
print("\n\nrank list:", rank_list)
SplitCards(rank_list)

# logging.info("test end")