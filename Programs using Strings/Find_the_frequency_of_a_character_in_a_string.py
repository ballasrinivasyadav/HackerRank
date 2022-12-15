
# Find the frequency of a character in a string

str1 = "python"
all_freq = {}
for i in str1:
    if i in all_freq:
        all_freq[i]=+1
    else:
        all_freq[i]=1
print(all_freq)