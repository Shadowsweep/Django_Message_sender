import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="2022",database="automessage",cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pno = input("Enter policy no. : ")
    q = "Select * from automessageapp_customers where policyno={0}".format(pno)
    smt.execute(q)
    row = smt.fetchone()
    if(row):
        print("Policy no.",row['policyno'])
        print("1] Customer name : ",row['Customername'])
        print("2] Contact number : ",row['contactno'])
        print("3] Last Date  : ",row['lastdate'])
        print("4] Time in Hours : ",row['hourtime'])
        print("5] Time in Minutes : ",row['mintime'])
    else:
        print("Record not found")
    conn.close()
except Exception as e:
    print("Error",e)