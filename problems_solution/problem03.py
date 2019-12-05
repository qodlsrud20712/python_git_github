from typing import List


class Solution:
    def numUniqueemails(self, emails: List[str]) -> int:
        email_out, email_destroy, email_out_tmp, email_res = [], [], [], []
        res = {}

        [email_out.append(emails[i].split(sep='@')) for i in range(len(emails))]

        [email_destroy.append(email_out[i][0].replace('.', '').split(sep='+')) for i in range(len(email_out))]

        for i in range(len(email_destroy)):
            email_out[i][0] = email_destroy[i][0]

        [email_res.append(email_out[i][0] + '@' + email_out[i][1]) for i in range(len(email_out))]

        [res.update(linearSearch(email_res, email_res[i])) for i in range(len(email_res))]

        return len(res.keys())


def linearSearch(lst, key):
    cnt = 0
    res_dict = {}
    for i in range(len(lst)):
        if key == lst[i]:
           cnt +=1

    tmp_dict = {key:cnt}
    res_dict.update(tmp_dict)

    return res_dict




if __name__ == '__main__':
    sol = Solution()
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    res = sol.numUniqueemails(emails)

    print(res)


