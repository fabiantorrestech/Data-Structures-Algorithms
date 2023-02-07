# order matters so this solution doesn't work?
# k = k-most-frequent words that appear in 'words' array

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # count number of usages in words
        seenWords = dict()
        for currStr in words:
            seenWords[currStr] = 1 + seenWords.get(currStr, 0)
        
        # organize a 2nd dictionary: <k,v> = <numAppearancesInWords, [key1, key2, key3...]>
        occurencesThenWord = dict()
        for key in seenWords:
            numOfOccurences = seenWords[key]
            if occurencesThenWord.get(numOfOccurences) == None: 
                occurencesThenWord[numOfOccurences] = [key]
            else:
                occurencesThenWord[numOfOccurences].append(key)
        
        print(occurencesThenWord)
        
        # now only get the first k words
        highestKey = max(occurencesThenWord)
        answer = []
        idx, kCounter = highestKey, 0
        while kCounter < k and idx > 0:
            if occurencesThenWord.get(idx):
                i=len(occurencesThenWord.get(idx))-1
                while kCounter < k and i>=0:
                    answer.append(occurencesThenWord.get(idx)[i])
                    print(occurencesThenWord.get(idx)[i])
                    i-=1
                    kCounter+=1
            idx-=1
        
        return answer
            
        