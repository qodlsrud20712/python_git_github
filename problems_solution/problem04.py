from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_out, arr_out2 = [], []


        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr_out.append(arr2[i])

        for i in arr1:
            if i not in arr2:
                arr_out2.append(i)

        arr_out2 = sorted(arr_out2)

        for i in arr_out2:
            arr_out.append(i)

        print(sorted(arr_out2))
        print(arr_out)
        return arr_out


if __name__ == '__main__':
    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6]


    #[2,2,2,1,4,3,3,9,6,7,19]

    Sol = Solution()

    Sol.relativeSortArray(arr1, arr2)


