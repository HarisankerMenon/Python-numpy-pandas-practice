import pandas as pd

data={"id":101,"name":'vinay',"age":26,"prof":'bigdata',"salary":1000}

a=pd.Series(data)

print(a)



import pandas as pd

data1={"id":101,"name":'vinay',"age":26,"prof":'bigdata',"salary":1000}

a=pd.Series(data1,index=["age","prof","salary","id","name"])

print(a)

