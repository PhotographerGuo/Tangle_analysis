import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import math

#degree dict
# degree_dict = {1: 9, 2: 82116, 3: 4763050, 4: 2554460, 5: 1248128, 6: 506719, 7: 208594, 8: 100283, 9: 56675, 10: 33920, 11: 22336, 12: 15052, 13: 10621, 14: 7463, 15: 5686, 16: 4033, 17: 3138, 18: 2402, 19: 1908, 20: 1616, 21: 1245, 22: 1077, 23: 847, 24: 683, 25: 566, 26: 520, 27: 423, 28: 348, 29: 349, 30: 264, 31: 245, 32: 199, 33: 174, 34: 146, 35: 141, 36: 94, 38: 100, 39: 88, 41: 75, 45: 52, 51: 22, 54: 27, 55: 24, 110: 1, 40: 78, 42: 78, 43: 51, 44: 49, 57: 14, 62: 16, 74: 10, 75: 9, 85: 7, 37: 101, 46: 43, 47: 33, 48: 32, 49: 25, 50: 23, 52: 21, 53: 19, 56: 18, 58: 14, 59: 14, 60: 18, 61: 12, 63: 18, 64: 16, 66: 14, 67: 14, 69: 7, 70: 8, 71: 11, 72: 7, 76: 8, 78: 12, 80: 7, 82: 6, 86: 7, 88: 8, 89: 4, 90: 5, 92: 3, 93: 7, 95: 5, 96: 5, 97: 7, 99: 4, 100: 2, 101: 3, 102: 9, 104: 4, 105: 6, 106: 8, 108: 2, 114: 3, 122: 2, 128: 2, 138: 2, 140: 2, 143: 1, 144: 1, 146: 3, 149: 2, 195: 2, 68: 10, 73: 6, 77: 10, 83: 5, 84: 5, 87: 1, 91: 3, 94: 3, 111: 3, 112: 3, 115: 2, 118: 4, 119: 2, 120: 1, 123: 1, 124: 3, 127: 2, 129: 2, 130: 3, 135: 1, 136: 1, 147: 1, 152: 1, 158: 1, 161: 2, 167: 1, 173: 1, 188: 1, 190: 1, 194: 1, 203: 1, 204: 2, 206: 4, 517: 1, 217: 1, 226: 1, 230: 1, 232: 2, 246: 1, 253: 1, 258: 1, 265: 1, 294: 1, 305: 1, 340: 1, 398: 1, 506: 1, 65: 6, 79: 6, 81: 4, 1119: 1, 126: 2, 139: 1, 169: 1, 179: 1, 193: 1, 214: 1, 282: 1, 98: 2, 615: 1, 107: 5, 113: 2, 125: 2, 131: 1, 133: 2, 145: 1, 157: 1, 164: 1, 165: 1, 174: 1, 175: 1, 177: 1, 178: 1, 201: 1, 243: 1, 251: 1, 272: 1, 283: 1, 300: 1, 325: 1, 327: 1, 400: 1, 498: 1, 137: 1, 181: 1, 196: 1, 1364: 1, 1012: 1}

