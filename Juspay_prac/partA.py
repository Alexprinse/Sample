import sys
from array import array

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    if not data:
        return
    
    try :
        N =  int(next(it))
    except StopIteration:
        return
    m = int(next(it))
    Q = int(next(it))

    intern = sys.intern

    name_to_idx = {}
    for i in range(N):
        name = intern(next(it).decode())
        name_to_idx[name] = i

    locked_by = array('I',[0]) * N
    locked_desc = array('I',[0]) * N

    def any_ans_lock(idx):
        lb = locked_by
        p = (idx - 1) // m if idx != 0 else -1
        while p != -1:
            if lb[p] != 0:
                return True
            p = (p - 1)// m if p != 0 else -1
        return False
    
    def inc_ans(idx,delt):
        ld = locked_desc
        p = (idx - 1) // m if idx != 0 else -1
        if delt == 1:
            while p != -1:
                ld[p] += 1
                p = (p - 1)// m if p != 0 else -1
        else:
            while p != -1:
                ld[p] -= 1
                p = (p - 1)// m if p != 0 else -1

    def child(idx):
        start = idx * m + 1
        end = start + m
        if end > N:
            end = N
        for c in range(start,end):
            yield c


    lb = locked_by
    ld = locked_desc

    outline = []

    for _ in range(Q):
        op = int(next(it))
        node_name = sys.intern(next(it).decode())
        uid = int(next(it))

        idx = name_to_idx.get(node_name)
        if idx is None:
            outline.append("false")
            continue

        if op == 1:
            if lb[idx] != 0 or ld[idx] > 0 or any_ans_lock(idx):
                outline.append("false")
            else:
                lb[idx] = uid
                inc_ans(idx,1)
                outline.append("true")

        elif op == 2:
            if lb[idx] != uid:
                outline.append("false")
            else:
                lb[idx] = 0
                inc_ans(idx,-1)
                outline.append("true")

        elif op == 3:
            if lb[idx] != 0 or ld[idx] == 0 or any_ans_lock(idx):
                outline.append("false")
                continue

            stack = [idx]
            locked_n = []
            valid = True
            while stack and valid:
                node = stack.pop()
                if node != idx and lb[node] != 0:
                    if lb[node] != uid:
                        valid = False
                        break
                    locked_n.append(node)
                if lb[node] == 0 and ld[node] == 0:
                    continue
                for c in child(node):
                    stack.append(c)

            if not valid:
                outline.append("false")
                continue

            for ln in locked_n:
                if lb[ln] == 0:
                    continue
                lb[ln] = 0
                inc_ans(ln,-1)

            lb[idx] = uid
            inc_ans(idx,1)
            outline.append("true")
        else:
            outline.append("false")

    sys.stdout.write("\n".join(outline))
if __name__ == "__main__":
    main()

            



