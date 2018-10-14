from suds.client import Client
##拿到远端对象
user=Client("http://115.28.108.130:4000/?wsdl").service
res=user.addUser("韩长远3","123456")
print(res)