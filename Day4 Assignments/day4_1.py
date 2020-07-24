str = "What we think we become, we are python programmer"
result1 = str.count("we")
print(f"The Occurence of the substring 'we' is : {result1} ")
result2 = str.find("we",0,10)
print(f"The index value of first occurence : {result2}")
result3 = str.find("we",6,17)
print(f"The index value of second occurence : {result3}")
result4 = str.find("we",15,40)
print(f"The index value of third occurence : {result4}")

