这是一个长春理工大学课表的爬虫，它可将课表生成为日历文件（.ics），该文件可以在电脑和手机自带的日历查看。
如果您想使用该爬虫，请将该项目导入pycharm当中。
若要生成课表信息，需要修改main.py中的代码

>[!Caution]
> 1. 此仓库来自于[上游仓库yeqinzhe/CUST-schedule](https://github.com/yeqinzhe/CUST-schedule)<br>
> 2. 本仓库重新适配了更改后的统一身份认证网
> 3. 对于长春理工现有的两个校区课时不同步的安排进行了适配
> 4. 对比原有的仓库的内容增加了易用性，并在README文件中增加更加详细的说明


1.首先您需要获得个人id，
请按F12按钮，找到network，点击之后教学信息一体化服务平台-》全校课表-》按学生-》选择班级，
找到GetStudentBasicInfoLessonOccupy，点击response，搜索（ctrl+f）个人姓名，找到SMXSJBXXID的值填入main.py中的PersonalId

2.点击network并排的application按钮，找到cookies，将ASP.NET_SessionId对应的值填入main.py中的SessionId

~~3.设置服务器编号，教学信息一体化服务平台网址是“jwgls4”开头，则服务器编号为4~~

4.周数range(0,21)代表开学前一周到20周

5.请在downloadJson.py中第31行`"XQJC": "春明湖校区",  # 校区检查`中确认并改写自己的校区（如果是朝阳校区的话）

6.学年学期的第一学期为九月学的学期，并且请确认自己本学期开始的时间，随后在tolCS中第26行`start_date = datetime.date(2026, 8, 24)`中更改本学期开始的日期

>[!Warning]
>* 请注意，个人id是固定的，SessionId则会过期!
>* 并且在程序main运行的过程中不要使用连接海外IP的网络代理防止连接错误
>* 若出现报错`Traceback (most recent call last):
  File "D:\CUST-schedule\main.py", line 21, in <module>
    data_filter(weekRange)
  File "D:\CUST-schedule\filter.py", line 40, in data_filter
    data += convert_to_output(i)
  File "D:\CUST-schedule\filter.py", line 16, in convert_to_output
    for i in data["data"]["AdjustDays"]:
TypeError: 'NoneType' object is not subscriptable`
>请确认获取的SessionId是否有效

电脑段日历
![Alt text](screenshot/browser_Ujk2qvm3SX.png)

手机端日历
(![Screenshot_20250306_132745_One UI Home.jpg](screenshot/Screenshot_20250306_132745_One%20UI%20Home.jpg)images/image.png)
