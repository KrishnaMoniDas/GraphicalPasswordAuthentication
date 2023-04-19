from sqlalchemy import create_engine, text

db_conn_string = "mysql+pymysql://qirgad7c97n0cvuescwl:pscale_pw_NkvqW2zs0hHVFIs3lSVr6wjCjCxitgsWkdIAoxJYr7g@aws.connect.psdb.cloud/graphicalpasswordauthentication?charset=utf8mb4"

engine=create_engine(db_conn_string,
                    connect_args={
                      "ssl":{
                        "ssl_ca" : "/etc/ssl/cert.pem"
                      }
                    }
                    )

def load_users_from_db():
  with engine.connect() as conn :
    result = conn.execute(text("select * from users"))
    users = []
    for row in result:
      user_dict = {column[0]:value for column, value in zip(result.cursor.description, row)}
      users.append(user_dict)
    return users

