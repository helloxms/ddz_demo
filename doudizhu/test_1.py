import itertools
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
        if self.m_value <= 1 :
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
        if self.m_value == 8:
            print("boom:", self.max)
        if self.m_value == 9:
            print("rocket:", self.max)
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
        if len(self._three) <= len(self._single) or len(self._three) <= len(self._double):
            tS -= len(self._three)
        return tS

    def returnValue(self, vec):
        sum = 0
        for i in range(len(vec)):
            sum += vec[i].m_value
        return sum

    def getQuanzhi(self):
        print(" Values: rocket:{}, boom:{}, plane:{}, link:{}, doublelink:{}, three:{}, double:{}, single:{}".format(returnValue(self._rocket), \
                returnValue(self._boom), returnValue(self._plane), returnValue(self._link),  \
                returnValue(self._doublelink), returnValue(self._three), returnValue(self._double), returnValue(self._single)))
        return returnValue(self._rocket) + returnValue(self._boom) + returnValue(self._plane) + returnValue(self._link) + \
                returnValue(self._doublelink) + returnValue(self._three) + returnValue(self._double) + returnValue(self._single)

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
    def print_typeNum(self):
        print(" typeNum: rocket:{}, boom:{}, plane:{}, link:{}, doublelink:{}, three:{}, double:{}, single:{}".format(len(self._rocket), \
                len(self._boom), len(self._plane), len(self._link),  \
                len(self._doublelink), len(self._three), len(self._double), len(self._single)))


def getAllPlane( Cards_three, Cards_plane,  b):
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
                    temp.m_ISprimary = True
                    temp.m_value = 7
                    Cards_plane.append(temp)
                    temp.print_Value()
                index = 0
        if index >= 1:
            temp = CardStyle()
            temp.max = j
            temp.min = j - index
            temp.m_ISprimary = True
            temp.m_value = 7
            Cards_plane.append(temp)
            temp.print_Value()
    return

def getAllDoubleLink(intArray, Cards_doublelink, iBoom, iThree):
    tmpArray = {}
    for i in range(12):
        tmpArray[i] = intArray[i]
    print("getAllDoubleLink intArray:{}".format(intArray))
    print("iBoom:{}, iThree:{}".format(iBoom, iThree))
    for i in range(12):
        if iThree == 0 and tmpArray[i] == 3:
            tmpArray[i] = 0
        if iBoom == 0 and tmpArray[i] == 4:
            tmpArray[i] = 0

    index = 0
    j = 0
    for i in range(11):
        if tmpArray[i]>=2 and tmpArray[i+1]>=2:
            index += 1
            j = i+1
        else:
            if index >= 2:
                temp = CardStyle()
                temp.max = j
                temp.min = j - index
                temp.m_ISprimary = True
                temp.m_value = 6
                Cards_doublelink.append(temp)
                for k in range(temp.min, temp.max+1):
                    intArray[k] -= 2
            index = 0

    if index >= 2:
        temp = CardStyle()
        temp.max = j
        temp.min = j - index
        temp.m_ISprimary = True
        temp.m_value = 6
        Cards_doublelink.append(temp)
        for k in range(temp.min, temp.max + 1):
            intArray[k] -= 2
    return

def getOneLink(intArray):
    index = 0
    #link
    Cards_link = []
    for i in range(12):
        if intArray[i] > 0:
            index += 1
            #print("index:{} value:{} num:{}".format(index, i, intArray[i]))
            if index == 5:
                cs = CardStyle()
                cs.max = i
                cs.min = cs.max-4
                cs.m_value = 5
                cs.m_ISprimary = True
                Cards_link.append(cs)
                for j in range(cs.min, cs.max+1):
                    intArray[j] -= 1
                index = 0
        else:
                index = 0

    #check link
    if len(Cards_link) > 0:
        for i in range(12):
            for j in range(len(Cards_link)):
                if intArray[i] > 0:
                    if Cards_link[j].max + 1 == i:
                        Cards_link[j].max = i
                        intArray[i] -= 1

        del_array = []
        for i in range(len(Cards_link)-1):
            if Cards_link[i].max + 1 == Cards_link[i+1].min:
                Cards_link[i+1].min = Cards_link[i].min
                del_array.append([Cards_link[i].min, Cards_link[i].max])

        #delete old link
        link_array = []
        for j in range(len(Cards_link)):
            imin = Cards_link[j].min
            imax = Cards_link[j].max
            if [imin, imax] not in del_array:
                link_array.append(Cards_link[j])
        Cards_link = link_array

    return Cards_link

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

