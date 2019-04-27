import mysql.connector
import pandas as pd
from pword import gen_pword

mydb = mysql.connector.connect(
    host="localhost", user="root", password=gen_pword(), database="marriage")

mycursor = mydb.cursor()

flag = True


def insert():
	name = input("Enter guest name: ")
	count = int(input("Enter the count of guests: "))
	mar = input("Is guest invited to marriage?(Y/N): ")
	rec = input("Is guest invited to reception?(Y/N): ")
	mar = mar.upper()
	rec = rec.upper()
	comb = (name, count, mar, rec)
	query = "INSERT INTO marriage_list (Name, Count, Marriage, Reception) VALUES (%s, %s, %s, %s)"
	mycursor.execute(query, comb)
	mydb.commit()


def delete():
	name = input("Enter the name of guest you want to remove: ")
	comb = (name,)
	query = "Delete from marriage_list where Name = (%s)"
	mycursor.execute(query, comb)
	mydb.commit()


def show():
	# query=("SELECT Name, Count FROM marriage_list")
	# mycursor.execute(query)
	# myresult= mycursor.fetchall()
	# for row in myresult:
	#	print(row);
    table = pd.read_sql('SELECT * FROM marriage_list order by Name', con=mydb)
    print(table)
    
def specific_query():
    name= input("Enter the character. Results will display records starting from that character: ")
    name= name + '%'
    comb=(name,)
    table_1= pd.read_sql('Select * FROM marriage_list where Name like (%s)' , con=mydb, params=comb)
    print(table_1)

'''
def specific_query():
	name = input("Enter the character. Results will display records starting from that character: ")
	name = name + '%'
   comb=(name,) 
   table_1 = pd.read_sql('SELECT * FROM marriage_list where Name like (%s)' , con=mydb, params=comb)
   print(table_1)
	# query="Select Name, Count from marriage_list where Name like (%s) "
	# comb=(name,)
	# mycursor.execute(query, comb)
	# myresult= mycursor.fetchall()
	# for row in myresult:
	#	print(row)
'''
def update():
	query="Update marriage_list set count=(%s) where name=(%s)"
	name=input("Enter guest name you want to update count of: ")
	count=int(input("Enter new guest count: "))
	comb=(count, name)
	mycursor.execute(query, comb)
	mydb.commit()

def orderby_name():
    table_2=pd.read_sql('Select Name, Count from marriage_list order by Name', con=mydb)
    print(table_2)
    #query="Select Name, Count from marriage_list order by Name"
    #mycursor.execute(query)
    #myresult= mycursor.fetchall()
    #for row in myresult:
     #   print(row)

def orderby_count():
    order=input("Enter Order Ascending or Descending-(A/D): ")
    order=order.upper()
    if order=='A':
        table_3=pd.read_sql('Select Name, Count from marriage_list order by Count', con=mydb)
        print(table_3)
    	#query="Select Name, Count from marriage_list order by Count"
    	#mycursor.execute(query)
    	#myresult= mycursor.fetchall()
    	#for row in myresult:
    	#	print(row)

    else:
        table_3=pd.read_sql('Select Name, Count from marriage_list order by Count DESC', con=mydb)
        print(table_3)
    	#query="Select Name, Count from marriage_list order by Count DESC"
    	#mycursor.execute(query)
    	#myresult= mycursor.fetchall()
    	#for row in myresult:
    	#	print(row)

def orderby_marriageonly():
    
    #query1="Select Name, Count from marriage_list where Marriage='Y' and Reception='N'"
    table_4=pd.read_sql("Select Name, Count from marriage_list where Marriage='Y' and Reception='N'", con=mydb)
    print(table_4)
    query2="Select count(*) from marriage_list where Marriage='Y' and Reception='N'"
    query3="Select SUM(Count) from marriage_list where Marriage='Y' and Reception='N'"
    #mycursor.execute(query1)
    #myresult1=mycursor.fetchall()
    #for row in myresult1:
    #	print(row)
    mycursor.execute(query2)
    myresult2=mycursor.fetchone()
    for row in myresult2:
    	print("Total no of families at marriage: ",row)
    mycursor.execute(query3)
    myresult3=mycursor.fetchone()
    for row in myresult3:
    	print("Total no of guests at wedding: ",row)

