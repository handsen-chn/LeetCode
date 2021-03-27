
#import numpy as np
#recs = [[0, 1, 1], [0.5, 2, 2]]
##题设给定矩形
rectangles = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

import matplotlib.pyplot as plt
import math
import pandas as pd

from collections import deque

'''################Step-1 构造堆及相关方法################'''


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = int(L_length / 2)  # 有孩子节点的节点
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    '''
    ##原文生成升序排列的list，此处不需要，因此注释掉
    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)
    '''

    return [L[i] for i in range(1, len(L))]


def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


# 构建入堆出堆函数
def heap_in(heap, item):  # list,int
    heap.append(item)
    L = deque(heap)
    L.appendleft(0)
    # print(heap_sort(L))
    heap = heap_sort(L)
    return heap


def heap_out(heap, item):  # list,int
    heap.remove(item)
    L = deque(heap)
    L.appendleft(0)
    # print(heap_sort(L))
    heap = heap_sort(L)
    return heap


'''################Step-2 处理数据并计算天际线################'''
# 导入原始数据
data_pd = pd.DataFrame(rectangles)  ##,columns=['Li','Ri','Hi'])

# 处理左右顶点
dta1 = pd.DataFrame(data_pd.iloc[:, [0, 2]])
dta1.columns = ['x', 'h']
dta2 = pd.DataFrame(data_pd.iloc[:, [1, 2]])
dta2.columns = ['x', 'h']
# 为了标识左右顶点，将右顶点置为负数
dta2.h = -dta2.h

# 拼接左右顶点
data = pd.concat([dta1, dta2], axis=0)
# 排序
data = data.sort(columns=['x', 'h'], axis=0, ascending=True)

# 初始化堆
heap = []
skyline = []
# 地平线入堆
heap = heap_in(heap, 0)

# 生成天际线
for x, h in zip(data.x, data.h):
    print(x, h)
    tmp = heap[0]
    if h >= 0:
        # 左顶点入堆
        heap = heap_in(heap, -h)
    else:
        # 右顶点出堆
        heap = heap_out(heap, -(-h))
    if heap[0] != tmp:
        skyline.append([x, abs(tmp)])
        skyline.append([x, abs(heap[0])])

pd_skyline = pd.DataFrame(skyline)

'''###################Step-3  绘图及可视化####################'''


# 给定矩形坐标画图
def plot_ori_rec(rectangles):
    data_pd = pd.DataFrame(rectangles, columns=['Li', 'Ri', 'Hi'])
    l = len(rectangles)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim(0, max(data_pd.loc[:, 'Ri']) * 1.1)
    plt.ylim(0, max(data_pd.loc[:, 'Hi']) * 1.1)
    for rectangle, colorr in zip(rectangles, [x for x in 'rgb' * math.ceil(l / 3)][0:l]):
        Li = rectangle[0]
        Ri = rectangle[1]
        Hi = rectangle[2]
        # print(Li,Ri,Hi)
        rect = plt.Rectangle((Li, 0), Ri - Li, Hi, color=colorr, alpha=0.3)  # 'r', alpha = 0.3)#左下起点，长，宽，颜色，不透明度
        ax.add_patch(rect)
    plt.show()


plot_ori_rec(rectangles)
# 画出天际线顶点
plt.scatter(pd_skyline[0], pd_skyline[1], color='r')
# 画出天际线
plt.plot(list(pd_skyline[0]), list(pd_skyline[1]), color='black')