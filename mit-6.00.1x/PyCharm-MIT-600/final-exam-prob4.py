def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """

    # finde the longest run of monotonically increasing numbers in L

    def mIncreasing(L):
        current_set = L[:]
        temp_set = [current_set[0]]
        m_increasing = []

        for i in range(len(current_set) - 1):
            if current_set[i] <= current_set[i + 1]:
                temp_set.append(current_set[i + 1])
                if len(temp_set) > len(m_increasing):
                    m_increasing = temp_set[:]
            elif current_set[i] > current_set[i + 1]:
                temp_set = [current_set[i + 1]]
        return m_increasing

    # finde the longest run of monotonically decreasing numbers in L
    def mDecreasing(L):
        current_set = L[:]
        temp_set = [current_set[0]]
        m_decreasing = []
        for i in range(len(current_set) - 1):
            if current_set[i] >= current_set[i + 1]:
                temp_set.append(current_set[i + 1])
                if len(temp_set) > len(m_decreasing):
                    m_decreasing = temp_set[:]
            elif current_set[i] < current_set[i + 1]:
                temp_set = [current_set[i + 1]]
        return m_decreasing

    firstone = mIncreasing(L)
    secondone = mDecreasing(L)
    result = 0
    if len(firstone) > len(secondone) :
        for i in firstone:
            result += i
    elif len(firstone) == len(secondone) :
        for i in L:
            if sum(firstone) == sum(secondone):
                for r in firstone:
                    result += r
                break
            if i in firstone and not i in secondone:
                for j in firstone:
                    result += j
                break
            elif i in secondone and not i in firstone:
                for k in secondone:
                    result += k
                break

    elif len(firstone) < len(secondone):
        for i in secondone:
            result += i
    return result
