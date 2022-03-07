def Palindrome(sentence):
    x, y= 0, len(sentence) - 1
   
    
    sentence = sentence.lower()
   
    
    while (x <= y):
   
       
        if (not(sentence[x] >= 'a' and sentence[x] <= 'z')):
            x += 1
   
        
        elif (not(sentence[y] >= 'a' and sentence[y] <= 'z')):
            y -= 1
   
        
        elif (sentence[x] == sentence[y]):
            x += 1
            y -= 1
         
       
        else:
            return False
    
    return True
   

s = input()
if (Palindrome(s)):
    print ("True")
else:
    print ("False")