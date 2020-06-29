# -*- coding: utf-8 -*-

"""
斗地主出牌模拟
~~~~~~~~~~~~~~~~~~~~~


"""
import itertools
import logging
from doudizhu import CardStyle
from doudizhu import handCard
import random
class PlayCards(object):

    _hc = []
    _hc.append(handCard())
    _hc.append(handCard())
    _hc.append(handCard())

    _lastCard = []
    _lastCard.append(CardStyle())
    _lastCard.append(CardStyle())
    _lastCard.append(CardStyle())

    _firstPlayer = 0
    _lastPlayer = 0

    _turnCount = 0
    _gameEnd = False

    def setBanker(self, hc):
        self._hc[0].setItems(hc._rocket, hc._boom, hc._plane, hc._doublelink, hc._link, hc._three, hc._double, hc._single)

    def setPesant1(self, hc):
        self._hc[1].setItems(hc._rocket, hc._boom, hc._plane, hc._doublelink, hc._link, hc._three, hc._double, hc._single)    

    def setPesant2(self, hc):
        self._hc[2].setItems(hc._rocket, hc._boom, hc._plane, hc._doublelink, hc._link, hc._three, hc._double, hc._single)    

    def setLastCards(self, pos, card):
        pass

    def isGameEnd(self):
        return self._gameEnd

    def call_quit(self, pos):
        if pos == 0:
            print("banker quit...")
        if pos == 1:
            print("pesant1 quit...")
        if pos == 2:
            print("pesant2 quit...")



    def getPlayCard(self, hc):
        cs = CardStyle()
        cs.m_value = 0
        if len(hc._plane)>0:
            cs = hc._plane[0]
            hc._plane.pop(0)
        elif len(hc._doublelink)>0:
            cs = hc._doublelink[0]
            hc._doublelink.pop(0)
        elif len(hc._link)>0:
            cs = hc._link[0]
            hc._link.pop(0)
        elif len(hc._three):
            cs = hc._three[0]
            hc._three.pop(0)
            if len(hc._single):
                cs.esingle = hc._single[0].max
                hc._single.pop(0)
            elif len(hc._double):
                cs.edouble = hc._double[0].max
                hc._double.pop(0)
        elif len(hc._double):
            cs = hc._double[0]
            hc._double.pop(0)
        elif len(hc._single):
            cs = hc._single[0]
            hc._single.pop(0)
        elif len(hc._boom):
            cs = hc._boom[0]
            hc._boom.pop(0)
        elif len(hc._rocket):
            cs = hc._rocket[0]
            hc._rocket.pop(0)
        cs.print_Value()
        return cs



    def getFollowCard(self, hc):
        tmp_cs = self._lastCard[self._lastPlayer]
        cs = hc.getGreaterCS(tmp_cs)
        if cs.m_value!= 0:
            cs.print_Value()
        return cs

    def Play(self, pos, bFirst):
        tmp_hc = self._hc[pos]

        if bFirst:            
            self._lastCard[pos] = self.getPlayCard(tmp_hc)
        else:
            self._lastCard[pos] = self.getFollowCard(tmp_hc)

        if tmp_hc.getShoushuEx() == 0:
            tmp_hc.print_Value()
            print("Game finished")
            self._gameEnd = True

        return self._lastCard[pos]

    def call_play(self, pos):

        # print("turncount:{}".format(self._turnCount))
        #if pos == 0:
        #    print("AI banker paly...")
        #if pos == 1:
        #    print("AI pesant1 play...")
        #if pos == 2:
        #    print("AI pesant2 play...")
        if self._firstPlayer == pos and self._lastPlayer == pos:            
            print("AI player{} first play".format(pos))
            # update last player pos
            # update last card type
            cs = self.Play(pos, True)
            self._lastPlayer  = pos
        else:
            print("AI player{} follow play".format(pos))
            cs = self.Play(pos, False)
            if cs.m_value == 0:
                print("AI player{} quit".format(pos))
                if self._firstPlayer == pos:
                    self._firstPlayer = self._lastPlayer
            else:
                
                # update last player pos
                # update last card type
                self._lastPlayer  = pos

        self._turnCount += 1