def orderby_marriage():
    #query1="Select Name, Count from marriage_list where Marriage='Y'"
    table_5=pd.read_sql("Select Name, Count from marriage_list where Marriage='Y'", con=mydb)
    print(table_5)
    query2="Select count(*) from marriage_list where Marriage='Y'"
    query3="Select SUM(Count) from marriage_list where Marriage='Y'"
    #mycursor.execute(query1)
    #myresult1=mycursor.fetchall()
    #for row in myresult1:
    #	print(row)
    mycursor.execute(query2)
    myresult2=mycursor.fetchone()
    for row in myresult2:
    	print("Total no of families at marriage: ",row)
    mycursor.execute(query3)
    myresult3=mycursor.fetchone()
    for row in myresult3:
    	print("Total no of guests at wedding: ",row)

def orderby_receptiononly():
    #query1="Select Name, Count from marriage_list where Reception='Y' and Marriage='N'"
    table_6= pd.read_sql("Select Name, Count from marriage_list where Reception='Y' and Marriage='N'", con=mydb)
    print(table_6)
    query2="Select count(*) from marriage_list where Reception='Y' and Marriage='N'"
    query3="Select SUM(Count) from marriage_list where Reception='Y' and Marriage='N'"
    #mycursor.execute(query1)
    #myresult1=mycursor.fetchall()
    #for row in myresult1:
    #	print(row)
    mycursor.execute(query2)
    myresult2=mycursor.fetchone()
    for row in myresult2:
    	print("Total no of families at reception: ",row)
    mycursor.execute(query3)
    myresult3=mycursor.fetchone()
    for row in myresult3:
    	print("Total no of guests at reception: ",row)

def orderby_reception():
    #query1="Select Name, Count from marriage_list where Reception='Y'"
    table_7= pd.read_sql("Select Name, Count from marriage_list where Reception='Y'", con=mydb)
    print(table_7)
    query2="Select count(*) from marriage_list where Reception='Y'"
    query3="Select SUM(Count) from marriage_list where Reception='Y'"
    #mycursor.execute(query1)
    #myresult1=mycursor.fetchall()
    #for row in myresult1:
    #	print(row)
    mycursor.execute(query2)
    myresult2=mycursor.fetchone()
    for row in myresult2:
    	print("Total no of families at reception: ",row)
    mycursor.execute(query3)
    myresult3=mycursor.fetchone()
    for row in myresult3:
    	print("Total no of guests at reception: ",row)

def orderby_common():
    #query1="select Name, Count from marriage_list where Marriage='Y' AND Reception='Y'"
    table_8= pd.read_sql("select Name, Count from marriage_list where Marriage='Y' AND Reception='Y'", con=mydb)
    print(table_8)
    query2="select count(*) from marriage_list where Marriage='Y' AND Reception='Y'"
    query3="select SUM(Count) from marriage_list where Marriage='Y' AND Reception='Y'"
    #mycursor.execute(query1)
    #myresult1=mycursor.fetchall()
    #for row in myresult1:
    #	print(row)
    mycursor.execute(query2)
    myresult2=mycursor.fetchone()
    for row in myresult2:
    	print("Total no of families at marriage and reception both: ",row)
    mycursor.execute(query3)
    myresult3=mycursor.fetchone()
    for row in myresult3:
    	print("Total no of guests at marriage and reception both: ",row)



def total_guests():
	query="Select SUM(Count) from marriage_list"
	mycursor.execute(query)
	myresult=mycursor.fetchone()
	for row in myresult:
		print("Total guests are: ",row)

while flag:
	print("a. Insert Guest")
	print("b. Remove Guest")
	print("c. Update a guest")
	print("d. Show all guests")
	print("e. Show guests starting by a letter")
	print("f. Show guests by name")
	print("g. Show guests by count")
	print("h. Show guests at marriage")
	print("i. Show guests only at marriage and not reception")
	print("j. Show guests at reception")
	print("k. Show guests only at reception and not marriage")
	print("l. Show guests both at marriage and reception")
	print("m. Show total count of guests")
	inp=input("Enter the function you want to perform(a,b,c,d,e,f,g,h,i,j,k):")
	inp=inp.upper()
	if inp=='A':
		insert()

	elif inp=='B':
		delete()

	elif inp=='C':
		update()

	elif inp=='D':
		show()

	elif inp=='E':
		specific_query()

	elif inp=='F':
		orderby_name()

	elif inp=='G':
		orderby_count()

	elif inp=='H':
		orderby_marriage()

	elif inp=='I':
		orderby_marriageonly()

	elif inp=='J':
		orderby_reception()

	elif inp=='K':
		orderby_receptiononly()

	elif inp=='L':
		orderby_common()

	else:
    
		total_guests()

	cont=input("Do you want to continue doing operations? (y/n): ")
	cont=cont.upper()
	print('\n'*40)
	if cont=='Y':
		flag=True
	else:
		flag=False

# table = pd.read_sql('SELECT * FROM marriage_list', con=mydb)
# print(table)
