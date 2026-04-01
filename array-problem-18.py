s = "hello"
# convert string to list (because string is immutable)
s = list(s)

vowels = "aeiouAEIOU"

left = 0
right = len(s) - 1

while left < right:
    # move left if not vowel
    if s[left] not in vowels:
        left += 1
        continue

    # move right if not vowel
    if s[right] not in vowels:
        right -= 1
        continue

    # swap vowels
    s[left], s[right] = s[right], s[left]

    left += 1
    right -= 1

# convert back to string
result = "".join(s)

print(result)
