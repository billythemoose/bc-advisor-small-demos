class subject:
    def __init__(self,subname,cource_list,deg_pri,other_name,info):
        self.s = subname
        self.cl = cource_list
        self.dp = deg_pri
        self.info = info

    def get_cources(self):
        return self.cl;

    def get_other_name(self):
        return self.other_name;

class courcebase:
    n = ''
    def __init__(self,name,num,credit,pro,des):
        self.n = name
        self.num = num
        self.cr = credit
        self.pro = pro
        self.des = des
    def get_courcename(self):
        return self.n;
    def get_credit(self):
        return self.cr
    def get_professor(self):
        return self.pro
    def get_description(self):
        return self.des
    
cs001 = courcebase('cs001','001',6,'mr A',"this is a cs class")
lista = [cs001.get_courcename()]
#print(cs001.get_credit())
#print(cs001.get_courcename)
cs = subject('computerscience',lista,'master','cos',"This is the cs major")
listb = cs.get_cources()
print(listb[0])
