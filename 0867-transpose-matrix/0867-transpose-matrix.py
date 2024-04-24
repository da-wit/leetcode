class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        s= []
        for i in range(len(matrix[0])):
            n = []
            for j in matrix:
                n.append(j[i])
            s.append(n)
        return s
























        # if len(matrix) == len(matrix[0]):
        #     for i in range(len(matrix)):
        #         for j in range(i + 1, len(matrix)):
        #             matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # else:
        #     new = []
        #     for j in range(len(matrix[0])):
        #         new1 = []
        #         for i in range(len(matrix)):
        #             new1.append(matrix[i][j])
        #         new.append(new1)
        #     return new

        # return matrix
        

        