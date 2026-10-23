class TimeMap:

    def __init__(self):
        self.timeM = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeM[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeM.get(key, [])
        #print("values",values)
        l, r = 0, len(values) - 1
        m =0 
        prev_t = 0
        while l<=r:
            m = (l+r)//2
            # print("m", m)
            # print("valuesm", values[m])
            if values[m][0] == timestamp:
                return values[m][1]
            elif  values[m][0] > timestamp:
                r = m- 1
            elif  values[m][0] < timestamp:
                res = values[m][1]
                prev_t = values[m][0]
                l = m+ 1
        # print("m-", m)
        # print("values-",values)
        return res if prev_t <= timestamp else ""




        
