from turtle import *
#你实际上导入了 turtle 模块的所有全局函数（如 setup(), listen(), forward(), right() 等）和一个隐式的默认海龟实例。
#这个默认海龟实例的创建规则如下：
#触发条件：当首次调用任何需要海龟实例的全局函数时（例如 forward(), right(), circle()），模块会自动创建一个默认海龟实例。
#默认属性：位置在屏幕中心 (0, 0)，方向朝右（0 度），默认可见（箭头显示）
from freegames import vector, square
import random

#重点考虑square的坐标是左下角的，arrow的坐标是三角形下中部分，
# 并且绘制蛇的方式是通过移动头节点加入新的头结点到蛇神列表，然后在踢出最后一个久节点
#  A B C   移动得到新节点D变成   D A B ，如果遇到食物最后一个节点不删除就变成 D A B C，绘制出所有节点
#设置屏幕宽高
win_height = 420
win_width = 420
game_over=False
#设置食物一开始的坐标
food = vector(0, 0)
#头节点坐标
head1 = vector(-win_width / 2 + 10, 0)
head2 = vector(win_width / 2 - 40, 0)

text_show=Turtle()
text_show.hideturtle()
text_show.penup()
text_show.color("green")

#创建两个箭头海龟代表蛇头
snake_head1 = Turtle()
snake_head2 = Turtle()
#用list存下蛇身坐标
snake1 = [head1]
snake2 = [head2]

#蛇头移动函数，
def condition(direction, head):
    if direction == "up":
        head.y += 10
    elif direction == "down":
        head.y -= 10
    elif direction == "left":
        head.x -= 10
    else:
        head.x += 10
    return head

#更换蛇头根据不同方向调转蛇头的方向位置
def change_head(direction, snake_head, head):
    # 确保海龟（蛇头）不会留下轨迹
    snake_head.clear()

    if direction == "up":
        snake_head.setheading(90)  # 向上，角度就是向上
        # 箭头在上方，此时箭头要在头结点上放中央，头结点是square，square的x，y是左下角的
        #那么就因该是(y+头结点高度10)此时在上方，在加上5保持一点间距，x保持中央就是+5宽度一半
        snake_head.goto(head.x + 5, head.y + 15)
    elif direction == "down":
        snake_head.setheading(270)  # 向下
        snake_head.goto(head.x + 5, head.y - 5)  # 箭头在下方
    elif direction == "left":
        snake_head.setheading(180)  # 向左
        snake_head.goto(head.x - 5, head.y + 5)  # 箭头在左侧
    elif direction == "right":
        snake_head.setheading(0)  # 向右
        snake_head.goto(head.x + 15, head.y + 5)  # 箭头在右侧

def judge(type,head):
    global game_over
    print(head)
    print(snake1)
    print(snake2)
    if (not (-win_width / 2 < head.x < win_width / 2)
            or not (-win_height / 2 < head.y < win_height / 2)
            or head in snake1 or head in snake2):
        if type==1:
            text_show.write("Blue win", align="center", font=("Arial", 30, "bold"))
        else:
            text_show.write("Red win", align="center", font=("Arial", 30, "bold"))
        update()
        game_over=True
        return
def move(type, direction):
    global head1, head2
    if game_over:
        return
    if type == 1:
        new_head=head1.copy()
        condition(direction, new_head)
        judge(1,new_head)
        head1=new_head
        snake1.insert(0, head1.copy())
        change_head(direction, snake_head1, head1)

        if abs(head1.x - food.x) < 10 and abs(head1.y - food.y) < 10:
            print("snake1 eat")
            food.x = random.randint(-win_width / 2 + 20, win_width / 2 - 20)
            food.y = random.randint(-win_height / 2 + 20, win_height / 2 + 20)
        else:
            snake1.pop()
    else:
        new_head=head2.copy()
        condition(direction, new_head)
        judge(2, new_head)
        head2=new_head
        snake2.insert(0, head2)
        change_head(direction, snake_head2, head2)

        if abs(head2.x - food.x) < 10 and abs(head2.y - food.y) < 10:
            print("snake2 eat")
            food.x = random.randint(-win_width / 2 + 20, win_width / 2 - 20)
            food.y = random.randint(-win_height / 2 + 20, win_height / 2 + 20)
        else:
            snake2.pop()

    clear()

    # 绘制蛇身
    for body in snake1:
        square(body.x, body.y, 10, 'red')

    for body in snake2:
        square(body.x, body.y, 10, 'blue')

    # 绘制食物
    square(food.x, food.y, 10, 'green')

    update()

#初始化
def init():
    #隐藏默认海龟
    hideturtle()
    # 设置蛇头外观，大小颜色，取消画笔
    snake_head1.shape("arrow")
    snake_head2.shape("arrow")
    snake_head1.shapesize(0.5, 0.5)
    snake_head2.shapesize(0.5, 0.5)
    snake_head1.penup()
    snake_head2.penup()
    snake_head1.color("red")
    snake_head2.color("blue")
    # 设置蛇头初始位置和方向
    snake_head1.setheading(0)  # 向右
    snake_head1.goto(head1.x + 15, head1.y + 5)  # 箭头在右侧
    snake_head2.setheading(180)  # 向左
    snake_head2.goto(head2.x - 5, head2.y + 5)  # 箭头在左侧
    # 绘制初始游戏元素
    square(head1.x, head1.y, 10, 'red')
    square(head2.x, head2.y, 10, 'blue')
    square(food.x, food.y, 10, 'green')
    tracer(False)  # 关闭自动刷新，而是使用手动更新，这个放在前面就能取消初始化动画

    #更新画面
    update()
    #设置窗口大小，不去设置位置默认屏幕中心
    setup(win_width, win_height)



init()
#使当前窗口监听键盘事件
listen()
#去监听
onkey(lambda: move(1, "up"), 'w')
onkey(lambda: move(1, "down"), 's')
onkey(lambda: move(1, "left"), 'a')
onkey(lambda: move(1, "right"), 'd')
onkey(lambda: move(2, "up"), 'Up')
onkey(lambda: move(2, "down"), 'Down')
onkey(lambda: move(2, "left"), 'Left')
onkey(lambda: move(2, "right"), 'Right')
done()