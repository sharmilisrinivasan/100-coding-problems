def solve(in_str, out_str):
    if not in_str:
        return out_str

    len_ = len(in_str)
    if len_ == 1:
        return out_str+in_str

    mid_idx = (len_//2)
    if len_ % 2 == 0:
        mid_idx = mid_idx-1

    to_return = solve(in_str[(mid_idx+1):], out_str+in_str[mid_idx])
    return solve(in_str[:mid_idx], to_return)


n = int(input())
to_print = []
for _ in range(n):
    str_len = int(input())
    str_ = input()
    to_print.append(solve(str_, ""))

for val in to_print:
    print(val)