def getBestHandNum(handNum):
    if len(handNum) > 0:
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

        tValue_max = handNum_tmp[0].getQuanzhi()
        for i in range(len(handNum_tmp)):
            tValue = handNum_tmp[i].getQuanzhi()
            if tValue >= tValue_max:
                tValue_max = tValue
        for i in range(len(handNum_tmp)):
            tValue = handNum_tmp[i].getQuanzhi()
            if tValue == tValue_max:
                handNum_bak.append(handNum_tmp[i])

        for i in range(len(handNum)):
            print("handNum {}/{}, Shoushu={} ,Value={} ".format(i + 1, len(handNum), handNum[i].getShoushuEx(),
                                                                handNum[i].getQuanzhi()))
            handNum[i].print_Value()

        for i in range(len(handNum_tmp)):
            print("handNum_tmp {}/{}, Shoushu={} ,Value={} ".format(i + 1, len(handNum_tmp),
                                                                    handNum_tmp[i].getShoushuEx(),
                                                                    handNum_tmp[i].getQuanzhi()))
            handNum_tmp[i].print_Value()

        for i in range(len(handNum_bak)):
            print("handNum_bak {}/{}, Shoushu={} ,Value={} ".format(i + 1, len(handNum_bak),
                                                                    handNum_bak[i].getShoushuEx(),
                                                                    handNum_bak[i].getQuanzhi()))
            handNum_bak[i].print_Value()
            handNum_bak[i].print_typeNum()
        return handNum_bak

def ReviewCards(Cards, handCardBak, iBoom, iPlane, iDoublelink, iThree, iDouble):
    m_intArray = {}
    for i in range(15):
        m_intArray[i] = 0
    for i in range(len(Cards)):
        m_intArray[Cards[i]] += 1
    print("ReviewCards func:")
    print(m_intArray)
    print("iBoom:{}, iPlane：{}, iDoublelink:{}, iThree:{}, iDouble:{}".format(iBoom, iPlane, iDoublelink, iThree, iDouble))
    handCardTmp = handCard()
    if len(handCardBak._rocket) > 0:
        for i in range(len(handCardBak._rocket)):
            handCardTmp._rocket.append(handCardBak._rocket[i])
        m_intArray[13] -= 1
        m_intArray[14] -= 1

    if iBoom > 0:
        for i in range(len(handCardBak._boom)):
            handCardTmp._boom.append(handCardBak._boom[i])
            m_intArray[handCardBak._boom[i].max] = 0
    if iPlane > 0:
        for i in range(len(handCardBak._plane)):
            handCardTmp._plane.append(handCardBak._plane[i])
            imin = handCardBak._plane[i].min
            imax = handCardBak._plane[i].max
            for j in range(imin, imax+1):
                m_intArray[j] -= 3
    if iDoublelink > 0:
        for i in range(len(handCardBak._doublelink)):
            handCardTmp._doublelink.append(handCardBak._doublelink[i])
            imin = handCardBak._doublelink[i].min
            imax = handCardBak._doublelink[i].max
            for j in range(imin, imax+1):
                m_intArray[j] -= 2

    if iThree > 0:
        for i in range(len(handCardBak._three)):
            handCardTmp._three.append(handCardBak._three[i])
            m_intArray[handCardBak._three[i].max] -= 3
        getAllPlane(handCardTmp._three, handCardTmp._plane, True)
        tmp = DeleteElement(handCardTmp._three, handCardTmp._plane)
        handCardTmp._three = tmp

    if iDouble > 0:
        for i in range(len(handCardBak._double)):
            handCardTmp._double.append(handCardBak._double[i])
            m_intArray[handCardBak._double[i].max] -= 2

        index = 0
        #check double link
        #and remove duplicate double
        #print("call getAllDoubleLink")
        getAllDoubleLink(m_intArray, handCardTmp._doublelink, iBoom, iThree)

        tmp = DeleteElement(handCardTmp._double, handCardTmp._doublelink)
        handCardTmp._double = tmp
        #print("len doublelink is:", len(handCardTmp._doublelink))
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

    templink = getOneLink(m_intArray)
    if(len(templink) > 0):
        for i in range(len(templink)):
            handCardTmp._link.append(templink[i])
    templink = getOneLink(m_intArray)
    if(len(templink) > 0):
        for i in range(len(templink)):
            handCardTmp._link.append(templink[i])
    templink = getOneLink(m_intArray)
    if(len(templink) > 0):
        for i in range(len(templink)):
            handCardTmp._link.append(templink[i])

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
            cs.m_value = -1
            if i >= 12:
                cs.m_value = 1
            cs.m_ISprimary = True
            handCardTmp._single.append(cs)
            #print("add single card: ", cs.max)

    getAllPlane(handCardTmp._three, handCardTmp._plane, True)
    getAllDoubleLink(m_intArray, handCardTmp._doublelink, iBoom, iThree)


    tmp = DeleteElement(handCardTmp._double, handCardTmp._doublelink)
    handCardTmp._double = tmp
    tmp = DeleteElement(handCardTmp._three, handCardTmp._plane)
    handCardTmp._three = tmp

    handCardTmp.print_Value()

    return handCardTmp


