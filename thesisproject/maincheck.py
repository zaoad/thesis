from check_class import checkclass
obj=[]
class1=checkclass(1)
print(class1.a,class1.dict,class1.list)
obj.append(class1)
print(obj[0].a,obj[0].dict,obj[0].list)
obj[0].dict[0]=1
obj[0].list.append(1)
print(obj[0].a,obj[0].dict,obj[0].list)
class2=checkclass(2)
print(class2.a,class2.dict,class2.list)
print(class1.a,class1.dict,class1.list)
obj.append(2)
