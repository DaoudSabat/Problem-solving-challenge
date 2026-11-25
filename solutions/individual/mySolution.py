def countPairs(nums, target):
    seen = {}
    count = 0
    for num in nums(len(nums)):
        needed = target - num
        if needed in seen:
            count += seen[needed]
        if nums[num] in seen:
            seen[nums[num]] += 1
        else:
            seen[nums[num]] = 1
    return count

def brute_force(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                count += 1
    return count


if __name__ == "__main__":
    # Examples from the problem
    assert countPairs([1, 5, 7, -1, 5], 6) == 3
    assert countPairs([3, 3, 3], 6) == 3

    # Edge cases
    assert countPairs([], 6) == 0                      # empty input
    assert countPairs([6], 6) == 0                     # single element
    assert countPairs([1, 2, 3], 100) == 0             # no pairs
    assert countPairs([0, 0, 0, 0], 0) == 6            # all equal
    assert countPairs([-1, -2, -3, 4], -3) == 1        # negatives
    assert countPairs([10**9, -10**9], 0) == 1         # bounds
    assert countPairs([10**9, 10**9], 2 * 10**9) == 1  # sum beyond 32-bit

    # Input must not be modified
    data = [1, 5, 7, -1, 5]
    countPairs(data, 6)
    assert data == [1, 5, 7, -1, 5]

    # Largest input, answer bigger than 32-bit
    n = 200000
    assert countPairs([1] * n, 2) == n * (n - 1) // 2

    # Random arrays compared against the slow version
    import random
    for _ in range(500):
        arr = [random.randint(-5, 5) for _ in range(random.randint(0, 30))]
        t = random.randint(-10, 10)
        assert countPairs(arr, t) == brute_force(arr, t)

    print("All tests passed")