
from typing import List, Tuple, Dict, Any, Union

def solve() -> None:
    M = {}
    v = ["TOI", "Hindu", "ET", "BM", "HT"]
    M["TOI"] = 26
    M["Hindu"] = 20.5
    M["ET"] = 34
    M["BM"] = 10.5
    M["HT"] = 18
    n = int(input())
    ansset = set()
    def helper(helper: "function", ind: int, sum_rem: int, taken_ind: List[int]) -> None:
        # base
        if ind == 5:
            ansset.add(tuple(taken_ind))
            return
        cur = M[v[ind]]
        if cur <= sum_rem:
            taken_ind.append(ind)
            helper(helper, ind + 1, sum_rem - cur, taken_ind)
            taken_ind.pop()
        helper(helper, ind + 1, sum_rem, taken_ind)

    vv = []
    helper(helper, 0, n, vv)
    flag = 0
    for it in ansset:
        t = list(it)
        if len(t) > 1:
            if flag > 0:
                print(",", end="")
            print("{", end="")
            for i in range(len(t)):
                print(f'"{v[t[i]]}"', end="")
                if len(t) - 1 != i:
                    print(",", end="")
            print("}", end="")
            flag = 1

solve()