from typing import List


class Solution:
    def numUniqueemails(self, emails: List[str]) -> int:
        email_out, email_destroy, email_out_tmp, email_res = [], [], [], []

        for i in range(len(emails)):
            email_out.append(emails[i].split(sep='@'))

        i = 0

        while 1:
            if i >= len(email_out):
                break
            if len(email_out[i][1].split(sep='.')) > 2:
                email_out.remove(email_out[i])
                email_out_tmp = email_out
            i += 1

        for i in range(len(email_out_tmp)):
            email_destroy.append(email_out[i][0].replace('.', '').split(sep='+'))

        for i in range(len(email_out_tmp)):
            email_out[i][0] = email_destroy[i][0]

        for i in range(len(email_out_tmp)):
            email_res.append(email_out[i][0] + '@' + email_out[i][1])

        res = len(email_res)

        return res


if __name__ == '__main__':
    emails = ["fg.r.u.uzj+o.pw@kziczvh.com", "r.cyo.g+d.h+b.ja@tgsg.z.com", "fg.r.u.uzj+o.f.d@kziczvh.com",
              "r.cyo.g+ng.r.iq@tgsg.z.com", "fg.r.u.uzj+lp.k@kziczvh.com", "r.cyo.g+n.h.e+n.g@tgsg.z.com",
              "fg.r.u.uzj+k+p.j@kziczvh.com", "fg.r.u.uzj+w.y+b@kziczvh.com", "r.cyo.g+x+d.c+f.t@tgsg.z.com",
              "r.cyo.g+x+t.y.l.i@tgsg.z.com", "r.cyo.g+brxxi@tgsg.z.com", "r.cyo.g+z+dr.k.u@tgsg.z.com",
              "r.cyo.g+d+l.c.n+g@tgsg.z.com", "fg.r.u.uzj+vq.o@kziczvh.com", "fg.r.u.uzj+uzq@kziczvh.com",
              "fg.r.u.uzj+mvz@kziczvh.com", "fg.r.u.uzj+taj@kziczvh.com", "fg.r.u.uzj+fek@kziczvh.com"]

    Sol = Solution()
    print(Sol.numUniqueemails(emails))