def getIndexArray(tmparray):
    inum = len(tmparray)
    result = [[]]
    temp = []
    for i in range(inum):
        temp.append(i)
    for i in range(1, inum+1):
        a = list(itertools.combinations(temp, i))
        for j in range(len(a)):
            result.append( list(a[j]))
    # print(result)
    return result

def getTempArr(Cards, idxArr):
    tmp = []
    #print("getTempArr:", idxArr)
    for i in range(len(idxArr)):
        #print(idxArr[i])
        j = idxArr[i]
        tmp.append(Cards[j])
    return tmp

def SplitCards(Cards):
    print("SplitCards func:")
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
        cs.max = 14
        cs.min = 14
        cs.m_value = 9
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
        if m_intArray[i] == 1:
            cs = CardStyle()
            cs.max = i
            cs.min = i
            cs.m_value = -1
            if i >= 12:
                cs.m_value = 1
            cs.m_ISprimary = True
            m_intArray[i] = 0
            temp_single.append(cs)

    getAllPlane(temp_three, temp_plane, True)
    if(len(temp_plane)):
        tmp = DeleteElement(temp_three, temp_plane)
        temp_three = tmp

    print("test1:")
    if len(temp_three) > 0 or len(temp_double) > 0:
        tempArray = {}
        for i in range(15):
            tempArray[i] = 0
        for i in range(len(temp_three)):
            tempArray[temp_three[i].max] = 3
        for i in range(len(temp_double)):
            tempArray[temp_double[i].max] = 2
    getAllDoubleLink(tempArray, temp_doublelink, 0, len(temp_three))

    if(len(temp_doublelink)):
        tmp = DeleteElement(temp_double, temp_doublelink)
        temp_double = tmp


    tempboom_Arr = []
    tempplane_Arr = []
    tempdoublelink_Arr = []
    tempthree_Arr = []
    tempdouble_Arr = []

    tempboom_Arr = getIndexArray(temp_boom)
    print("tempboom_Arr", tempboom_Arr)

    tempplane_Ar = getIndexArray(temp_plane)
    print("tempplane_Ar", tempplane_Ar)

    tempdoublelink_Ar = getIndexArray(temp_doublelink)
    print("tempdoublelink_Ar", tempdoublelink_Ar)

    tempthree_Ar = getIndexArray(temp_three)
    print("temp_three", tempthree_Ar)

    tempdouble_Ar = getIndexArray(temp_double)
    print("temp_double", tempdouble_Ar)


    for i in range(len(tempboom_Arr)):
        tmp_boom_idx = tempboom_Arr[i]
        tmp_boom_ex = getTempArr(temp_boom, tmp_boom_idx)
        for j in range(len(tempplane_Ar)):
            tmp_plane_idx = tempplane_Ar[j]
            tmp_plane_ex = getTempArr(temp_plane, tmp_plane_idx)
            for k in range(len(tempdoublelink_Ar)):
                tmp_dl_idx = tempdoublelink_Ar[k]
                tmp_dl_ex = getTempArr(temp_doublelink, tmp_dl_idx)
                for f in range(len(tempthree_Ar)):
                    tmp_th_idx = tempthree_Ar[f]
                    tmp_th_ex = getTempArr(temp_three, tmp_th_idx)
                    for h in range(len(tempdouble_Ar)):
                        tmp_db_idx = tempdouble_Ar[h]
                        tmp_db_ex = getTempArr(temp_double, tmp_db_idx)
                        hc = handCard()
                        hc.setItems(temp_rocket, tmp_boom_ex, tmp_plane_ex, tmp_dl_ex, temp_link, tmp_th_ex,
                                    tmp_db_ex, temp_single)

                        hc_review = ReviewCards(Cards, hc, i, j, k, f, h)
                        handNum.append(hc_review)

    result = getBestHandNum(handNum)







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
print("\n\nrank list:", rank_list)
SplitCards(rank_list)


rank_list.sort(reverse=False)
print("\n\nrank_list = ", rank_list)
# logging.info("test end")