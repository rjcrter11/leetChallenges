'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''


class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.part_of_island(i, j, grid)
        return islands

    def part_of_island(self, i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
        self.part_of_island(i, j+1, grid)
        self.part_of_island(i, j-1, grid)
        self.part_of_island(i+1, j, grid)
        self.part_of_island(i-1, j+1, grid)


island_array = [["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
                ]

island_counter = Solution()
print(island_counter.numIslands(island_array))
