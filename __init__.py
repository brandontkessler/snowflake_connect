import snowflake.connector
import pandas as pd

class Snowflake:
    def __init__(self, user, password, account):
        self.user = user
        self.password = password
        self.account = account
    
    def connect(self):
        conn = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account
        )
        cur = conn.cursor()
        return conn,cur

    def pyql(self, query):
        conn, cur = self.connect()
        cur.execute(query)

        colnames = [desc[0] for desc in cur.description]
        results = pd.DataFrame(data=cur.fetchall(), columns=colnames)

        cur.close()
        conn.close()
        return results

if __name__=='__main__':
    user='305915'
    password='Wildcat1982!'
    account='petco.us-east-1'

    query = """
        select * 
        from WHPRD_VW.DWADMIN.FT_UPC_SLS_PALS
        limit 10;
    """

    db = Snowflake(user, password, account)
    df = db.pyql(query)
    print(df.head())