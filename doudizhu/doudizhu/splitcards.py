# -*- coding: utf-8 -*-

"""
斗地主拆牌计算接口
~~~~~~~~~~~~~~~~~~~~~


"""
import itertools
import logging
import copy


class CardStyle(object):
    max = 0
    min = 0
    m_value = 0
    id = 0
    m_ISprimary = False
    edouble = -1
    esingle = -1

    def print_Value(self):
        if self.m_value <= 1 :
            print("single:", self.max)
        if self.m_value == 2:
            print("double:", self.max)
        if self.m_value == 3:
            print("three:{} + sigle:{} + double:{}".format(self.max, self.esingle, self.edouble))
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

    def getGreaterCS(self, cs):
        return self.getGreater(cs.m_value, cs.max, cs.min, cs.esingle, cs.edouble)

    def getGreater(self, iValue, iMax, iMin, esingle, edouble):
        cs = CardStyle()
        if iValue == -1:
            for i in range(len(self._single)):
                if self._single[i].max > iMax:
                    cs = copy.copy(self._single[i])
                    self._single.pop(i)
                    return cs
        if iValue == 2:
            for i in range(len(self._double)):
                if self._double[i].max > iMax:
                    cs = copy.copy(self._double[i])
                    self._double.pop(i)
                    return cs 

        if iValue == 3:
            for i in range(len(self._three)):
                if self._three[i].max > iMax:
                    if esingle>=0 and len(self._single) > 0:
                        cs = copy.copy(self._three[i])
                        cs.esingle = self._single[0].max
                        self._single.pop(0)
                        self._three.pop(i)
                    elif edouble>=0 and len(self._double) > 0:
                        cs = copy.copy(self._three[i])
                        cs.edouble = self._double[0].max
                        self._double.pop(0)
                        self._three.pop(i)
                    else:
                        cs = copy.copy(self._three[i])
                        self._three.pop(i)
                    return cs
        if iValue == 5:
            for i in range(len(self._link)):
                delta = self._link[i].max - self._link[i].min
                if self._link[i].max > iMax and self._link[i].min> iMin and \
                delta == iMax-iMin:
                    cs = copy.copy(self._link[i])
                    self._link.pop(i)
                    return cs
        if iValue == 6:
            for i in range(len(self._doublelink)):
                if self._doublelink[i].max > iMax:
                    cs = copy.copy(self._doublelink[i])
                    self._doublelink.pop(i)
                    return cs
        if iValue == 7:
            for i in range(len(self._plane)):
                if self._plane[i].max > iMax:
                    cs = copy.copy(self._plane[i])
                    self._plane.pop(i)
                    return cs
        if iValue == 8:
            for i in range(len(self._boom)):
                if self._boom[i].max > iMax:
                    cs = copy.copy(self._boom[i])
                    self._boom.pop(i)
                    return cs                   
        return cs

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
        print(" Values: rocket:{}, boom:{}, plane:{}, link:{}, doublelink:{}, three:{}, double:{}, single:{}".format(self.returnValue(self._rocket), \
                self.returnValue(self._boom), self.returnValue(self._plane), self.returnValue(self._link),  \
                self.returnValue(self._doublelink), self.returnValue(self._three), self.returnValue(self._double), self.returnValue(self._single)))
        return self.returnValue(self._rocket) + self.returnValue(self._boom) + self.returnValue(self._plane) + self.returnValue(self._link) + \
                self.returnValue(self._doublelink) + self.returnValue(self._three) + self.returnValue(self._double) + self.returnValue(self._single)

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


