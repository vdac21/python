import cx_Oracle


class OracleDb:

    def __init__(self, **kwargs):
        self.user = kwargs.get("user")
        self.password = kwargs.get("password")
        self.port = kwargs.get("port")
        self.host = kwargs.get("host")
        self.service_name = kwargs.get("service_name")
        self.con_str = f"{self.user}/{self.password}@{self.host}:{self.port}/{self.service_name}"
        self.cur_obj = None
        self.con_obj = None

        # initiating db connection
        self.connect()

    def connect(self):
        try:
            print(f"Trying to connect oracle db... : {self.con_str}")
            self.con_obj = cx_Oracle.connect(self.con_str)
            self.cur_obj = self.con_obj.cursor()
            print(f"Successfully conncted Oracle db. Host : {self.host}")
        except Exception as e:
            print(f"Unable to connect the db with command :  {self.con_str}")
            print(str(e))

    def get_db_fileds(self, table_name):
        try:
            query = f"SELECT * FROM {table_name} WHERE ROWNUM = 0"
            results = self.cur_obj.execute(query)
            col_names = [row[0] for row in results.description]
            con_lowercase=[]
            for col in col_names:
                con_lowercase.append(col.lower())
            return con_lowercase

        except Exception as e:
            print(f"table doesn't exit in given database: {table_name}")
            print(str(e))

    def get_table_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        print(f"QUERY COMMAND :- {query}")
        results = self.cur_obj.execute(query)
        res = results.fetchall()
        return res

    def update_filed_with_nul(self, table_name, column_name):
        # This method is not working to update the db
        try:
            query = f"UPDATE {table_name} SET {column_name.upper()} = null"

            print(f"QUERY COMMAND:- {query}")
            self.cur_obj.execute(query)
            self.con_obj.commit()
            #self.con_obj.close()
        except Exception as e:
            print(f"Unable to update column with null values : {table_name}\{column_name}")
            print(str(e))

    def get_all_column_values(self, table_name, column):
        """
        This function returns  all values from the given column
        """
        pass
        # return statement


if __name__ == "__main__":
    db =OracleDb(host='localhost', port='1521', user='system', password='Oracle@123', service_name='orcl.docker.internal')
    # --->  Get table filed values
    res = db.get_table_data('sample_data')
    print(res)

    #all_paths = db.get_all_column_values()

