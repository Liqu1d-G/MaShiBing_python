# 查询闪退原因，随后根据实际情况解决相应问题。
# 创建test.py文件
# 修改需要执行的exe文件路径
# 使用python运行该程序即可打印出闪退原因
import os
result=os.popen(r"E:\CODE\python\MaShiBing\chap16\exe2.0\stusystem.exe")
print(result.read())