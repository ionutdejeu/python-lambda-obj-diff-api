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
    # add extra rule, the objects that are modified, will have their own difference made
    # only one level of nested objects
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}

    same = set(o for o in shared_keys if d1[o] == d2[o])
    for modified_index in modified:
        print(modified_index)
        if isinstance(d1[modified_index], dict):
            print(d1[modified_index])
            a,r,m,s= diff_dict(d1[modified_index],d2[modified_index])
            print(a,r,m,s)
        if isinstance(d1[modified_index],list):
            a,r = diff_list(d1[modified_index],d2[modified_index])
            print(a,r)
    return added, removed, modified, same

def diff_list(l1:list,l2:list):
    added = [item for item in l1 if item not in l2]
    removed = [item for item in l2 if item not in l1]
    obj_to_cmp = [item for item in l1+l2 if isinstance(item, dict)]
    print(obj_to_cmp)
    return added,removed

a = {"x":[{'unique_id':'001', 'key1':'AAA', 'key2':'BBB', 'key3':'EEE'},
              {'unique_id':'002', 'key1':'AAA', 'key2':'CCC', 'key3':'FFF'}]}

b = {"x":[{'unique_id':'001', 'key1':'AAA', 'key2':'DDD', 'key3':'EEE2'},
              {'unique_id':'002', 'key1':'AAA', 'key2':'CCC', 'key3':'FFF'}]}
c = {"x":{'unique_id':'001', 'key1':'AAA', 'key2':'BBB', 'key3':'EEE'}}

d = {"x":{'unique_id':'001', 'key1':'AAA', 'key2':'DDD', 'key3':'EEE2'}}

if __name__ == '__main__':
    x = diff_dict(a,b)
    print(x)
