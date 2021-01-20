d1= {'a':{'b':{'cs':10},'d':{'cs':20}}}
d2= {'a':{'b':{'cs':30} ,'d':{'cs':20}},'newa':{'q':{'cs':50}}}

class Diff:
    added = []
    removed = []
    changed = []

def diff_dict(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys

    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same

def diff_list(l1:list,l2:list):
    d = set(l1)-set(l2)
    c = set(l1) & set(l2)
    print(d)
    print(c)

a = {

}
b = {

}

if __name__ == '__main__':
   x = diff_dict(a,b)
   print(x)


