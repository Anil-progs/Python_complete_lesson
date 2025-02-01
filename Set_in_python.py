
set
    #it will avoid from repetition, set is {},we will use from set in Data Sciance for delete the repetite data
    ex:
        list={"anil","anil","ahmad"}
        print(list)
        >>>{'anil','ahmad'}
        
        list={"anil","anil","ali","ahmad"}
        print(list)            >>>{'anil', 'ahmad', 'ali'}
        list.add("hkjkh")
        print(list)     >>>{'anil', 'hkjkh', 'ahmad', 'ali'}
        #if something is repeate it will write it
        list.add("anil")
        print(list)     >>>{'anil', 'hkjkh', 'ahmad', 'ali'}

        # it is range 
            list[0]       >>> 'set' object is not subscriptable
    
        a={1,2,3,4,5,6}
        b={3,4,7,8,9,1,3}
        print(a.difference(b))  >>>{2, 5, 6}
        print(b.difference(a))    >>>{8, 9, 7}
    #only show those numbers that not repeate to both sets
        a={1,2,3,4,5,7}
        b={3,4,7}
        a.difference_update(b)
        print(a)   >>>{1, 2, 5}

    # to remove one item from set
        a={1,2,3,4,5,7}
        a.discard(7)
        print(a)     >>>{1, 2, 3, 4, 5}
    #repeate item in both sets
        a={1,2,3,4,5,7}
        b={3,4,7,765}
        print(a.intersection(b))   >>>{3, 4, 7}
    #only get those number which is repeate to both steps
        a={1,2,3,4,5,7}
        b={3,4,7}
        a.intersection_update(b)
        print(a)  >>{1,2,5}
    #some mothods of set
        S1={1,2,3,4,5}
        S2={8,9,10,7}
        print(S1.isdisjoint(S2))
       >>>True

        S1={1,2,3,4,5,6,7,8,9}
        S2={8,9,10,7}
        print(S1.issubset(S2))    >>>False

        S1={1,2,3,4,5,6,7,8,9}
        S2={8,9,10,7}
        print(S1.issuperset(S2))   >>>False

        S1={1,2,3,4,5,6,7,8,9}
        S2={8,9,10,7}
        S1.pop()   # in set pop will delete from beginning 
        print(S1)    >>>{2, 3, 4, 5, 6, 7, 8, 9}


        S1={1,2,3,4,5,6,7,8,9}
        S2={8,9,10,7}       #union in set will jain two set create new set and avoid from repeate number
        print(S1.union(S2))   >>>{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


        S1={1,2,3,4,5,6,7,8,9}
        S2={8,9,10,7}       
        S1.update(S2)  from S2 bring new item in S1
        print(S1)>>>  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

        S1={1,2,3,4,5,6,7,8,9}
        S2={8,9,10,7,4,3,2}       
        print(S1.symmetric_difference(S2))  >>>{1, 5, 6, 10}

        set={45,444456,34,23,23,12,23,35,2,3,5,6,78,12}
        set2={23,35,2,3,5,6,78,12}
        set.symmetric_difference_update(set2)
        print(set)
        >>>{34, 444456, 45}