#Data generation

f = open("D:\Work\MWT\Data\VW_raw\created_data.txt","w+")
g = open("D:\Work\MWT\Data\VW_raw\Barget_data.txt","w+")
from random import randint
#context = np.empty(2000, dtype=np.str)
for i in range(0,2000):
    #context[i] = (str(randint(0,9))+","+str(randint(0,9)))
    f.write(str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+" "+
    str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+"\n")
    g.write(str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+" "+
    str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+" "+str(randint(0,9))+"\n")

f.close()
g.close()


#------------

import pandas
import numpy as np
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:shahidur_123@localhost:3306/mwt')

sql = "select context from stringRecord limit 10;"
dataX = pandas.read_sql_query(sql=sql,con=engine)

dataZ = dataX.values.tolist()

import ast
for i in range(0,10):
    #print(i[0])
    lst = ast.literal_eval(dataZ[i][0])
    print(lst[0])


sR_actionValue = "select actionID from stringRecord limit 10;"
dataY = pandas.read_sql_query(sql=sR_actionValue,con=engine)
dataY = dataY.values.tolist()
print(dataY[1])
import ast
for i in range(0,10):
    #print(i[0])
    lst = ast.literal_eval(dataY[i])
    print(lst[0])


#------------


import pandas
import numpy as np
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:shahidur_123@localhost:3306/mwt')

sql = "select context from stringRecord limit 10;"
dataX = pandas.read_sql_query(sql=sql,con=engine)
print(dataX)

dataZ = dataX.values.tolist()
for i in dataZ:
    print(np.asarray(i[0])[0])
print(dataX[2])

dataY = [0] * 10
dataY = [np.asarray(dataX) for dataX in dataX]


print(np.asarray(dataX[2])[0])
ty = np.asarray(dataX[2])[0]
print(np.asarray(ty))















