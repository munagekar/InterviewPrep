

# lps: longest proper prefix which is suffix
def cal_lps(pat):
    j = 0
    i = 1
    lps = [0]
    while i < len(pat):
        if pat[i] == pat[j]:
            i += 1
            j += 1
            lps.append(j)

        else:
            if j == 0:
                i += 1
                lps.append(0)
            # Some of the work has been already done
            # So can we use that work ?
            # This is the basic speedup in KMP
            else:
                j = lps[j - 1]
    return lps


def search(text, pat):
    lps = cal_lps(pat)
    j = 0   # Char to be matched
    i = 0
    indices = []
    while i < len(text):
        if text[i] == pat[j]:
            i += 1
            j += 1

        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

        if j == len(pat):
            indices.append(i - j)
            j = lps[j - 1]

    return indices


pat = "ABABCABAB"
text = "ABABDABACDABABCABAB"
print cal_lps(pat)
print search(text, pat)
