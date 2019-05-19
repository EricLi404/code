# coding=utf-8
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    """
    solution 1 by EricLi
    遍历法
    运行时间：292ms
    占用内存：5752k
    """

    def Find(self, target, array):
        while len(array) > 0:
            if len(array[-1]) > 0 and target < array[-1][0]:
                array.pop()
            else:
                for a in array[-1]:
                    if a == target:
                        return True
                array.pop()
        return False


sl = Solution()
tar = 6
# array = [
#     [1, 2, 3, 4, 5],
#     [3, 4, 5, 7, 8],
#     [7, 8, 9],
#     [10, 11, 13]
# ]
array = [[]]

print sl.Find(tar, array)
