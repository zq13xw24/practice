# class Solution(object):
#
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if not s:
#             return ''
#         # 先将任一单个字母作为结果
#         start = 0
#         maxlen = 1
#         dp = [[0 for __ in range(len(s))] for __ in range(len(s))]
#         # 将长度1和长度2（相同字母）情况初始化赋值
#         for i in range(len(s)):
#             dp[i][i] = 1
#             if (i < len(s) - 1) and (s[i] == s[i+1]):
#                 dp[i][i+1] = 1
#                 start = i
#                 maxlen = 2
#         # for line in dp:
#         #     print line
#         # 注意：不可横向遍历，否则例如abcba，是无法先将bcb置为1的，进而无法将abcba置为1
#         # 从长度3开始
#         for length in range(3, len(s)+1):
#             for i in range(len(s)-length+1):
#                 j = i + length - 1
#                 if (dp[i+1][j-1] == 1) and s[i] == s[j]:
#                     dp[i][j] = 1
#                     if length > maxlen:
#                         start = i
#                         maxlen = length
#         # for line in dp:
#         #     print line
#         return s[start:start+maxlen]


# class Solution(object):
# #     def longestPalindrome(self, s):
# #         """
# #         :type s: str
# #         :rtype: str
# #         """
# #         # 使用动态规划，用空间换时间，把问题拆分
# #         # 获取字符串s的长度
# #         str_length = len(s)
# #         # 记录最大字符串长度
# #         max_length = 0
# #         # 记录位置
# #         start = 0
# #         # 循环遍历字符串的每一个字符
# #         for i in range(str_length):
# #             # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
# #             if i - max_length >= 1 and s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1]:
# #                 # 记录当前开始位置
# #                 start = i - max_length - 1
# #                 # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
# #                 max_length += 2
# #                 continue
# #             # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
# #             if i - max_length >= 0 and s[i-max_length: i+1] == s[i-max_length: i+1][::-1]:
# #                 start = i - max_length
# #                 # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
# #                 max_length += 1
# #         # 返回最长回文子串
# #         return s[start: start + max_length]
# #
# #
# # if __name__ == '__main__':
# #     s = "babad"
# #     # s = "cbbd"
# #     sl = Solution()
# #     print(sl.longestPalindrome(s))


# s = input()
# l = []
# for i in s:
#     l.append(i)
# def max_string_count(s):
#     list1 = []
#     for i in s:
#
#         count_max = s.count(i)
#
#         list1.append(count_max)
#     num = max(list1)
#     return num
#
# if __name__ == "__main__":
#     print(max_string_count(l))

# s = input()
# def cut(s):
#     res = []
#     for i in range(len(s)):
#         for j in range(len(s)-i):
#             if i == 0:
#                 res.append(s[j:j+i+1])
#             elif i < 2:
#                 for x in range(len(s)-i-j):
#                     res.append(s[j] + s[i+j+x])
#             else:
#                 for x in range(len(s) - i - j):
#                     res.append(s[j:i+j] + s[i+j+x])
#     return res
#
# if __name__ == "__main__":
#     res = cut(s)
#     max = 0
#     for i in res:
#         if res.count(i) > max:
#             max = res.count(i)
#     print(max)

s = input()
def cut(s):
    res = []
    for i in range(len(s)):
        for j in range(len(s)-i):
            res.append(s[j:j+i+1])
    return res
if __name__ == "__main__":
    res = cut(s)
    max_v = 0
    for i in res:
        if res.count(i) > max_v:
            max_v = res.count(i)
    print(max_v)










