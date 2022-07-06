# Author: Fishycx
# Time: 2022/7/4 10:27 AM

def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice == 0:
            answer = input('您确定要退出系统吗？y/n')
            if answer == 'y' or answer == 'Y':
                print('谢谢您的使用')
        elif choice == 1:
            insert()
        elif choice == 2:
            search()
        elif choice == 3:
            delete()
        elif choice == 4:
            total()
        elif choice == 5:
            show()

def menu():
    print("======================管理系统=========================")
    print('======================功能菜单=========================')
    print('\t\t\t\t\t\t\t\t1.输入学生信息')
    print('\t\t\t\t\t\t\t\t2.插')
    print('\t\t\t\t\t\t\t\t1.输入学生信息')

def insert():
    pass
def search():
    pass
def delete():
    pass
def total():
    pass
def show():
    pass