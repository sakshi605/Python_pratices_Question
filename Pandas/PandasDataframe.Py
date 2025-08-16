import pandas as pd
data ={
    'student':[" Sakshi ","priya"],
    'rank' : [1,4],
    'marks' : [90,95]
}
df = pd.DataFrame(data)
print ("student records \n \n",df)

df =pd.DataFrame (data, index =['rowA', 'rowB'])

print ("student records \n \n",df)

# acess the value in the student colum corresponding to rowA

print ("\n value = ", df.loc['rowA', 'student'])
print ("\n value = ", df.loc['rowB', 'student'])
print ("\n value = ", df.loc['rowA', 'marks'])