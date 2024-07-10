import psycopg
import json

from constant import  POSTGRES_PASSWORD, POSTGRES_USER, POSTGRES_DB

from psycopg.rows import dict_row

class Postgres() :
    def __init__(self) -> None:
        self.connect =  psycopg.connect(
            'postgres://{}:{}@localhost:5432/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB),
            row_factory = dict_row,
            autocommit=True
        )
        self.cursor = self.connect.cursor()
        
        
    def init_db(self):
        with open('schema.sql') as f:
            self.cursor.execute(f.read())
            self.connect.commit()
    def migrate(self):
        with open('migrations.sql') as f:
            self.cursor.execute(f.read())
            self.connect.commit()
    
    def create_user(self, email, password, **kwargs ):
        try :
            query = """INSERT INTO users(email, password, first_name, last_name, is_superuser, is_staff)
                       VALUES (%s, %s, %s, %s, %s, %s)
                    """
            values  = (email, password, kwargs.get("first_name"), kwargs.get("last_name"), kwargs.get("is_superuser", False), kwargs.get("is_staff", False))
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "Utilisateur cree avec success"
        except psycopg.errors.UniqueViolation as e :
            return False, "Un utilisateur avec cet email existe deja"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction create_user de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer"
        
    def confirm_email(self, email):
        try :
            query = """UPDATE users SET emailVerified = true WHERE email = %s"""
            self.cursor.execute(query, (email,))
            self.connect.commit()
            return True
        except Exception as e :
            print("Une erreur s'est produite dans la fonction confirm_email de la classe postgres ==> \n", e)
            return False
    
    def get_data_table(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Une erreur s'est produite dans la fonction get_data_table de la classe postgres ==> \n", e)
            return False

    def get_user_by_id(self, uid):
        try :
            query = """SELECT * FROM users WHERE uid = %s"""
            self.cursor.execute(query, (uid,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_user_by_id de la classe postgres ==> \n", e)
            return False
    
    def get_user_by_email_and_password(self, email,password):
        try :
            query = """SELECT * FROM users WHERE email = %s AND password = %s"""
            self.cursor.execute(query, (email, password))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_user_by_email_and_password de la classe postgres ==> \n", e)
            return None
    
    def get_user_by_email(self, email):
        try :
            query = """SELECT * FROM users WHERE email = %s"""
            self.cursor.execute(query, (email,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_user_by_email de la classe postgres ==> \n", e)
            return False 

        
    def create_prompt(self, title, text, created_by, **kwargs ):
        try :
            query = """INSERT INTO prompts(title ,text,created_by, tags)
                       VALUES (%s, %s, %s, %s)
                    """
            values  = (title, text, created_by, kwargs.get("tags"))
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "prompt cree avec success"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction create_prompt de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer" 
        
    def get_prompt_by_id(self, prompt_id):
        try :
            query = """SELECT * FROM prompts WHERE prompt_id = %s"""
            self.cursor.execute(query, (prompt_id,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_prompt_by_id de la classe postgres ==> \n", e)
            return False
    
    def create_group(self, name, created_by):
        try :
            query ="""INSERT INTO groups(name, created_by) VALUES (%s, %s)"""
            values = (name, created_by)
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "Group cree avec success"
        except psycopg.errors.UniqueViolation as e :
            return False, "Un groupe avec ce nom existe deja"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction create_group de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer"
        
    def get_group_by_id(self, group_id):
        try :
            query = """SELECT * FROM groups WHERE group_id = %s"""
            self.cursor.execute(query, (group_id,))
            return self.cursor.fetchall()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_group_by_id de la class postgres ==> \n", e)
        
    def get_group_member_by_uid(self, uid): 
        try : 
            query = """SELECT * FROM group_members WHERE uid = %s"""
            self.cursor.execute(query, (uid,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_group_member_by_uid de la classe postgres ==> \n", e)
            return False
    
    def get_group_member_by_gid(self, group_id):
        try :
            query = """SELECT * FROM group_members WHERE group_id = %s"""
            self.cursor.execute(query, (group_id,))
            return self.cursor.fetchall()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_group_member_by_gid de la classe postgres ==> \n", e)
            return False
    
    def add_member (self, uid, group_id):
        try :
            query = """INSERT INTO group_members(uid, group_id) VALUES (%s, %s)"""
            values = (uid, group_id)
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "Membre ajoute avec success"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction add_member de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer"
        
        
    def add_vote(self, uid, prompt_id, value=1):
        try :
            query = """INSERT INTO votes(uid, prompt_id, value) VALUES (%s, %s, %s)"""
            values = (uid, prompt_id, value)
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "Vote ajoute avec success"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction add_vote de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer"
    
    def add_note(self, uid, prompt_id, value):
        try :
            print(uid, prompt_id, value)
            query = """INSERT INTO notes(uid, prompt_id, value) VALUES (%s, %s, %s)"""
            values = (uid, prompt_id, value)
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "Note ajoute avec success"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction add_vote de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer"
    
    def get_vote_by_uid_and_pid(self, uid, prompt_id):
        try :
            query = """SELECT * FROM votes WHERE uid = %s AND prompt_id = %s"""
            self.cursor.execute(query, (uid, prompt_id))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_vote_by_uid_and_pid de la classe postgres ==> \n", e)
            return False
        
    def get_notes_by_uid_and_pid(self, uid, prompt_id):
        try :
            query = """SELECT * FROM notes WHERE uid = %s AND prompt_id = %s"""
            self.cursor.execute(query, (uid, prompt_id))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_vote_by_uid_and_pid de la classe postgres ==> \n", e)
            return False
        
    def get_sum_votes_by_pid(self, prompt_id):
        try :
            query = """SELECT SUM(value) FROM votes WHERE prompt_id = %s"""
            self.cursor.execute(query, (prompt_id,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_sum_votes_by_pid de la classe postgres ==> \n", e)
            return False
    
    def get_avg_notes_by_pid(self, prompt_id):
        try :
            print("prompt id, ", prompt_id)
            query = """SELECT AVG(value) FROM notes WHERE prompt_id = %s"""
            self.cursor.execute(query, (prompt_id,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_sum_votes_by_pid de la classe postgres ==> \n", e)
            return False
            
    
    def get_votes_by_pid(self, prompt_id):
        try :
            query = """SELECT * FROM votes WHERE prompt_id = %s"""
            self.cursor.execute(query, (prompt_id,))
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_votes_by_pid de la classe postgres ==> \n", e)
            return False
        
    def update_prompt_state(self, prompt_id, state):
        try :
            query = """UPDATE prompts SET state = %s WHERE prompt_id = %s"""
            values = (state, prompt_id)
            self.cursor.execute(query, values)
            self.connect.commit()
            return True
        except Exception as e :
            print("Une erreur s'est produite dans la fonction update_prompt_state de la classe postgres ==> \n", e)
            return False
     
    def update_prompt_price(self, prompt_id, price):
        try :
            query = """UPDATE prompts SET price = %s WHERE prompt_id = %s"""
            values = (price, prompt_id)
            self.cursor.execute(query, values)
            self.connect.commit()
            return True
        except Exception as e :
            print("Une erreur s'est produite dans la fonction update_prompt_state de la classe postgres ==> \n", e)
            return False
        
    def add_transaction(self, buyer_info : dict, prompt_id: int, amount: int) -> bool:
        try :
            buyer_info_json = json.dumps(buyer_info, indent=1)
            print(buyer_info_json)
            query = """INSERT INTO transactions(buyer_info, prompt_id, amount) VALUES (%s, %s, %s)"""
            values = ([buyer_info_json, prompt_id, amount])
            self.cursor.execute(query, values)
            return True
        except Exception as e :
            print("Une erreur s'est produite dans la fonction add_transaction de la classe postgres ==> \n", e)
            return False
    
    def get_table_count(self, table_name):
        try :
            query = f"""SELECT COUNT(*) FROM {table_name}"""
            self.cursor.execute(query)
            return self.cursor.fetchone().get("count")
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_sum_analytics_tables de la classe postgres ==> \n", e)
            return False
    
    def get_recent_transactions(self):
        try :
            query = """SELECT * FROM transactions ORDER BY created_at DESC LIMIT 10"""
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_transactions de la classe postgres ==> \n", e)
            return False
    def get_sum_transactions(self):
        try :
            query = """SELECT SUM(amount) FROM transactions"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_sum_transactions de la classe postgres ==> \n", e)
            return False