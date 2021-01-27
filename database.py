import mysql.connector

data = mysql.connector.connect(host="localhost", user="root", passwd='nemo@1', database="mydata")

mycursor = data.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()
print(result)

