import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate

def option1():
    try:
        print("Enter name of legislaive body member: ")
        name = input()
        query = "SELECT Member_name, street, city, State_name, lbm_address.zipcode  FROM legislative_body_members, lbm_address WHERE legislative_body_members.zip_code = lbm_address.zipcode AND legislative_body_members.Member_name=('%s')" % (name)
        with con.cursor() as cur:
            cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, headers="keys", tablefmt='psql'))
        for x in cur:
            print(x)

        
    except Exception as e:
        con.rollback()
        print("Failed to query database")
        print(">>>>>>>>>>>>>", e)



def option2():
    print("Enter budget : ")
    budget = int(input())
    query = "select * from department where Budget > ('%d')" % (budget)
    try:
        
        with con.cursor() as cur:
            cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, headers="keys", tablefmt='psql'))
        for x in cur:
            print(x)
    except Exception as e:
        con.rollback()
        print("Failed to show")
        print(">>>>>>>>>>>>>", e)

    return


def option3():
    try:
        print("Enter Party ID : ")
        name = input()
        query = "select ((100.0*(select count(Member_Name) from legislative_body_members where P_ID=('%s'))) / (1.0*(SELECT count(Member_Name) from legislative_body_members)));" % (name)
        #print(query)
        with con.cursor() as cur:
            cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, tablefmt='psql'))
        for x in cur:
           print(x)

        
    except Exception as e:
        con.rollback()
        print("Failed to query database")
        print(">>>>>>>>>>>>>", e)

def option4():
    
    try:
        print("Enter turnout %: ")
        turnout = int(input())
        query = "SELECT *  FROM election WHERE voter_turnout > ('%d')" % (turnout)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, headers="keys", tablefmt='psql'))
        for x in cur:
            print(x)
        
    except Exception as e:
        con.rollback()
        print("Failed to query database")
        print(">>>>>>>>>>>>>", e)


def option5():
    print("Enter Start Year : ")
    year = int(input())
    query = "select * from lok_sabha where Start_Year = ('%d')" % (year)
    try:
        
        with con.cursor() as cur:
            cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, headers="keys", tablefmt='psql'))
        for x in cur:
            print(x)
    except Exception as e:
        con.rollback()
        print("Failed to query into database")
        print(">>>>>>>>>>>>>", e)

    return


def option6():
    try:
        print("Enter name of legislative body member: ")
        name = input()
        print("Enter new phone number: ")
        phone = input()
        query = "UPDATE lbm_phone_numbers SET phone_number = ('%s') WHERE member_name=('%s')" % (phone, name)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, headers="keys", tablefmt='psql'))
        for x in cur:
            print(x)
        
    except Exception as e:
        con.rollback()
        print("Failed to query database")
        print(">>>>>>>>>>>>>", e)

    
def option7():
    print("Enter Department name : ")
    depart = input()
    print("Enter new budget: ")
    new_budget = int(input())
    query = "UPDATE department SET Budget = ('%d') WHERE Dept_Name = ('%s'); " % (new_budget, depart)

    try:
        
        with con.cursor() as cur:
            cur.execute(query)
        print("updated Database")
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def option8():
    try:
        print("Enter name of Chief Minister: ")
        name = input()
        print("Enter new term: ")
        nterm = int(input())
        query = "UPDATE State_name SET finish_year=('%d') where chief_minister=('%s')" % (nterm, name)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        print()
        print(tabulate(table, headers="keys", tablefmt='psql'))
        for x in cur:
            print(x)
        
    except Exception as e:
        con.rollback()
        print("Failed to query database")
        print(">>>>>>>>>>>>>", e)
    

def dispatch(ch):
    if(ch == 1):
        option1()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option5()
    elif(ch == 6):
        option6()
    elif(ch == 7):
        option7()
    elif(ch == 8):
        option8()
    else:
        print("Error: Invalid Option")

while(1):
    tmp = sp.call('clear', shell=True)

    # change following details based on your sql credentials
    HOST="localhost"
    USER="root"
    PASS="password"
    DATABASE='project'
    try:
        con = pymysql.connect(host=HOST,
                              user=USER,
                              password=PASS,
                              db=DATABASE,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
            exit()

        

        with con.cursor() as cur:
            while(1):
                
                print("1. Get the address of a member of a legislative body")
                print("2. Get all the departments with budget more than some amount")
                print("3. Display percentage of Legislative body members belonging to some party")
                print("4. Get information about elections with voter turnout greater than some %")
                print("5. Get list of Lok Sabha members who started term at a year")
                print("6. Update the phone number of a legislative body member")
                print("7. Update the budget of some department")
                print("8. Update the term of some Chief Minister")
                print("9. Exit")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        exit()
