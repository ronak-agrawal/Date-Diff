__author__ = 'Ronak'

def calculateDiff(d1,d2):
    d1_splits=d1.split('/')
    d1_splits=[int(i) for i in d1_splits]
    d2_splits=d2.split('/')
    d2_splits=[int(i) for i in d2_splits]
    is_d1_leaf = True if int(d1_splits[2])%4 else False
    is_d2_leaf = True if int(d2_splits[2])%4 else False
    days_31=[1,3,5,7,8,10,12]
    days_30=[4,6,9,11]
    d_diff,m_diff,y_diff = 0,0,0
    if (d1_splits[1]>d2_splits[1]):
        d_diff = int(d1_splits[1]) - int(d2_splits[1])
    elif d1_splits[1]==d2_splits[1]:
        d_diff = 0
    else:
        days = 28
        if d2_splits[0]in days_31:
            days = d2_splits[1]+31
        elif d2_splits[0]in days_30:
            days = d2_splits[1]+30
        elif d2_splits[0]==2 and is_d2_leaf:
            days = 29
        d2_splits[0] -= 1
        d_diff = days - d1_splits[1]
        d1_splits[0] = d1_splits[0] -1
    if (d1_splits[0]<d2_splits[0]):
        d1_splits[2]-=1
        d1_splits[0]+=12
    m_diff = abs(int(d1_splits[0]) - int(d2_splits[0]))
    y_diff = abs(int(d1_splits[2]) - int(d2_splits[2]))
    return d_diff, m_diff,y_diff

if __name__ =='__main__':
   #   - 11/03/1994 : 03/09/2020 # (37, 8, 26)
   # - 12/12/1999 : 11/05/2004 #(7, 1, 5)
   # - 28/02/2009 : 25/09/2009 #(26, 3, 0)
   # - 16/04/2011 : 15/03/2010 #(1, 1, 1)
   # - 16/08/2013 : 11/02/2014 #(6, 5, 1)
    print(calculateDiff('28/02/2009','25/09/2009'))
    print(calculateDiff('16/04/2011','15/03/2010'))
    print(calculateDiff('16/08/2013','11/02/2014'))