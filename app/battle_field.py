import random

from app.army_factory import ArmyFactory
from app.constants import STRATEGIES
from app.log_saver import LogSaver


class Battlefield:
    def __init__(self, num_armies):
        LogSaver.clear()
        self._armies = []
        for i in range(num_armies):
            self._armies.append(ArmyFactory.create(random.choice(STRATEGIES)))

    def start(self):
        LogSaver.add("There are {} armies.<br> The strategies are:".format(len(self._armies)))
        for i in range(0, len(self._armies)):
            LogSaver.add("<br>{} - {}".format(i, self._armies[i].get_strategy()))
        while True:
            for i in range(0, len(self._armies)):
                if self._armies[i].is_alive() and len([x for x in self._armies if x.is_alive()])>1:
                    target_army = random.choice([x for x in self._armies if x != self._armies[i] and x.is_alive()])
                    LogSaver.add("<p>&ensp;NEW BATTLE army # {} ATTACKS army # {}. It's strategy is {}</p>".format(i, self._armies.index(target_army), self._armies[i].get_strategy()))
                    self._armies[i].attack(target_army)

            if len([x for x in self._armies if x.is_alive()])==1:
                break

        for i in range(0, len(self._armies)):
            if self._armies[i].is_alive():
                LogSaver.add("<p>&ensp;ARMY # {} WINS THE WAR. {} IS THE BEST</p>".format(i, self._armies[i].get_strategy()))




