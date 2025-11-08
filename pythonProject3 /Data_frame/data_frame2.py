import pandas as pd

data={'name':['nithin','noel','hains','manu','jack'],'qual':['msc','bsc','mba','mcom','bca'],'job':['busines','data analyst','manger','tutor','piolt'],'salary':
      [500000,250000,145521,172358,1452651]}

df=pd.DataFrame(data)
print(df)

print(df.columns)



import pandas as pd
data=[[101,'vinay','k',26,'bigdata',1000],
      [102,'sanjay','n',29,'python',1000],
      [103,'amal','p',25,'python',1000],
      [104,'vimal','q',25,'python',1000],
      [105,'vishnu','s',27,'bigdata',1000]]


data1=pd.DataFrame(data)
print(data1)


print(type(data1))
print(data1.shape)
print(data1.size)
print(data1.ndim)

print(data1.columns)

# Describe


import pandas as pd
data=[[101,'vinay','k',26,'bigdata',1000],
      [102,'sanjay','n',29,'python',1000],
      [103,'amal','p',25,'python',1000],
      [104,'vimal','q',25,'python',1000],
      [105,'vishnu','s',27,'bigdata',1000]]


data1=pd.DataFrame(data,columns=["id","fname","lname","age","prof","salary"])
print(data1)

print(data1.describe())

print(data1.describe(include='O'))

print(data1.describe(include='all'))

