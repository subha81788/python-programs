str1 = "Good";  
str2 = "morning";  
   
print("Strings before swapping:{0} {1}\n".format(str1,str2));  
   
str1 = str1 + str2;  
str2 = str1[0 : (len(str1) - len(str2))];  
str1 = str1[len(str2):];  
   
print("Strings after swapping:{0} {1}".format(str1,str2));  
