import random
import textwrap

def show_theme_message(width):
    print_dotted_line()
    print('\033[1m' + '来战吧！' + '\033[0m')

    msg = ('她加入了一场战争')
    print(textwrap.fill(msg, width=width))


def show_game_mission():
    print('Mission')
    print('\t选择一个营地吧')
    print('TIP')
    print('小心营地旁边有小怪兽哦~')
    print_dotted_line()

def occupy_huts():
    huts = []
    occupants = ['敌军', '友军', '空置']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts

def process_user_choice():
    msg = '选择营地编号(1-5):'
    user_choice = input('\n' + msg)
    idx = int(user_choice)
    print('查看情况')
    msg = ''
    l = [i for i in range(1,6)]
    if idx not in l:
        print('选择错误请重新选择')
        return process_user_choice()
    return idx

def show_health(health_meter,bold=False):
    msg = '血量：玩家：%d,敌军：%d' %(health_meter['玩家'],health_meter['敌军'])

    if bold:
        print_bold(msg)
        print_dotted_line()
    else:
        print(msg)

def print_bold(msg,end='\n'):
    print('\033[1m' + msg + '\033[0m',end=end)

def print_dotted_line(width=72):
    dotted_line = '.' * width
    print(dotted_line)

def reset_health_meter(health_meter):
    health_meter['玩家'] = 40
    health_meter['敌军'] = 30

def attack(health_meter):
    hit_list = 4 * ['玩家'] + 6 * ['敌军']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10,15)
    health_meter[injured_unit] = max(hit_points - injury,0)
    print('攻击！',end='')
    show_health(health_meter)

def reveal_occupants(idx,huts):
    msg = ""
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i + 1, huts[i])
        if i + 1 == '敌军':
            occupant_info = "occupant_info"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

def enter_hut(idx,huts):
    if huts[idx - 1] == '敌军':
        pass
    else:
        print('选择营地编号 %d...' % idx, end=' ')
        print("你赢了")
    print_dotted_line()


def play_game(health_meter):
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx,huts)
    if huts[idx - 1] != '敌军':
        print_bold('你赢了')
    else:
        print_bold('野生的敌军跳出来了！',end='')
        show_health(health_meter,bold=True)
        continue_attack = True

        while continue_attack:
            continue_attack = input('继续攻击吗？y/n')
            if continue_attack == 'n':
                print_bold('您的剩余血量是...')
                show_health(health_meter,bold=True)
                print_bold('你已经死了！')
                break

            attack(health_meter)

            if health_meter['敌军'] <= 0:
                print_bold('GJ！敌军已经被覆灭！你已成最大赢家！')
                break
            if health_meter['玩家']<= 0:
                print_bold('你已经死了！青山不改绿水长流，少侠请来日再战！')
                break

def run_application():
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()
    width = 72
    show_theme_message(width)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input('重来一遍？y/n')


if __name__ == '__main__':
    run_application()



        #




