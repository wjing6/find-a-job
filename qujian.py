

    def merge(intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()  # 下标从左到右排列

        # 找到最大下标，用它构建我们的0数组
        upper = 0
        for l, u in intervals:
            upper = max(u, upper)

        zeros = [0] * (upper + 1)
        ret = []

        for l, u in intervals:
            for i in range(l, u + 1):  # 涂色
                zeros[i] += 1
            if sum(zeros[l:u + 1]) > (u - l + 1):  # 有重合，更新区间
                mi = min(ret[-1][0], l)
                ma = max(ret[-1][1], u)
                ret[-1] = [mi, ma]
            else:
                # 没有重合，直接添加
                ret.append([l, u])

        return ret
