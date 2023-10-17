Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
use org
go
create table [dbo].[dept](
[deptno] [int] NOT NULL,
[dname] [varchar](20) NULL,
[loc] [varchar](15) NULL
) ON [PRIMARY]

create table [dbo].[emp](
[empno] [int] NOT NULL,
[ename] [varchar](20) NULL,
[job] [varchar](20) NULL,
[mgr] [int] NULL,
[hiredate] [datetime] NULL,
[sal] [int] NULL,
[comm] [int] NULL,
[dept] [int] NULL
)

INSERT [dbo].[dept] ([deptno], [dname], [loc]) VALUES(10, 'ACCOUNTING', 'NEW YORK')
INSERT [dbo].[dept] ([deptno], [dname], [loc]) VALUES(20, 'RESEARCH', 'DALLAS')
INSERT [dbo].[dept] ([deptno], [dname], [loc]) VALUES(30, 'SALES', 'CHICAGO')
INSERT [dbo].[dept] ([deptno], [dname], [loc]) VALUES(40, 'OPERATIONS', 'BOSTON')

INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7369, 'SMITH', 'CLERK', 7902, '1980-12-17 0:00', 800, NULL, 20)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7499, 'ALLEN', 'SALESMAN',7698,'1981-02-20 0:00', 1600, 300, 30)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7521, 'WARD', 'SALESMAN', 7698,'1981-02-22 0:00', 1250, 500, 30)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7566, 'JONES', 'MANGER', 7839, '1981-04-02 0:00', 2975, NULL, 20)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 0:00', 1250, 1400, 30)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 0:00', 2850, NULL,30)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 0:00', 2450, NULL,10)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7788, 'SCOTT', 'ANALYST', 7566, '1982-12-09 0:00', 3000, NULL, 20)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7839, 'KING', 'PRESIDENT', NULL, '1981-09-08 0:00', 5000, NULL, 10)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 0:00', 1500, 0, 30)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7876, 'ADAMS', 'CLERK', 7788, '1983-01-12 0:00', 1100, NULL, 20)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7900, 'JAMES', 'CLERK', 7698, '1981-12-03 0:00', 950, NULL, 30)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7902, 'FORD', 'ANALYST', 7566, '1981-12-03 0:00', 3000, NULL, 20)
INSERT [dbo].[emp] ([empno], [ename], [job], [mgr], [hiredate], [sal], [comm], [dept]) VALUES(7934, 'MILLER', 'CLERK', 7782, '1982-01-23 0:00', 1300, NULL,10)

 
SELECT MAX(sal) FROM emp


select ename, job from emp

select ename,sal,comm,(sal+((sal*comm)/100)) as "total sal" from emp

select MIN(sal) as dept20 from emp 
 
 select * from emp where job not in ('CLERK')
 
 select hiredate,count(hiredate)
 from emp
 group by hiredate

 select * from  emp where job not in ('MANAGER')

 select * from emp where sal=(select MAX(sal) from emp)

 select dept,sum(sal) from emp GROUP BY dept 

 select * from emp where dept=10 and job in (select job from emp where dept=30)
 
 select * from dept WHERE dname='sales' OR dname='RESEARCH' ORDER BY dname 

 select MAX(SAL)'MAX SAL', MIN(SAL)'MIN SAL', AVG(SAL)'AVG SAL',dept
 from emp
 group by dept

 SELECT COUNT(*),ename,dept-10
 from emp
 where dept=dept
 group by ename,dept-10

 

 select * from emp where sal in (select sal from emp where ( ename ='SCOTT' OR ename= 'WARD')) 
