# Data_frame

# Data frame used for 2-D array


# nested list

import pandas as pd
data=[[101,'vinay','k',26,'bigdata',1000],
      [102,'sanjay','n',29,'python',1000],
      [103,'amal','p',25,'python',1000],
      [104,'vimal','q',25,'python',1000],
      [105,'vishnu','s',27,'bigdata',1000]]


data1=pd.DataFrame(data,columns=["id","fname","lname","age","prof","salary"])
print(data1)


print(type(data1))
print(data1.shape)
print(data1.size)
print(data1.ndim)



