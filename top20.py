
##########################《对〈https://github.com/simble1986/LearningPython〉的学习记录》######################################
##########################《〈列表〉》######################################
##########################《〈列表〉》######################################
##########################《〈列表〉》######################################
def Listtest() :  
    print ("1.生成两个列表")
    list1 = list(range(1,10))
    list2 = list(range(11,21))
    print(list(list1))
    print(list(list2))

    print(" ")
    print ("2.对第一个列表进行操作，分别在头部增加0和尾部增加10,3.对第二个列表进行操作，删除20")
    list1.insert(0, 0) #在1这个位置添加元素
    list2.remove(20)
    print(list1)
    print(list2)
    print(" ")
    print ("4.将列表1与列表2合并为一个列表（列表3）")
    list1.extend(list2)
    print("合并列表1、2：  ",list1)

    #object [ start : end : step ]
    print(" ")
    print ("5.从合并后的列表（列表3）中每3个元素取出一个")
    list3 = list1[0:19:3]
    print(list3)

    print ("6.对列表进行逆序操作")
    list1.reverse()
    print("reverse: ",list1)
    print ("7.查找列表中是否包含11", 11 in list1)
    print ("8.计算列表长度",len(list1))

def zidian():
    dict1 = {"key1":1,"key2":3, "key9":2, "key4":9, "key5":100}
    dict2 = {"key1":65,"key9":36,"key3":32}

    dict1['key7','key3'] = "36", "12"
    dict1['key5'] = 15
    dict1.pop('key9')
    dict1.update(dict2)	#把dict2的键/值更新到dict里
    
    for i in sorted(dict1.items(), key=lambda x:x[1]):
     print (i)

#
def qiantao3():
 Jim = {"name": 'Jim', "scores": [90.0, 85.0]}
 Sue = {"name": 'Sue', "scores": [75.0, 88.0]}
 Lily = {"name": 'Lily', "scores": [99.0, 92.0]}
 student = [Jim,Sue,Lily]
 print(student)
 score3=[95.0, 90.0, 89.0]
 #sum(scores)/len(scores)
 for i in range(len(score3)):
   student[i]["scores"].append(score3[i])
 print(student)

#体会两种for循环（两个for位置调换效果不同）
def qiantao4():
 Jim = {"name": 'Jim', "scores": [90.0, 85.0]}
 Sue = {"name": 'Sue', "scores": [75.0, 88.0]}
 Lily = {"name": 'Lily', "scores": [99.0, 92.0]}
 student = [Jim,Sue,Lily]
 print(student)
 score3=[95.0, 90.0, 89.0]
 #sum(scores)/len(scores)
 for j in student:
    print("j={}".format(j))
    for i in score3:
     print("i={}".format(i))
        #print("student[j]"scores"[1]={}".format)
        #student[j]["scores"].append(score3[i])  
 #print(循环score3，再嵌套循环student)

def qiantao5():
 Jim = {"name": 'Jim', "scores": [90.0, 85.0]}
 Sue = {"name": 'Sue', "scores": [75.0, 88.0]}
 Lily = {"name": 'Lily', "scores": [99.0, 92.0]}
 student = [Jim,Sue,Lily]
 print(student)
 score3=[95.0, 90.0, 89.0]
 #sum(scores)/len(scores)
 for i in range(len(student)):
    #print("score3[i]={}",format(score3[i]))
    print("我要新插入的值={}".format(score3[i]))
    print("我要插到的地方={}".format(student[i]))
    student[i]["scores"].append(score3[i])
 print("我插入后长这样=",student)
 print("输出Sue字典的name的value值",student[1]["name"])
 print("——————觉悟for循环————————列表当数组访问list[0],list[1]")


#强制类型转换，数据类型判断，数据格式化等操作通常被用于输入输出或变量传递过程中，以避免用户或其他人使用时出现异常的情况。希望通过本次练习，了解一些通常的操作
def test4() :
    items = [{"t": "meat", "price": [15, 25, 30], "num": 30}, {"t": "mushroom", "price": ["3.5", "5.5"], "num": 20}, {"t": "fruit", "price": 6.5, "num": 15.3}]
    list1 =list(range(1,31)[0::2])
    print(list1)
    #遍历列表的常规操作
    for i in range(len(list1)):
     if list1[i] %7 == 0:
        print("能被7整除的",list1[i])



if __name__ == '__main__':
    #Listtest()
    #zidian()
    #qiantao5()
   test4()
