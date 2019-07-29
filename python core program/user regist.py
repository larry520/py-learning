# -*- encoding: utf-8 -*-


"""
用户注册功能：
    实现用户注册，并将信息保存在磁盘中，用户注册至少给定：用户名  密码
用户登录功能：
    建立一个用户数据库,包含： 登录名，密码， 上次登录的时间戳
    根据系统提示，输入用户名和密码，信息正确时显示登录成功，否则
    登录失败，连续三次失败账号锁死1分钟
"""

def regist():
    flag = True
    while flag:
        username = input("请输入用户名：\n")
        if not user_exist(username):
            flag = False
        else:
            print('用户名已存在! 请重新输入:\n')

    flag2 = True
    while flag2:
        password = input("请输入密码：\n")
        passwordnew = input("请再次输入密码\n")
        if password == passwordnew:
            flag2 = False

    with open('users.log', 'a', encoding='utf-8') as f:
        temp = '\n' + username + "$" + password
        f.write(temp)

    print("用户%s注册成功，请牢记用户名和密码\n" % username)
    return True


def user_exist(username):
    """
    判断用户名是否已存在, 存在返回 True
    :param username: 用户名
    :return: Bool
    """
    with open('users.log', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split("$")
            if username == line_list[0]:
                return True
    return False


def login():
    username = input("请输入用户名：\n")
    password = input("请输入密码：\n")
    with open('users.log', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split("$")
            print("...", line_list)

            if not line_list == "":
                if username == line_list[0] and password == line_list[1]:
                    print('用户{}登录成功\n' .format(username))
                    return True
    return False

if __name__ == '__main__':
    print('welcome login PY system')
    flag = 0
    while True:
        inp = input("1:登录; 2:注册 \n")
        if inp == '1':
            is_loging = login()
            if is_loging:
                print('登录成功\n')
            else:
                print('登录失败\n')
                flag = flag + 1
                if flag ==3:
                    print('重复登录超出限制,程序退出')
                    break
        if inp == '2':
            result = regist()
            if result:
                print('注册成功\n')
            else:
                print('注册失败\n')


