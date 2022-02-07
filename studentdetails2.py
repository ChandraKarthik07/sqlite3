import cgi,cgitb
form=cgi.FieldStorage()
import sqlite3
conn=sqlite3.connect('details.db')
si=form.getvalue('stu_id')
sn=form.getvalue('stu_name')
sa=form.getvalue('stu_address')
sc=form.getvalue('stu_course')
sf=form.getvalue('stu_fee')
print ('Content-type:text/html\r\n\r\n')
print ('<html>')
print ('<body>')
print ('<title> Student Details Added with id</title>')

if form.getvalue('insert_button'):
    conn=sqlite3.connect('details.db')
    conn.execute("INSERT INTO STUDENT(ID,NAME,ADDRESS,COURSE,FEE)VALUES(?,?,?,?,?)",(si,sn,sa,sc,sf))
    conn.commit()
    if(si):
        conn=sqlite3.connect('details.db')
        si=form.getvalue('stu_id')
        conn.commit()
    else:
        si="You are not  inserted any value"
        
    print('<h2> Student Details Added with ID: %s</h2>')%si
    
           
elif form.getvalue('delete_button'):
    conn=sqlite3.connect('details.db')
    conn.execute("DELETE FROM STUDENT WHERE ID=?",(si,))
    conn.commit()
    print ('<h2> Deleted Student ID is: %s</h2>')%si
    
elif form.getvalue('select_button'):
    cursor=conn.execute("SELECT*FROM STUDENT WHERE ID=?",(si,))
    conn.commit()
    if(si):
        conn=sqlite3.connect('details.db')
        si=form.getvalue('stu_id')
        conn.commit()
    else:
        si="ID not Exixts"
       
    for col in cursor:
            print "Studnet ID=",col[0],
            print "Student Name=",col[1]
            print "Address=",col[2]
            print "Course=",col[3]
            print "Fee=",col[4]
            
elif form.getvalue('update_button'):
    conn=sqlite3.connect('details.db')
    cursor=conn.execute("UPDATE STUDENT SET NAME=? WHERE ID=?",(sn,si))
    conn.commit()
        
    print('<h2> Updated Name for Studnet ID: %s is %s</h2>')%(si,sn)

         
    
elif form.getvalue('display_button'):
    conn=sqlite3.connect('details.db')
    cursor=conn.execute("SELECT*FROM STUDENT")
    for col in cursor:
        print "Studnet ID=",col[0]
        print "Student Name=",col[1]
        print "Address=",col[2]
        print "Course=",col[3]
        print "Fee=",col[4]
    
                   

        
       
print ('</body>')
print ('</html>')
