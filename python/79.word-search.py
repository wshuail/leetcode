#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (45.16%)
# Total Accepted:    184.5K
# Total Submissions: 408.3K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n = board[i].length
# 1 
# 1 
# board 和 word 仅由大小写英文字母组成
# 
# 
# 
# 
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])
        mark = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.dfs(i, j, m, n, mark, board, word[1:])==True:
                        return True
                    else:
                        mark[i][j] = 0
        return False

    def dfs(self, i, j, m, n, mark, board, word):
        if len(word)==0:
            return True

        for direction in self.directions:
            cur_i = i+direction[0]
            cur_j = j+direction[1]
            if 0 <= cur_i < m and 0 <= cur_j < n and board[cur_i][cur_j]==word[0]:
                if mark[cur_i][cur_j]:
                    continue
                mark[cur_i][cur_j] = 1
                if self.dfs(cur_i, cur_j, m, n, mark, board, word[1:])==True:
                    return True
                else:
                    mark[cur_i][cur_j] = 0

        return False


