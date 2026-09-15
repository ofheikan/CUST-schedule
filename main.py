from downloadJson import download_jsons
from filter import data_filter
from toICS import to_ics

# 个人id F12 GetStudentBasicInfoLessonOccupy SMXSJBXXID
PersonalId = "862d4596-de18-4673-9a4f-c1024f3ecd26"

# cookie ASP.NET_SessionId
SessionId = "35pobiebnvheij0mad01utdb"

# 服务器编号
#server = 3

# 周数
weekRange = range(0,20)

# 学年学期
year_semester = "20261"

download_jsons(weekRange,PersonalId,SessionId, year_semester)
data_filter(weekRange)
to_ics("all_lessons")
