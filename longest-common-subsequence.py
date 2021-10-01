def longestCommonSubsequence(text1: str, text2: str) -> int:
    index = 0
    seq = ''
    seq_max = ''

    shorter_str = ''
    longer_str = ''

    if len(text1) >= len(text2):
        longer_str = text1
        shorter_str = text2
    else:
        longer_str = text2
        shorter_str = text1

    for j in range(len(shorter_str)):
        for i in range(j, len(shorter_str)):
            if longer_str.find(shorter_str[i], index) != -1:
                seq += shorter_str[i]
                index = shorter_str.find(longer_str[i], index) + 1
        print(seq)
        if len(seq) > len(seq_max):
            seq_max = seq
        seq = ''
        index = 0

    print(seq_max)
    return len(seq_max)


# text1 = "abcde"
# text2 = "ace"

# text1 = "abc"
# text2 = "abc"

# text1 = "abc"
# text2 = "def"
# text1 = "bsbininm"
# text2 = "jmjkbkjkv"

text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"

print(longestCommonSubsequence(text1=text1, text2=text2))
