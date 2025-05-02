import turtle

# 设置画布和画笔
screen = turtle.Screen()
screen.setup(800, 800)
pen = turtle.Turtle()
pen.speed(3)

# 定义颜色
colors = ["#4285F4", "#DB4437", "#F4B400", "#0F9D58"]

# 绘制第一个圆弧（蓝色部分）
pen.penup()
pen.goto(-50, 30)
pen.pendown()
pen.color(colors[0])
pen.begin_fill()
pen.circle(100, 90)
pen.setheading(0)
pen.circle(-100, 90)
pen.end_fill()

# 绘制第二个圆弧（红色部分）
pen.penup()
pen.goto(-50, -70)
pen.pendown()
pen.color(colors[1])
pen.begin_fill()
pen.setheading(-90)
pen.circle(100, 90)
pen.setheading(180)
pen.circle(-100, 90)
pen.end_fill()

# 绘制第三个圆弧（黄色部分）
pen.penup()
pen.goto(50, -70)
pen.pendown()
pen.color(colors[2])
pen.begin_fill()
pen.setheading(-180)
pen.circle(100, 90)
pen.setheading(90)
pen.circle(-100, 90)
pen.end_fill()

# 绘制第四个圆弧（绿色部分）
pen.penup()
pen.goto(50, 30)
pen.pendown()
pen.color(colors[3])
pen.begin_fill()
pen.setheading(90)
pen.circle(100, 90)
pen.setheading(0)
pen.circle(-100, 90)
pen.end_fill()

# 绘制中间的白色圆形
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# 隐藏画笔
pen.hideturtle()

# 保持窗口打开
turtle.done()