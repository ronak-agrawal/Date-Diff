__author__ = 'Ronak'

# Programming Exercise
# --------------------
#
# Design and develop a django application in which a user can:
#
#   -- Input two dates to find days difference.
#
#   	-- Implement daysDifference class to find gaps between two dates.
#   		-- In terms of years, months and days.
#        		-- Is there any leap year in-between?
#
#   -- Can save and share their result using permlink.
#   -- Can consume an API to do the same.
#
# Application should have:
#
#   -- db models and migration
#   -- form validations
#   -- appropriate error messages
#   -- respective unit tests
#   -- meaningful API endpoint
#
# An explanation for
#
#   -- time and space complexity
#   -- justification for selection of approach

class Dates(Models.model):
    # store the date as mm/dd/yyyy in str format
    date1 = models.strField(null=True,blank=True)
    date2 = models.strField(null=True,blank=True)
    diff = models.strField(null=True,blank=True)

    def __str__(self):
        return f'difference is {self.diff}'

    def calculateDiff(self):
        d1=self.date1
        d2=self.date2
        d1_splits=d1.split('/')
        d2_splits=d2.split('/')
        is_d1_leaf = True if d1_splits[2]%4 else False
        is_d2_leaf = True if d2_splits[2]%4 else False

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