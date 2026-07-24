# Naive Search
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print("Pattern found at index", i)
# KMP Failure Function
def kmp_failure_function(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps
# KMP Search
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = kmp_failure_function(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
# Rabin-Karp
def rabin_karp(text, pattern, q=101):
    n = len(text)
    m = len(pattern)
    d = 256
    h = pow(d, m - 1, q)
    pattern_hash = 0
    text_hash = 0
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q
    for s in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[s:s + m] == pattern:
                print("Pattern found at index", s)
        if s < n - m:
            text_hash = (d * (text_hash - ord(text[s]) * h) + ord(text[s + m])) % q
            if text_hash < 0:
                 text_hash += q
# Main Program
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

print("\nNaive Search:")
naive_search(text, pattern)

print("\nKMP Search:")
kmp_search(text, pattern)

print("\nRabin-Karp Search:")
rabin_karp(text, pattern)