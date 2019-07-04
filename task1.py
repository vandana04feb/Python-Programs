from sqlite3 import connect
import os
import platform

conn = connect('/home/vandana/Desktop/PythonDatabase/empp2.db')
curs = conn.cursor()



def manageOuthum():

	print("""******WELCOME TO OUTHUM MEDIA******
Enter 1 : To Create the Employees table
Enter 2 : To Insert the New Employees details
Enter 3 : To Select the Employees table
Enter 3 : To Drop the Employees table
Enter 4 : To Update the Employees details
Enter 5 : To Delete the Employees details
          """)

userInput = input("your database: ")

try: 
	userInput = int(userInput)
	print("This is valid queries: ", userInput)

	if(userInput == 1): 
		print("Create the database: ")
		curs.execute("CREATE TABLE IF NOT EXISTS employees(emp_id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT NOT NULL,last_name TEXT NOT NULL,age text NOT NULL,gender text NOT NULL,material text NOT NULL,phone_no numeric NOT NULL,address text NOT NULL)")

	elif(userInput == 2):
		def Empnew(self):
			Empnew = input("Insert the employees table: ")
			data = ['emp_id', 'first_name', 'last_name', 'age', 'gender', 'material', 'phone_no', 'address']
			curs.execute("INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?, ?, ?)".format(*data))
			return
			Empnew(" ") 

	elif(userInput == 3):
		def EmpSe(self):
			EmpSe = input("Select the employees table: ")
			curs.execute('SELECT * FROM employees')	
			return 
			EmpSe(" ")		

	elif(userInput == 4):
		def EmpDr(self):
			EmpDr = input("Drop the employees table: ")
			curs.execute('DROP TABLE employees')	
			return 
			EmpDr(" ")

	elif(userInput == 5):
		def EmpUp(self):
			Empup = input("Update the employees table: ")
			emp_id = '05'
			emp_id = '01'
			curs.execute( 'UPDATE employees SET emp_id = 05 WHERE emp_id = 01')
			curs.execute('SELECT * FROM employees;')
			return
			EmpUp(" ")

	elif(userInput == 6):
		def EmpDel(self):
			EmpDel = input("Delete the employees table: ")
			delete_emp_id = '05'
			curs.execute('DELETE FROM employees WHERE emp_id = 01')
			curs.execute('SELECT * FROM employees;')
			return
			EmpDel(" ")

	else:
		print("Please Enter Valid Option: ")

except ValueError:
	exit("\n That's Not A Number") 

finally:
	print("All details is complete")	

manageOuthum()

def runAgain(): 
	runAgn = input("\n Want To Run Again y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"):
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageOuthum()
		runAgain()


runAgain()		


for (name) in curs.fetchall():
    print (name)
    for row in cursor: 
    	print (row)

conn.close()


		    








