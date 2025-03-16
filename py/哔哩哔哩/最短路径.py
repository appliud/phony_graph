import sys

class Edge:
    def __init__(self, a, b, c):
        #self 是一个约定俗成的参数名称
        #self 参数表示当前的 Graph 对象
        #通过使用 self，我们可以访问和操作 Graph 对象的属性
        self.a = a
        self.b = b
        self.c = c

class Graph:
    def __init__(self, d, e):
        self.d = d
        self.e = e
        self.adds = []

    def add_edge(self, edge1):
        self.adds.append(edge1)
        #append()修改原列表，将新的元素添加到列表的最后

def input_graph(figure):
    for i in range(figure.e):
        #range(0,figure.e,1)从0开始，到figure.e结束，间隔为1
        a, b, c = map(int, sys.stdin.readline().split())
        #sys.stdin.readline() 用于从标准输入读取一行
        #stdin 是 Python 中的标准输入流对象，而 readline() 方法则用于从输入流中读取一行内容
        #split() 方法用于将字符串按照指定的分隔符进行分割，默认的分隔符是空格
        figure.add_edge(Edge(a, b, c))

def exportation(figure):
    for i, add in enumerate(figure.adds):
        #i=0(默认)
        #enumerate()接受一个可迭代对象作为参数，并返回一个迭代器
        #迭代器生成由索引和对应元素组成的元组
        #元组具有不可修改性
        print(f"第{i+1}个：{add.a} {add.b} {add.c}")

def find_shortest_path(figure, source, destination):
    distance = [float('inf')] * figure.d
    parent = [-1] * figure.d

    distance[source-1] = 0
    b=-1
    while b!=distance[destination-1]:
        for j in range(figure.e):
            u = figure.adds[j].a
            v = figure.adds[j].b
            weight = figure.adds[j].c

            if distance[u-1] != float('inf') and distance[u-1] + weight < distance[v-1]:
                distance[v-1] = distance[u-1] + weight
                parent[v-1] = u
        b=distance[destination-1]

    path = [destination]
    c = parent[destination-1]
    while c != -1:
        path.append(c)
        if c != source:
            path.append(" <- ")
        c = parent[c-1]

    print(f"从{source}号点到{destination}号点的最短路径为：")
    print(" <- ".join(map(str, path[::-1])))
    print(f"最小权重为：{distance[destination-1]}")

def main():
    d1, e1 = map(int, input("请输入点的个数和边的个数：").split())
    #split()字符串方法，用于将字符串分割成一个列表，根据指定的分隔符(默认)将字符串拆分为多个元素
    figure = Graph(d1, e1)
    print("请输入每条边的起点，终点，权重：")
    input_graph(figure)
    exportation(figure)
    source, destination = 1, d1
    find_shortest_path(figure, source, destination)
#确保 main() 函数只在当前模块作为主程序执行时被调用
#__name__表示当前模块的名称
if __name__ == "__main__":#当main是一个模块时被调用
    main()