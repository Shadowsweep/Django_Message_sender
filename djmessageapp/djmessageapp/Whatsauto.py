import pywhatkit
import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="2022",database="automessage",cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pno = input("Enter Policy no. : ")
    q = "Select * from automessageapp_customers where policyno={0}".format(pno)
    smt.execute(q)
    row = smt.fetchone()
    if(row):
        # n = int(input("Enter No. of customers : "))
        print("Policy no.",row['policyno'])
        print("1] Customer name : ",row['customername'])
        print("2] Contact number : ",row['contactno'])
        print("3] Last Date  : ",row['lastdate'])
        print("4] Time in Hours : ",row['hourtime'])
        print("5] Time in Minutes : ",row['mintime'])
        n=1
        while(1<=n):
            mn= row['contactno']
            one = len(str(mn))
            if one == 10:
                pno = row["policyno"]
                two = len(str(pno))
                if two == 9:
                    cn = row['customername']
                    ld = row['lastdate']
                    th = int(row['hourtime'])
                    tm = int(row['mintime'])
                    pywhatkit.sendwhatmsg("+91{0}".format(mn)," Dear {0} Please pay  Policy No.{1} on or before {2}. You can pay online at https://ebiz.licindia.in/D2CPM/#Login. Please Ignore, if paid".format(cn,pno,ld),th,tm)
                else:
                    print("Invalid Policy number")
                    break
            else:
                print("Invalid Mobile Number")
                break

            # n = n + 1
    else:
        print("Record not found")
    conn.close()
except Exception as e:
    print("Error",e)