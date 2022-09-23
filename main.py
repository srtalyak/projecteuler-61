# This program is a solution for
# Project Euler Problem 61
# https://projecteuler.net/problem=61

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
# is represented by a different number in the set.


from itertools import permutations


def main():
    def listChoice(formulaNumber):
        if formulaNumber == "3":
            return triangles
        if formulaNumber == "4":
            return squares
        if formulaNumber == "5":
            return pentagonals
        if formulaNumber == "6":
            return hexagonals
        if formulaNumber == "7":
            return heptagonals
        if formulaNumber == "8":
            return octagonals

    # converting to string for ease of operation
    # I set all ranges only for 4-digits numbers
    triangles = [str(n * (n + 1) // 2) for n in range(45, 141)]
    squares = [str(n ** 2) for n in range(32, 100)]
    pentagonals = [str(n * (3 * n - 1) // 2) for n in range(26, 82)]
    hexagonals = [str(n * (2 * n - 1)) for n in range(23, 71)]
    heptagonals = [str(n * (5 * n - 3) // 2) for n in range(21, 64)]
    octagonals = [str(n * (3 * n - 2)) for n in range(19, 59)]

    # we don't know what order polygonal types are in
    for permutation in permutations(list("345678"), 6):  # this line tries every order of polygonal type
        for firstListItems in listChoice(permutation[0]):
            firstTwoOf1 = firstListItems[:2]
            lastTwoOf1 = firstListItems[2:]

            for secondListItems in listChoice(permutation[1]):
                firstTwoOf2 = secondListItems[:2]
                if lastTwoOf1 != firstTwoOf2:
                    continue
                lastTwoOf2 = secondListItems[2:]

                for thirdListItems in listChoice(permutation[2]):
                    firstTwoOf3 = thirdListItems[:2]
                    if lastTwoOf2 != firstTwoOf3:
                        continue
                    lastTwoOf3 = thirdListItems[2:]

                    for fourthListItems in listChoice(permutation[3]):
                        firstTwoOf4 = fourthListItems[:2]
                        if lastTwoOf3 != firstTwoOf4:
                            continue
                        lastTwoOf4 = fourthListItems[2:]

                        for fifthListItems in listChoice(permutation[4]):
                            firstTwoOf5 = fifthListItems[:2]
                            if lastTwoOf4 != firstTwoOf5:
                                continue
                            lastTwoOf5 = fifthListItems[2:]

                            for sixthListItems in listChoice(permutation[5]):
                                firstTwoOf6 = sixthListItems[:2]
                                if lastTwoOf5 != firstTwoOf6:
                                    continue
                                lastTwoOf6 = sixthListItems[2:]

                                if lastTwoOf6 == firstTwoOf1:
                                    cyclicSet = [int(i) for i in (
                                        firstListItems, secondListItems, thirdListItems,
                                        fourthListItems, fifthListItems, sixthListItems)]
                                    print(cyclicSet)
                                    print(sum(cyclicSet))
                                    return


main()
