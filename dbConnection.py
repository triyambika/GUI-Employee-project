import mysql.connector as m1
import time
def returnConnection():
        mycon = m1.connect(host="root",user="root",password='triyambika123',database='company')
        return mycon


	
