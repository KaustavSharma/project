import os 
import platform
import mysql.connector
import pandas as pd 
mydb=mysql.connector.connect(host='localhost',user='root',password='kaustav',database='service')

def create_table():
    try:
        mycursor=mydb.cursor()
        mycursor.execute('create database service') 
        mycursor=mydb.cursor()
        mycursor.execute("create table ims(msg_id VARCHAR(10),rname VARCHAR(30),sname VARCHAR(30),rmail VARCHAR(50),smail VARCHAR(50),msg VARCHAR(250))")
        print('table created')
    except:
        print('database or table already created')

def add_msg():
    mycursor=mydb.cursor()
    msg_id=input('enter message id:')
    rname=input('enter name of receiver:')
    sname=input('enter name of sender:')
    rmail=input('enter receivers mailid:')
    smail=input('enter senders mailid:')
    msg=input('enter message:')

    sql='insert into ims(msg_id,rname,sname,rmail,smail,msg) values(%s,%s,%s,%s,%s,%s)'
    val==(msg_id,rname,sname,rmail,smail,msg)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,' record inserted.')

def search_msg():
    mycursor=mydb.cursor()
    print('select the search criteria')
    print('1 message id:')
    print('2 name of the sender:')
    print('3 name of the receiver:')
    print('4 all details')
    ch=int(input('enter your choice:'))

    if ch==1:
        s=input('enter message id:')
        mycursor.exceute('select * from ims')
        myresult=mycursor.fetchall()
        for x in myresult:
            if x[0]==s:
                print(x)
        if myresult:
            print('no record found for id: ',s)

    elif ch==2:
        sn==input('enter sender name')
        mycursor.execute('select * from ims')
        myresult=mycursor.fetchall()
        for x in myresult:
            if x[2]==s:
                print(s)
        if myresult:
            print('no record found for sender name: ',s)
    
    elif ch==3:
        s=input('enter receiver name')
        mycursor.execute("select * from ims")
        myresult=mycursor.fetchall()
        for x in myresult:
            if x[1]==s:
                print(x)
        if myresult:
            print('no record found')

    elif ch==4:
        mycursor.execute('select * from ims')
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        if myresult:
            print('no record found')

def delete_msg():
    mycursor=mydb.cursor()
    ms=input('enter the message id to be deleted:')
    sql='delete from ims where msg_id=%s'%ms
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,'record(s) deleted')

def main_menu():
    print('enter 1: to add new message')
    print('enter 2: to search message')
    print('enter 3: to delete message')
    print('enter others to exit')

    try:
        userinput=int(input("please enter your choice"))

        if userinput==1:
            print('\n')
            add_msg()

        elif userinput==2:
            search_msg()
        
        elif userinput==3:
            delete_msg()
        
        else:
            print('enter correct choice')
            ch=input('\n want to continue (y/n):')
            if ch.lower()=='y':
                print(os.system('cls'))
                main_menu()
            else:
                print('program going to exit')
                exit('\n thanks')

    except():
        print('something wrong in code')
#main_menu()
create_table()
