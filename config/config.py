"""项目配置文件"""
import os
import logging





#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(prj_path,'data')
testcase_path=os.path.join(prj_path,'testcase')
report_file = os.path.join(prj_path,'report','report.html')
log_file =os.path.join(prj_path,'log','log.txt')




##日志配置
logging.basicConfig(level=logging.DEBUG,  # log level##级别
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式




#数据库配置
db_host="115.28.108.130"
db_port=3306
db_user="test"
db_password="123456"
db="api_test"











#邮件配置
smtp_server="smtp.qq.com"
smtp_user="2869600290@qq.com"
smtp_password="fmiqwvosquxcddjg"
sender=smtp_user
receiver="2869600290@qq.com"
subject="接口测试邮件"
is_send_email=False#是否发送邮件


if __name__ == "__main__":
    print(prj_path)
    print(data_path)
    print(report_file)
    print(log_file)
    print(testcase_path)