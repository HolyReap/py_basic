import psycopg2

def create_db(conn):
    cur.execute ("""
                 CREATE TABLE IF NOT EXISTS client(
                     client_id serial PRIMARY KEY,
                     first_name text,
                     last_name text,
                     email text
                 );
            """)
    cur.execute ("""
                 CREATE TABLE IF NOT EXISTS phones(
                     phone text PRIMARY KEY,
                     client_id INTEGER REFERENCES client(client_id)
                 );
            """)    
    conn.commit()
    

def add_client(conn, first_name, last_name, email, phones=None):
    if find_client_one(conn, first_name, last_name, email,) == 'client not found':
        cur.execute ("""
                 INSERT INTO client(first_name, last_name, email) VALUES(%s,%s,%s);
            """,(first_name, last_name, email))
        conn.commit()
        print(f'client id {find_client_one(conn, first_name, last_name, email,)} added\n') 
    else:
        print('client already exists')
        return 0
    if phones!=None:
        id = find_client_one(conn, first_name, last_name, email,)
        for item in phones:
            add_phone(conn, id, item)      

def id_check(conn, client_id):
    cur.execute("""
                select client_id from client 
                                 where client_id=%s;
            """, (client_id,))
    res = cur.fetchone()
    if res == None:
        return 'does not exist'
    return 'exists'

def add_phone(conn, client_id, phone):
    if id_check(conn, client_id) == 'does not exist':
        print('this client id does not exist')
        return 0
    if find_client_one(conn,'', '', '',phone) != client_id:         
        cur.execute ("""
                  INSERT INTO phones(phone, client_id) VALUES(%s,%s);
              """,(phone, client_id))   
        conn.commit()  

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    if id_check(conn, client_id) == 'does not exist':
        print('this client id does not exist')
        return 0
    if first_name!=None:
        cur.execute ("""
                 UPDATE client SET first_name=%s WHERE client_id=%s;
            """,(first_name, client_id))
        conn.commit()
    if last_name!=None:
        cur.execute ("""
                 UPDATE client SET last_name=%s WHERE client_id=%s;
            """,(last_name, client_id))
        conn.commit()    
    if email!=None:
        cur.execute ("""
                 UPDATE client SET email=%s WHERE client_id=%s;
            """,(email, client_id))
        conn.commit()
    if phones!=None:
        cur.execute ("""
                  DELETE FROM phones WHERE client_id=%s;
              """,(client_id,))   
        conn.commit() 
        for item in phones:
            add_phone(conn, client_id, item) 

def delete_phone(conn, client_id, phone):
    if id_check(conn, client_id) == 'does not exist':
        print('this client id does not exist')
        return 0
    if find_client_one(conn,'', '', '',phone) == client_id:         
        cur.execute ("""
                  DELETE FROM phones WHERE phone=%s and client_id=%s;
              """,(phone, client_id))   
        conn.commit() 

def delete_client(conn, client_id):
    if id_check(conn, client_id) == 'does not exist':
        print('this client id does not exist')
        return 0
    cur.execute ("""
                  DELETE FROM phones WHERE client_id=%s;
              """,(client_id,)) 
    conn.commit()
    cur.execute ("""
                  DELETE FROM client WHERE client_id=%s;
              """,(client_id,))  
    conn.commit()    

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    if first_name==None and last_name==None and email==None and phone==None:
        res = 'at least one condition required'
        return res
    cur.execute("""
                select c.*, p.phone from client c 
                                   left join phones p on c.client_id = p.client_id
                                   where first_name = coalesce(%s,first_name)
                                     and last_name = coalesce(%s,last_name)
                                     and email = coalesce(%s,email)
                                      or phone=%s;
            """, (first_name, last_name, email, phone))
    res = cur.fetchall()
    if res == []:
        return 'client not found'
    return res

def find_client_one(conn, first_name=None, last_name=None, email=None, phone=None):
    if first_name==None and last_name==None and email==None and phone==None:
        res = 'at least one condition required'
        return res
    cur.execute("""
                select c.client_id from client c 
                                   left join phones p on c.client_id = p.client_id
                                   where first_name=%s 
                                     and last_name=%s 
                                     and email=%s
                                      or phone=%s;
            """, (first_name, last_name, email, phone))
    res = cur.fetchone()
    if res == None:
        return 'client not found'
    return res[0]


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    cur = conn.cursor()
    create_db(conn)
    first_name='John'
    last_name='Smith'
    email='jsmith@gmail.com'
    phones = ('999-99-99','22-22-22')
    
    add_client(conn, first_name, last_name, email, phones)
    print(find_client(conn, None, None, email, None))
    print(find_client(conn, None, None, None, '22-22-22'))
    delete_phone(conn, 1, '999-99-99')
    add_phone(conn,1,'8-000-00-00')
    print(find_client(conn, None, None, email, None))
    change_client(conn,1,None,None,None,phones)
    delete_client(conn,1)
#    cur.execute("""
#                select c.*, p.phone from client c 
#                                   left join phones p on c.client_id = p.client_id
#            """)
#    print(cur.fetchall())
    cur.close()
conn.close()