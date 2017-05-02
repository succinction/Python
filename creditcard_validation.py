# ##### Instructions
#
# 1. Slice off the last digit.  That is the **check digit**.
# 2. Reverse the digits.
# 3. Double every other element in the reversed list.
# 4. Subtract nine from numbers over nine.
# 5. Sum all values.
# 6. Take the second digit of that sum.
# 7. If that matches the check digit, the whole card number is valid.
#
# For example, the worked out steps would be:
#
# ```
# 1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
# 2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
# 3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
# 4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
# 5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
# 6. 85
# 7. 5
# 8. Valid!
# ```


ccnum = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"
dgts = ccnum.split(' ')
check_dgt = int(dgts.pop())
# print(check_dgt)
dgts.reverse()
dbl_rev_dgt = [int(dgts[x])*2 if x % 2 == 0 else int(dgts[x]) for x in range(len(dgts))]
# print(dbl_rev_dgt )
minine = [dg - 9 if dg > 9 else dg for dg in dbl_rev_dgt]
sumnine = sum(minine)
chk = int(str(sumnine)[1])
print(chk == check_dgt)