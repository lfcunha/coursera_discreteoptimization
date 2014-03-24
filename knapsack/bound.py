from numpy import array
#v=[8,10,15,4]
#w=[4,5,8,3]
#c=11

w=[5,8,3]
v=[45,48,35]
c=10

items=[]
for x in range(len(w)):
    items.append((w[x],v[x],x))
#print items
items=sorted(items, key=lambda item: item[1]/float(item[0]), reverse=True)
#print items

def maxEstimate(items,c,uLevel=0,uProfit=0, uWeight=0):
    #v=array(v[uLevel:])
    #w=[float(x) for x in array(w[uLevel:])]
    #f=v/w
    #s=sorted(v/w, reverse=True)
    #s1=[x for x in s]
    #f1=[x for x in f]

    #print s1
    #print f1
    #order = [f1.index(s1[x]) for x in range(len(s1))]
    #print order
    tw=uWeight
    val=uProfit
    print items
    for item in items[0:]:
            #print item
            #print v[order[x]]
            w=item[0]
            v=item[1]
            tw=tw+w
            val=val+v

            if tw>c:
                #print tw
                tw=tw-w
                val=val-v
                #print val
                dif=c-tw
                #print dif
                frac=dif/float(w)
                val+=frac*v
                break
            #print val
    return int(val)

print "max " + str(maxEstimate(items,c, 0,0,0))