class SplitCards(object):


    def getAllPlane(self,  Cards_three, Cards_plane,  b):
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


    def getAllDoubleLink(self, intArray, Cards_doublelink, iBoom, iThree):
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


    def getOneLink(self, intArray):
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


    def JudgeLink(self, intArray, Cards_link):

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
    # delete des doublelink item, from src three array 
    def DeleteElement(self,  src, des):
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


    def InsertElement(self, src, des):
        for i in range(len(des)):
            src.append(dex[i])


    def returnValue(self, vec):
        sum = 0
        for i in range(len(vec)):
            sum += vec[i].m_value
        return sum


    def getBestHandNum(self, handNum):
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


    def ReviewCards(self, Cards, handCardBak, iBoom, iPlane, iDoublelink, iThree, iDouble):
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
            self.getAllPlane(handCardTmp._three, handCardTmp._plane, True)
            tmp = self.DeleteElement(handCardTmp._three, handCardTmp._plane)
            handCardTmp._three = tmp

        if iDouble > 0:
            for i in range(len(handCardBak._double)):
                handCardTmp._double.append(handCardBak._double[i])
                m_intArray[handCardBak._double[i].max] -= 2

            index = 0
            #check double link
            #and remove duplicate double
            #print("call getAllDoubleLink")
            self.getAllDoubleLink(m_intArray, handCardTmp._doublelink, iBoom, iThree)

            tmp = self.DeleteElement(handCardTmp._double, handCardTmp._doublelink)
            handCardTmp._double = tmp
            tmp = self.DeleteElement(handCardTmp._three, handCardTmp._doublelink)
            handCardTmp._three = tmp
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

        templink = self.getOneLink(m_intArray)
        if(len(templink) > 0):
            for i in range(len(templink)):
                handCardTmp._link.append(templink[i])
        templink = self.getOneLink(m_intArray)
        if(len(templink) > 0):
            for i in range(len(templink)):
                handCardTmp._link.append(templink[i])
        templink = self.getOneLink(m_intArray)
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

        self.getAllPlane(handCardTmp._three, handCardTmp._plane, True)
        self.getAllDoubleLink(m_intArray, handCardTmp._doublelink, iBoom, iThree)


        tmp = self.DeleteElement(handCardTmp._double, handCardTmp._doublelink)
        handCardTmp._double = tmp
        tmp = self.DeleteElement(handCardTmp._three, handCardTmp._doublelink)
        handCardTmp._three = tmp
        tmp = self.DeleteElement(handCardTmp._three, handCardTmp._plane)
        handCardTmp._three = tmp

        handCardTmp.print_Value()

        return handCardTmp


    def getIndexArray(self, tmparray):
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

    def getTempArr(self, Cards, idxArr):
        tmp = []
        #print("getTempArr:", idxArr)
        for i in range(len(idxArr)):
            #print(idxArr[i])
            j = idxArr[i]
            tmp.append(Cards[j])
        return tmp


    def SplitCards(self, Cards):
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

        self.getAllPlane(temp_three, temp_plane, True)
        if(len(temp_plane)):
            tmp = self.DeleteElement(temp_three, temp_plane)
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
        self.getAllDoubleLink(tempArray, temp_doublelink, 0, len(temp_three))

        if(len(temp_doublelink)):
            tmp = self.DeleteElement(temp_double, temp_doublelink)
            temp_double = tmp
        if(len(temp_doublelink)):
            tmp = self.DeleteElement(temp_three, temp_doublelink)
            temp_three = tmp


        tempboom_Arr = []
        tempplane_Arr = []
        tempdoublelink_Arr = []
        tempthree_Arr = []
        tempdouble_Arr = []

        tempboom_Arr = self.getIndexArray(temp_boom)
        print("tempboom_Arr", tempboom_Arr)

        tempplane_Ar = self.getIndexArray(temp_plane)
        print("tempplane_Ar", tempplane_Ar)

        tempdoublelink_Ar = self.getIndexArray(temp_doublelink)
        print("tempdoublelink_Ar", tempdoublelink_Ar)

        tempthree_Ar = self.getIndexArray(temp_three)
        print("temp_three", tempthree_Ar)

        tempdouble_Ar = self.getIndexArray(temp_double)
        print("temp_double", tempdouble_Ar)


        for i in range(len(tempboom_Arr)):
            tmp_boom_idx = tempboom_Arr[i]
            tmp_boom_ex = self.getTempArr(temp_boom, tmp_boom_idx)
            for j in range(len(tempplane_Ar)):
                tmp_plane_idx = tempplane_Ar[j]
                tmp_plane_ex = self.getTempArr(temp_plane, tmp_plane_idx)
                for k in range(len(tempdoublelink_Ar)):
                    tmp_dl_idx = tempdoublelink_Ar[k]
                    tmp_dl_ex = self.getTempArr(temp_doublelink, tmp_dl_idx)
                    for f in range(len(tempthree_Ar)):
                        tmp_th_idx = tempthree_Ar[f]
                        tmp_th_ex = self.getTempArr(temp_three, tmp_th_idx)
                        for h in range(len(tempdouble_Ar)):
                            tmp_db_idx = tempdouble_Ar[h]
                            tmp_db_ex = self.getTempArr(temp_double, tmp_db_idx)
                            hc = handCard()
                            hc.setItems(temp_rocket, tmp_boom_ex, tmp_plane_ex, tmp_dl_ex, temp_link, tmp_th_ex,
                                        tmp_db_ex, temp_single)

                            hc_review = self.ReviewCards(Cards, hc, i, j, k, f, h)
                            handNum.append(hc_review)

        result = self.getBestHandNum(handNum)
        return result


