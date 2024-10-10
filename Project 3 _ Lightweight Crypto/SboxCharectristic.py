def anf(s):
    s = list(s)
    for i in range(n):
        for j in range(0, 2**n, 2*2**i):
            for o in range(2**i):
                s[j+o+2**i] ^= s[j+o]
    return s


def size_reduce(lst):
    res = set()
    for u in lst:
        if not any(u != v and u & v == v for v in lst):
            res.add(u)
    return sorted(res)

def expand(lst):
    res = set()
    for v in range(2**n):
        if any(v & u == u for u in lst):
            res.add(v)
    return sorted(res)

def lessthan_set(u,n):
    set_out=set()
    for i in range(n):
        mask=2**i
        if u & mask == mask:
            u_i=u & (mask ^ (2**n-1))
            set_out.add(u_i)
            set_out.update(lessthan_set(u_i,n))
    return set_out

def hammingweight(i):
    i_b=bin(i)
    i_b=i_b[2:]
    i_hw=sum([int(j) for j in i_b])
    return i_hw

n = 4


# craft sbox:
# =============================================================================
sbox=[[12,10,13,3,14,11,15,7,8,9,1,5,0,2,4,6]]
# =============================================================================

# LED sbox:
# =============================================================================
# sbox=[[12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]]
# =============================================================================

# TWINE sbox:
# =============================================================================
# sbox=[[12,0,15,10,2,11,9,5,8,3,13,7,1,14,6,4]] 
# =============================================================================


hw=[[] for i in range(n+1)]
for u in range(2**n):
    u_b=bin(u)
    u_b=u_b[2:]
    hw[sum([int(j) for j in u_b])].append(u)
    
    
    
for Sbox in sbox:
    # calculate ANFs of products
    dppt = [set() for u in range(2**n)]
    for v in range(2**n):
        a = anf([int(y & v == v) for y in Sbox])
        for u, take in enumerate(a):
            if take:
                dppt[u].add(v)
    
    # propagate larger monomials to smaller ones
    for u1 in range(2**n):
        for u2 in range(u1):
            if u2 & u1 == u2:  # u2 \prec u1
                dppt[u2] = dppt[u2] | dppt[u1]
    
    # remove redundant ones
    dppt = [size_reduce(lst) for lst in dppt]
    print("\nValid input-output division trails:")
    for u, lst in enumerate(dppt):
        print(f"{u:04b}:", *[f"{v:04b}" for v in lst])
    
    
    
    dp=[n for i in range(n+1)]    
    
    for i in range(len(dppt)):
        i_hw=hammingweight(i)
        for j in range(len(dppt[i])):
            lessthanset=lessthan_set(dppt[i][j], n)
            
            dp_=0
            for p in range(len(hw)):
                cond=True
                for q in range(len(hw[p])):
                    if hw[p][q] in lessthanset:
                        continue
                    else:
                        cond=False
                        break
                if cond:
                    dp_+=1
                else:
                    break
            
            if dp_<dp[i_hw]:
                dp[i_hw]=dp_
        