class Solution(object):
    def average(self, salary):
        salary.sort()
        minsalary=salary[0]
        maxsalary=salary[-1]
        ave=(sum(salary)-minsalary-maxsalary)/float(len(salary)-2)
        return ave
        
