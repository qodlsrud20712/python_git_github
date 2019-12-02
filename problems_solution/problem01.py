class Solution:
    def numJewelsInStones(self, J: str, S: str)->int:
        J_list = list(J)
        S_list = list(S)

        print(J_list)
        print(S_list)

        cnt = 0
        for i in range(len(J_list)):
            for j in range(len(S_list)):
                if J_list[i] == S_list[j]:
                    cnt += 1

        print(cnt)

        return cnt

if __name__ == '__main__':
    Test = Solution()

    Test.numJewelsInStones('aA', 'aAAbbbb')