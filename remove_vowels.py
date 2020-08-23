#Amazon interview Question
#Given a User Input , Print the number of words in the input before and after removing vowels in it.

#Sample example 
#Sample Input: "Here is a example"
#Sample Output : "hr s xmpl"
#Before removing:4 ,after removing:3

def RemoveVowelsAndCountWords(s):
    vowels=['a','e','i','o','u']
    s=s.lower()
    for i in s:
        for j in i:
            if j in vowels:
                s=s.replace(j,"")
    
    return len(s.split())

s=raw_input("Enter String")
before=len(s.split())
after=RemoveVowelsAndCountWords(s)
print "before removing:",before,"after removing:",after
