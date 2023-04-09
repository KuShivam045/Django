from django.db import connection, transaction, connections
import sys
import os
import re


def dictfetchall(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def insert_q(data):
    # print(data)
    with connection.cursor() as cursor:
        resp = cursor.execute("""INSERT INTO movies.movie(Title, genre, cast, director, release_year) 
        VALUES(%s,%s,%s,%s,%s);""",data)
        # print("jnlshbfhba")
    return cursor.lastrowid

def insert_r(data):
    with connection.cursor() as cursor:
        resp = cursor.execute(""" INSERT INTO movies.employee(EmployeeID, FirstName, LastName, EmployeeProfile, DateofJoining, CompanyAddress, City)
         VALUES (%s,%s,%s,%s,%s,%s,%s);""",data)
        
    return resp


def readData(find_):
    with connection.cursor() as cursor:
        # print(364989846549841)
        resp = cursor.execute(f"select * from movies.employee where ID = '{find_}';")
        # print(resp)
        if resp and cursor.rowcount:
            resp =dictfetchone(cursor)
            # print(resp)
        else:
            resp = None
    return resp     

        
def updateData(find_):

    print("1546468684698484")
    with connection.cursor() as cursor:
        resp = cursor.execute("""update movies.employee set EmployeeID = %s, FirstName = %s,
        LastName = %s, EmployeeProfile = %s, DateofJoining = %s, CompanyAddress = %s, City = %s 
        WHERE ID = %s;""",find_)

        print(resp)
    return resp
        
