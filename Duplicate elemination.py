student_data={'id1':{
'name':['Manansh'],
'class':['VI'],
'subject':['English,Mathematics,Science,Hindi,Arabic']
},
'id2':{'name':['Aarav'],
'class':['VI'],
'subject':['English,Mathematics,Science,Hindi,Arabic']
},
'id3':{'name':['Swarup'],
'class':['VI'],
'subject':['English,Mathematics,Science,Hindi,Arabic']
},
'id4':{'name':['Preyanshu'],
'class':['VI'],
'subject':['English,Mathematics,Science,Hindi,Arabic']
},
'id5':{'name':['Manansh'],
'class':['VI'],
'subject':['English,Mathematics,Science,Hindi,Arabic']
},
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)