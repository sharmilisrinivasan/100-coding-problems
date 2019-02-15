from bisect import insort
t = int(raw_input())

output = []
for _ in range(t):
    final_cnt = 0
    n = int(raw_input())
    pos_pairs = []
    for _ in range(n):
        in_ = map(int,raw_input().split())
        insort(pos_pairs,(in_[0],in_[1]))
    start_, end_ = pos_pairs[0]
    for cur_start_, cur_end_,  in pos_pairs[1:]:
        if cur_start_ <= end_:
            end_ = max(cur_end_, end_)
        else:
            final_cnt += (end_-start_)+1
            start_, end_ = cur_start_, cur_end_
    final_cnt += (end_-start_)+1
    output.append(final_cnt)
    
for val_ in output:
    print val_