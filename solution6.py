import common

N = 256
lines = common.get_lines(__file__)
numbers = [int(_) for _ in lines[0].split(',')]

dp = [0] * N
# f(0, 80) = f(6, 79) + f(8, 79) = f(0, 73) + f (0, 71)
# f(80) = f(73) + f(71)
# Recursive: f(N) = f(N - 7) + f(N - 9)
# Initial: f(0) -- f(6) -> 2, f(7) -- f(9) -> 3
# for i in range(7): dp[i] = 2
# for i in range(7, 9): dp[i] = 3
# for i in range(9, N): dp[i] = dp[i - 7] + dp[i - 9]

for i in range(N):
    def get_dp(index):
        return 1 if index < 0 else dp[index]
    dp[i] = get_dp(i - 7) + get_dp(i - 9)


def part_one():
    return sum(dp[N - 1 - n] for n in numbers)

#Part two, just update N to 256
