import sqlite3

def connect():
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Create Table If not exists data1 (id  INTEGER PRIMARY KEY,fn TEXT,ln TEXT,term INTEGER,gpa REAL )")

    con.commit()
    con.close()

def insert(fn,ln,term,gpa):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Insert Into data1 Values(NULL,?,?,?,?)",(fn,ln,term,gpa))

    con.commit()
    con.close()

def view():
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Select * From data1")
    rows=cur.fetchall()
    
    con.close()
    return(rows)

def view_all():
    out=view()
    print(out)
    

def Search_fn(fn=""):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Select * From data1 where fn=? ",(fn,))
    rows=cur.fetchall()
    
    con.close()
    print(rows)

def Search_ln(ln=""):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Select * From data1 where ln=? ",(ln,))
    rows=cur.fetchall()
    
    con.close()
    print(rows)

def Search_term(term=""):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Select * From data1 where term=? ",(term,))
    rows=cur.fetchall()
    
    con.close()
    print(rows)
    
def Search_gpa(gpa=""):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Select * From data1 where gpa=? ",(gpa,))
    rows=cur.fetchall()

    con.close()
    print(rows)

def update_fn(id,fn):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Update data1 Set fn=? Where id=?",(fn,id))

    con.commit()
    con.close()

def update_ln(id,ln):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Update data1 Set ln=? Where id =?",(ln,id))

    con.commit()
    con.close()

def update_term(id,term):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Update data1 Set term=?",(term,id))

    con.commit()
    con.close()

def update_gpa(id,gpa):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Update data1 Set gpa=? Where id=?",(gpa,id))

    con.commit()
    con.close()

def delete(id):
    con=sqlite3.connect("students.db")
    cur=con.cursor()

    cur.execute("Delete from data1 Where id=?",(id,))

    con.commit()
    con.close()
    


