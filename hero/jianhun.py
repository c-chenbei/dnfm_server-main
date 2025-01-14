import time
from .hero import Hero


class Jianhun(Hero):

    # 职业键位映射表
    def skillMap(self):
        return {
            "后跳": "Jump_Back",
            "取消": "Jump",
            "崩山击": "button1",
            "三段斩": "button2",
            "小小乱舞": "button3",
            "小乱舞": "button4",
            "temp1": "button5",
            "咸鱼连突": "button6",
            "破军": "button7",
            "觉醒": "button8",
            "猛龙": "button9",
            "乱舞": "button10",
            "小拔刀": "button11",
            "temp3": "button12",
            "上状态": "button13",
            "temp2": "button14",
            "temp4": "button15"
        }

    # 预设每个房间的行为
    def action(self, MapNumber):
        wait = 0.1
        if MapNumber == 0:
            self.ctrl.reset()
            time.sleep(wait)
            self.skill("上状态")
            time.sleep(1.2)
            self.ctrl.move(330)
            time.sleep(0.3)
            self.ctrl.move(0)
            time.sleep(0.8)
            self.skill("破军")
            time.sleep(0.3)
            self.skill("小乱舞")
            time.sleep(1.5)
            self.skill("小小乱舞")
        elif MapNumber == 1:
            time.sleep(wait)
            self.ctrl.move(230)
            time.sleep(0.4)
            self.ctrl.move(350)
            time.sleep(0.3)
            self.skill("乱舞")
        elif MapNumber == 2:
            time.sleep(wait)
            self.ctrl.move(340)
            time.sleep(0.5)
            self.ctrl.move(0)
            time.sleep(0.6)
            self.skill("小乱舞")
            time.sleep(1.0)
            self.skill("破军")
        elif MapNumber == 3:
            time.sleep(wait)
            self.ctrl.move(340)
            time.sleep(0.7)
            self.skill("小拔刀")
        elif MapNumber == 4:
            time.sleep(wait)
            self.ctrl.move(45)
            time.sleep(0.55)
            self.ctrl.move(180)
            time.sleep(0.05)
            self.skill("咸鱼连突")
            time.sleep(1.0)
        elif MapNumber == 5:
            time.sleep(wait)
            self.ctrl.move(200)
            time.sleep(0.7)
            self.ctrl.move(1)
            time.sleep(0.7)
            self.ctrl.move(180)
            time.sleep(0.05)
            self.skill("觉醒")
            time.sleep(0.4)
            self.skill("觉醒")
            time.sleep(0.4)
            self.skill("觉醒")
            time.sleep(0.4)
            self.skill("觉醒")
        elif MapNumber == 6:
            var = None
        elif MapNumber == 7:
            time.sleep(wait)
            self.ctrl.move(335)
            time.sleep(0.4)
            self.ctrl.move(1)
            time.sleep(0.7)
            self.skill("小拔刀")
        elif MapNumber == 8:
            time.sleep(wait)
            self.ctrl.move(340)
            time.sleep(0.4)
            self.ctrl.move(0)
            time.sleep(0.4)
            self.skill("猛龙")
            time.sleep(0.1)
            self.ctrl.move(180)
            self.skill("猛龙")
            time.sleep(0.1)
            self.skill("猛龙")
            time.sleep(1.0)
        elif MapNumber == 9:
            time.sleep(wait)
            self.ctrl.move(330)
            time.sleep(0.4)
            self.ctrl.move(1)
            time.sleep(0.3)
            self.skill("乱舞")
            time.sleep(0.5)
            self.skill("乱舞")
            time.sleep(0.5)
            self.skill("乱舞")
            time.sleep(0.5)
            self.skill("乱舞")
            time.sleep(0.5)

    #################################################################################
    # 2024/9/15
    # 自动攻击执行逻辑
    # 给角色安排1-2个冷却低的小技能（最好是不在上面的预定施放列表中的）
    # 自动攻击期间，每隔2.5秒，尝试施放一次该技能，其余时间普攻
    # （把几个小技能做成一键连招可以节省键位，只需填写连招第一个技能名，每2.5秒会点一次连招）
    #
    #################################################################################
    def get_auto_skill(self):
        return ["小小乱舞"]

    #################################################################################
    # 特殊动作
    #
    # 某些情况下希望人物做出一些特殊动作而设计
    # 比如说剑魂打完狮子头回到6号房时，用五段斩跑图直接进入7号房
    # 没有特殊动作的英雄，可以不写这个方法
    #################################################################################
    def special_action(self, last_room_num, room_num):
        if self.pre_room_num == room_num:
            return False
        if last_room_num == 5 and room_num == 6:
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.skill("三段斩", prefix="特殊动作")
            time.sleep(0.2)
            self.pre_room_num = room_num
            return True
        else:
            return False
