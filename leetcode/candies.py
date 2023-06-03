def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        maxcandy = max(candies)
        booleanlist = []
        for i in range(len(candies)):
            if candies[i] + extraCandies > maxcandy:
                booleanlist.append(True)
            else:
                booleanlist.append(False)
        return booleanlist

candies = [2,3,5,1,3]
print(kidsWithCandies(candies,3))