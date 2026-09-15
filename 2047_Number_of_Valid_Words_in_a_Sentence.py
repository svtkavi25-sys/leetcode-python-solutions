import re
class Solution(object):
    def countValidWords(self, sentence):
        pattern = re.compile(r'^([a-z]+(-[a-z]+)?)?[!.,]?$')
        count = 0
        
        for token in sentence.split():
            if token == '-':
                continue
            if pattern.match(token):
                count += 1
                
        return count
