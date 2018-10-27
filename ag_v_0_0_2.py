import random
import textwrap

def weighted_random_selection(obj1,obj2):
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2

def print_bold(msg,end='\n'):
    print("\033[1m" + msg + "\033[0m",end=end)


class GameUnit:
    def __init__(self,name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    def info(self):
        pass

    def attack(self,enemy):
        injured_unit = weighted_random_selection(self,enemy)
        injury = random.randint(10,15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury,0)
        print('攻击',end='')
        self.show_health(end=' ')
        enemy.show_health(end=' ')

    def heal(self,heal_by=2,full_healing=True):
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
        print_bold('你被治愈了!',end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        self.health_meter = self.max_hp

    def show_health(self,bold=False,end='\n'):
        msg = '血量: %s:%d' % (self.name,self.health_meter)

        if bold:
            print_bold(msg,end=end)
        else:
            print(msg,end=end)


class Knight(GameUnit):
    def __init__(self,name='Sir_U'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = '友军'

    def info(self):
        print('我是一名骑士！')

    def acquire_hut(self,hut):
        print_bold('您选择了营地 %d...' % hut.number,end=' ')
        is_enemy = (isinstance(hut.occupant,GameUnit) and hut.occupant.unit_type == '敌军')
        continue_attack = 'y'
        if is_enemy:
            print_bold('野生的敌军跳出来了')
            self.show_health(bold=True,end=' ')
            hut.occupant.show_health(bold=True,end=' ')
            while continue_attack:
                continue_attack = input("继续攻击吗？y/n:")
                if continue_attack == 'n':
                    self.run_away()
                    break

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break

            else:
                if hut.get_occupant_type() == '空置':
                    print_bold('该营地空置')
                else:
                    print_bold('前方友军出没')
                hut.acquire(self)
                self.heal()

    def run_away(self):
        print_bold('逃跑了... ...')
        self.enemy = None


class OrcRider(GameUnit):
    def __init__(self,name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = '敌军'
        self.hut_number = 0

    def info(self):
        print("敌军在此，莫要搞我！")


class Hut:
    def __init__(self,number,occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False


    def acquire(self,new_occupant):
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold('GJ!你成功获取了 %d 号营地' % self.number)

    def get_occupant_type(self):
        if self.is_acquired:
            occupant_type = '已占领'
        elif self.occupant is None:
            occupant_type = '空置'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type


class AttackofTheOrcs:
    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        print_bold('Mission')
        print("1、和敌人战斗")
        print("2、占领所有营地")
        print("------------------------------------\n")

    def _process_user_choice(self):
        verifying_choice = True
        idx = 0
        print("Current occupants: %s" % self.get_occupants())
        while verifying_choice:
            user_choice = input('请输入营地编号（1-5）：')
            idx = int(user_choice)
            if self.huts[idx-1].is_acquired:
                print('您泳有这个营地了，请换一个')
            else:
                verifying_choice = False

        return idx


    def _occupy_huts(self):
        for i in range(5):
            choice_lst = ['敌军','友军',None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == '敌军':
                name = '敌军-' + str(i+1)
                self.huts.append(Hut(i+1,OrcRider(name)))
            elif computer_choice == '友军':
                name = '骑士' + str(i+1)
                self.huts.append(Hut(i+1,Knight(name)))
            else:
                self.huts.append(Hut(i+1,computer_choice))


    def play(self):
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter <5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print_bold("你输了！青山不改绿水长流，少侠改日再战")
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold('胜利！')





if __name__ == '__main__':
    game = AttackofTheOrcs()
    game.play()



        #




