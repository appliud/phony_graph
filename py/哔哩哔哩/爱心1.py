import turtle

# 注册自定义图标
turtle.register_shape("heart_shape", ((5, 0), (4, 2), (1, 4), (-2, 3), (-4, 1), (-5, -1),
                                    (-3, -4), (0, -5), (3, -4), (5, -1), (4, 2), (0, 0)))

# 设置画布和画笔参数
canvas = turtle.Screen()#创建了一个名为canvas的画布，可以在其上进行绘图操作。
canvas.bgcolor("black")#将画布的背景颜色设置为黑色。
pen = turtle.Turtle()#创建了一个名为pen的画笔。
pen.shape("heart_shape")#将画笔的形状设置为"heart_shape"，即之前我们注册的自定义爱心形状。
pen.color("red")#将画笔的颜色设置为红色
pen.speed(1)#将画笔的绘制速度设置为3，数字越大绘制速度越快。

# 绘制爱心图案
def draw_heart():
    pen.begin_fill()#用于开始填充颜色。
    pen.left(50)#将画笔向左旋转50度
    pen.forward(133)#将画笔向前移动133个像素
    pen.circle(50, 200)#绘制半径为50的圆弧，角度为200度，即绘制了一个弧形的部分。
    pen.right(140)#将画笔向右旋转140度
    pen.circle(50, 200)#再次绘制半径为50的圆弧，角度为200度，即绘制了另一个弧形的部分。
    pen.forward(133)#再次将画笔向前移动133个像素。
    pen.end_fill()#结束填充颜色。

# 移动画笔到绘制起始位置
pen.penup()#将画笔抬起，不绘制图形。
pen.goto(-70, -50)#将画笔移动到坐标 (-70, -50) 的位置。这里的坐标指的是画布上的点坐标，x 坐标为 -70，y 坐标为 -50。
pen.pendown()# 将画笔放下，准备绘制图形。



# 绘制爱心图案
draw_heart()

# 关闭画布
canvas.exitonclick()