import pyinputplus as pyip

def Merge(dict1, dict2): 
   for key, value in dict2.items():
      if key in dict1:
         dict1[key] = [value , dict1[key]]
      else:
         dict1[key]=value
   return(dict1)   

n1= pyip.inputInt(prompt='Enter The no of inputs In Dictionary 1:',min=0)
d1 = {}
for i in range(n1):
    keys = pyip.inputNum("Enter the Key:")
    values = pyip.inputStr("Enter the Value:")
    d1[keys] = values
print(d1)

n2= pyip.inputInt(prompt='Enter The no of inputs In Dictionary 2:',min=0)
d2 = {}
for i in range(n2):
    keys = pyip.inputNum("Enter the Key :")
    values = pyip.inputStr("Enter the Value:")
    d2[keys] = values
print(d2)

d3 = (Merge(d1, d2)) 
print("\nDictionary after merging ::>",d3)