#in degree dict
# degree_dict = {1: 4826614, 2: 2567934, 3: 1251485, 4: 507785, 5: 208893, 6: 100475, 7: 56756, 8: 33955, 9: 22364, 10: 15058, 11: 10628, 12: 7463, 13: 5693, 14: 4035, 15: 3136, 16: 2399, 17: 1913, 18: 1615, 19: 1245, 20: 1078, 21: 847, 22: 683, 23: 566, 24: 518, 25: 425, 26: 348, 27: 347, 28: 266, 29: 244, 30: 200, 31: 174, 32: 146, 33: 141, 34: 94, 36: 100, 37: 88, 39: 76, 43: 52, 49: 22, 52: 27, 53: 24, 108: 1, 38: 77, 40: 78, 41: 51, 42: 49, 55: 14, 60: 16, 72: 10, 73: 9, 83: 7, 35: 101, 44: 43, 45: 33, 46: 32, 47: 25, 48: 23, 50: 21, 51: 19, 54: 18, 56: 14, 57: 14, 58: 18, 59: 12, 61: 18, 62: 16, 64: 14, 65: 14, 67: 7, 68: 8, 69: 11, 70: 7, 74: 8, 76: 12, 78: 7, 80: 6, 84: 7, 86: 8, 87: 4, 88: 5, 90: 3, 91: 7, 93: 5, 94: 5, 95: 7, 97: 4, 98: 2, 99: 3, 100: 9, 102: 4, 103: 6, 104: 8, 106: 2, 112: 3, 120: 2, 126: 2, 136: 2, 138: 2, 141: 1, 142: 1, 144: 3, 147: 2, 193: 2, 66: 10, 71: 6, 75: 10, 81: 5, 82: 5, 85: 1, 89: 3, 92: 3, 109: 3, 110: 3, 113: 2, 116: 4, 117: 2, 118: 1, 121: 1, 122: 3, 125: 2, 127: 2, 128: 3, 133: 1, 134: 1, 145: 1, 150: 1, 156: 1, 159: 2, 515: 1, 165: 1, 171: 1, 186: 1, 188: 1, 192: 1, 201: 1, 202: 2, 204: 4, 215: 1, 224: 1, 228: 1, 230: 2, 244: 1, 251: 1, 256: 1, 263: 1, 292: 1, 303: 1, 338: 1, 396: 1, 504: 1, 63: 6, 77: 6, 79: 4, 1117: 1, 124: 2, 137: 1, 167: 1, 177: 1, 191: 1, 212: 1, 280: 1, 96: 2, 613: 1, 105: 5, 111: 2, 123: 2, 129: 1, 131: 2, 143: 1, 155: 1, 162: 1, 163: 1, 172: 1, 173: 1, 175: 1, 176: 1, 199: 1, 241: 1, 249: 1, 270: 1, 281: 1, 298: 1, 323: 1, 325: 1, 398: 1, 496: 1, 135: 1, 179: 1, 194: 1, 1362: 1, 1010: 1}
degree_dict = {0: 1, 1: 644745, 2: 321033, 3: 154457, 4: 63408, 5: 29498, 6: 16967, 7: 10751, 8: 6644, 9: 4024, 10: 2497, 11: 1653, 12: 1087, 13: 741, 14: 470, 15: 312, 16: 193, 17: 150, 18: 90, 19: 77, 20: 57, 21: 62, 22: 33, 23: 25, 24: 24, 25: 20, 26: 18, 27: 9, 28: 12, 29: 9, 30: 11, 31: 12, 32: 3, 33: 6, 34: 4, 35: 2, 36: 4, 37: 4, 38: 3, 39: 2, 40: 3, 41: 6, 42: 2, 159: 1, 44: 3, 45: 1, 46: 2, 135: 1, 48: 1, 49: 1, 51: 2, 179: 1, 53: 2, 54: 2, 55: 1, 56: 3, 58: 1, 59: 1, 62: 1, 64: 2, 65: 2, 194: 1, 71: 1, 72: 2, 73: 1, 74: 1, 204: 1, 77: 1, 76: 1, 1362: 1, 84: 1, 87: 1, 92: 1, 97: 1, 100: 1, 102: 1, 105: 2, 1010: 1}

degree_num = list(degree_dict.keys())
degree_cout = list(degree_dict.values())


fig = plt.figure()
# ax1 = fig.add_subplot(121)
# plt.pie(y,labels = x,autopct= '%1.2f%%' )
plt.title("IRI_1.4.0")
plt.xlabel('In_degree num.')
plt.ylabel('percent')
#dram histogram
# log_list = []
# for i in list(in_degree_statistic.values()):
#     log_list.append(math.log(i))

# print(log_list)
# ax2 = fig.add_subplot(122)
# plt.bar(in_degree_statistic.keys(),log_list, fc = 'b')
# plt.show()

#degree distribution
# print(nx.degree_histogram(G))
# degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列
x = degree_num                             #生成x轴序列，从1到最大度
# y = degree_cout
y = [z / float(sum(degree_cout)) for z in degree_cout]
#将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
# ax3 = fig.add_subplot(122)

plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线


plt.show()                                                            #显示图表
