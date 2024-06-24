import os

import psycopg2
from dotenv import load_dotenv
load_dotenv()
class Postgres() :
    def __init__(self) -> None:
        self.connect =  psycopg2.connect(
            user = "ktmlee",
            database = "promptmaster",
            password = "pass",
            host = "localhost",
        )
        self.cursor = self.connect.cursor()
        
    def init_db(self):
        create_user_table_query = """CREATE TABLE IF NOT EXISTS users(
            uid SERIAL PRIMARY KEY,
            email VARCHAR(250) UNIQUE NOT NULL,
            password VARCHAR(250) NOT NULL,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            is_superuser BOOL DEFAULT FALSE,
            is_staff BOOL DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT NOW(),
            last_login TIMESTAMP
        );
        """
        create_prompt_table_query = """CREATE TABLE IF NOT EXISTS prompt
            Prompt_id SERIAL PRIMARY KEY,
            title VARCHAR(250) UNIQUE NOT NULL,
            text VARCHAR(250) NOT NULL,
            tags VARCHAR(100),
            price integer,
            state varchar(10),
            vote integer,
            created_at TIMESTAMP DEFAULT NOW(),
            constraint fk_uid foreign key(fk_uid) references users(uid)
        );
        """
        self.cursor.execute(create_user_table_query,create_prompt_table_query)
        self.connect.commit()
    
    def create_user(self, email, password,**kwargs ):
        try :
            query = """INSERT INTO users(email, password, first_name, last_name, is_superuser, is_staff)
                       VALUES (%s, %s, %s, %s, %s, %s)
                    """
            values  = (email, password, kwargs.get("first_name"), kwargs.get("last_name"), kwargs.get("is_superuser", False), kwargs.get("is_staff", False))
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "Utilisateur cree avec success"
        except psycopg2.errors.UniqueViolation as e :
            return False, "Un utilisateur avec cet email existe deja"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction create_user de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer" 
    
    def get_data_table(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            
            if rows:
                # Obtenir les noms des colonnes
                colnames = [desc[0] for desc in self.cursor.description]
                
                # Créer une liste de dictionnaires
                data_list = [dict(zip(colnames, row)) for row in rows]
                
                return data_list
            else:
                return []
        except Exception as e:
            print("Une erreur s'est produite dans la fonction get_data_table de la classe postgres ==> \n", e)
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
            row = self.cursor.fetchone()
        
            if row:
                colnames = [desc[0] for desc in self.cursor.description]
                user_dict = dict(zip(colnames, row))
                return user_dict
            else:
                return None
        except Exception as e :
            print("Une erreur s'est produite dans la fonction get_user_by_email de la classe postgres ==> \n", e)
            return False 
        
    def create_prompt(self, title, text,**kwargs ):
        try :
            query = """INSERT INTO prompt(title,text,tags,price,state,vote)
                       VALUES (%s, %s, %s, %s, %s, %s)
                    """
            values  = (title, text, kwargs.get("tags"), kwargs.get("price"), kwargs.get("state", False), kwargs.get("vote", False))
            self.cursor.execute(query, values)
            self.connect.commit()
            return True, "prompt cree avec success"
        except psycopg2.errors.UniqueViolation as e :
            return False, "Un prompt avec ce titre existe deja"
        except Exception as e :
            print("Une erreur s'est produite dans la fonction create_prompt de la classe postgres ==> \n", e)
            return False, "Une erreur s'est produite , veuillez reesayer" 