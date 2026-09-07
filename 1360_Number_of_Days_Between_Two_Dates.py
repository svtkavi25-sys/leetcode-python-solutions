from datetime import datetime
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        format_str = "%Y-%m-%d"
        d1 = datetime.strptime(date1, format_str)
        d2 = datetime.strptime(date2, format_str)
        return abs((d2 - d1).days)
