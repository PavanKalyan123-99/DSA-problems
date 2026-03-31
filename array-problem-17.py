s = "A man, a plan, a canal: Panama"

left = 0
right = len(s) - 1

while left < right:
    # skip left if not letter/number
    if not s[left].isalnum():
        left += 1
        continue

    # skip right if not letter/number
    if not s[right].isalnum():
        right -= 1
        continue

    # compare (ignore case)
    if s[left].lower() != s[right].lower():
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)