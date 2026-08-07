from collections import Counter


class Solution:

  def smallestNumber(self, num: str, t: int) -> str:
    # Step 1: Prime factorize t into 2, 3, 5, 7
    temp_t = t
    prime_factors = {2: 0, 3: 0, 5: 0, 7: 0}
    for p in [2, 3, 5, 7]:
      while temp_t % p == 0:
        prime_factors[p] += 1
        temp_t //= p

    # If t has prime factors > 7 (like 11, 13), it's impossible
    if temp_t > 1:
      return "-1"

    # Helper: Convert prime count requirements into minimum needed digits (greedy combination)
    def get_min_digits(pf):
      cnt2, cnt3, cnt5, cnt7 = pf[2], pf[3], pf[5], pf[7]
      # Combine powers of 2 and 3 into larger digits: 8, 9, 6, 4
      d8 = cnt2 // 3
      r2 = cnt2 % 3

      d9 = cnt3 // 2
      r3 = cnt3 % 2

      d4 = r2 // 2
      r2 = r2 % 2

      d6 = 0
      if r2 == 1 and r3 == 1:
        r2, r3, d6 = 0, 0, 1

      if r3 == 1 and d4 == 1:
        r2, d6, r3, d4 = 1, 1, 0, 0

      digits = (
          [2] * r2
          + [3] * r3
          + [4] * d4
          + [5] * cnt5
          + [6] * d6
          + [7] * cnt7
          + [8] * d8
          + [9] * d9
      )
      return sorted(digits)

    # Helper to remove digit's prime factors from current requirements
    def sub_factors(pf, digit):
      res = pf.copy()
      d_pf = {2: 0, 3: 0, 5: 0, 7: 0}
      val = digit
      for p in [2, 3, 5, 7]:
        while val > 0 and val % p == 0:
          d_pf[p] += 1
          val //= p
      for p in [2, 3, 5, 7]:
        res[p] = max(0, res[p] - d_pf[p])
      return res

    n = len(num)
    first_zero = num.find("0")
    if first_zero == -1:
      first_zero = n

    # Prefix prime factor count of num
    pref_pf = {2: 0, 3: 0, 5: 0, 7: 0}
    for i in range(n):
      if num[i] == "0":
        break
      d = int(num[i])
      for p in [2, 3, 5, 7]:
        while d % p == 0 and d > 0:
          pref_pf[p] += 1
          d //= p

    # Check if num itself works
    if first_zero == n and all(pref_pf[p] >= prime_factors[p] for p in [2, 3, 5, 7]):
      return num

    # Try modifying at index i from right to left
    for i in range(n - 1, -1, -1):
      # Update prefix factors removing num[i]
      if i < first_zero:
        d = int(num[i])
        for p in [2, 3, 5, 7]:
          while d > 0 and d % p == 0:
            pref_pf[p] -= 1
            d //= p

      if i > first_zero:
        continue

      start_d = int(num[i]) + 1 if i < first_zero else 1
      space = n - 1 - i

      for bigger_digit in range(start_d, 10):
        req_pf = sub_factors(prime_factors, bigger_digit)
        for p in [2, 3, 5, 7]:
          req_pf[p] = max(0, req_pf[p] - pref_pf[p])

        needed_digits = get_min_digits(req_pf)
        if len(needed_digits) <= space:
          ones = space - len(needed_digits)
          suffix = "1" * ones + "".join(map(str, needed_digits))
          return num[:i] + str(bigger_digit) + suffix

    # If length n wasn't enough, extend to length n + 1
    needed_digits = get_min_digits(prime_factors)
    ones = (n + 1) - len(needed_digits)
    return "1" * max(0, ones) + "".join(map(str, needed_digits))