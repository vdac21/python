import pyodbc 
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=LAPTOP-1P7LLK45\SQLEXPRESS;"
                      "Database=sample;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()
"""
cursor.execute('create table DATA(policy int,expirydate date,location varchar(10),state varchar(10),region varchar(10),insurencevalue money,construction varchar(10),businesstype varchar(20),eartquake varchar(10),flood varchar(10))')

'''
cursor.execute('''insert into DATA(policy ,expirydate,location,state,region,insurencevalue,construction,businesstype,eartquake,flood) values
               
              (100388,'2021-01-04','Urban','IL','Midwest',12934500,'Frame','Apartment','Y','Y'),
              (100358,'2021-01-05','Urban','WI','Midwest',928300,'Mansonry','OfficeBldg','N','N'),
              (100264,'2021-01-07','Rural','NY','East',2219900,'Frame','Farming','N','N'),
              (100281,'2021-01-13','Rural','WI','Midwest',1432835,'Frame','Farming','N','N'),
              (100426,'2021-01-16','Urban','VT','Northeast',2432875,'FireResist','Apartment','N','N'),
              (100461,'2021-01-20','Urban','WI','Midwest',4380200,'Mansonry','OfficeBldg','Y','Y'),
              (100381,'2021-01-23','Urban','VT','Northeast',7203500,'Frame','OfficeBldg','Y','Y'),
              (100275,'2021-01-25','Urban','WI','Midwest',53410614,'Frame','Construction','Y','Y'),
              (100312,'2021-01-25','Rural','IL','MIdwest',3145700,'Frame','Education','N','N'),
              (100327,'2021-01-25','Urban','WI','Midwest',1451100,'Frame','Recreation','N','N'),
              (100326,'2021-01-26','Urban','OH','Central',1787900,'Frame','OfficeBldg','N','N'),
              (100310,'2021-01-28','Urban','WI','Midwest',8800000,'FireResist','OfficeBLdg','Y','Y'),
              (100289,'2021-01-29','Rural','NY','East',2145420,'Frame','Farming','N','N'),
              (100496,'2021-02-04','Urban','IL','Midwest',1895000,'Mansonry','OfficeBldg','N','N'),
              (100309,'2021-02-05','Urban','WI','Midwest',5000368,'Mansonry','Manufacturing','N','N'),
              (100509,'2021-02-07','Urban','OH','Central',1849000,'MetalClad','Retail','N','N'),
              (100371,'2021-02-08','Urban','OH','Central',218490,'Frame','Apartment','N','N')

''')
'''
cursor.execute('''SELECT POLICY,COUNT(POLICY)
                FROM DATA
                GROUP BY POLICY
                HAVING COUNT(POLICY) >1

                SELECT EXPIRYDATE,COUNT(EXPIRYDATE)
                FROM DATA
                GROUP BY EXPIRYDATE
                HAVING COUNT(EXPIRYDATE)>1

                SELECT REGION,COUNT(REGION)
                FROM DATA
                GROUP BY REGION
                HAVING COUNT(REGION)>1


                SELECT STATE,COUNT(STATE)
                FROM DATA
                GROUP BY STATE
                HAVING COUNT(STATE)>1

                SELECT LOCATION,COUNT(LOCATION)
                FROM DATA
                GROUP BY LOCATION
                HAVING COUNT(LOCATION)>1

                SELECT INSURENCEVALUE,COUNT(INSURENCEVALUE)
                FROM DATA
                GROUP BY INSURENCEVALUE
                HAVING COUNT(INSURENCEVALUE)>1

 
                SELECT CONSTRUCTION,COUNT(CONSTRUCTION)
                FROM DATA
                GROUP BY CONSTRUCTION
                HAVING COUNT(CONSTRUCTION)>1


                SELECT BUSINESSTYPE,COUNT(BUSINESSTYPE)
                FROM DATA
                GROUP BY BUSINESSTYPE
                HAVING COUNT(BUSINESSTYPE)>1

                SELECT Eartquake,COUNT(Eartquake)
                FROM DATA
                GROUP BY Eartquake
                HAVING COUNT(Eartquake)>1

                SELECT FLOOD,COUNT(FLOOD)
                FROM DATA
                GROUP BY FLOOD
                HAVING COUNT(FLOOD)>1
''')

"""

cursor.execute('''alter table DATA alter column Insurencevalue int not null''') 
cursor.execute('''alter table DATA add primary key (policy)''')
cursor.execute('''alter table DATA add unique key (Insurencevalue)''')
conn.commit()

