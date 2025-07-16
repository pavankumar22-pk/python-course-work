#1

date=input("enter the date in dd-mm-yyyy format")
dd,mm,yyyy=date.split('-')
formatted_date=f"{yyyy}/{mm}/{dd}"
print(formatted_date)'''

#3vowel replacer bot
'''msg=input("enter the message")
vowels='aeiou'
result=''
for ch in msg:
    if ch in vowels:
        result += '*'
    else:
        result += ch
print("modified message:", result)'''

#4.cart analyzer
'''prices=list(map(float,input("enter the  prices:").split()))
total=sum(prices)
maximum=max(prices)
print("total price:",total)
print("max price:",maximum)'''

#5 secure login system
'''credintials= ("admin", "python123")
username=input("enter username")
password=input("enter password")
if credintials[0] == username and credintials[1] == password:
    print("login successful")
else:
    print("aceess denied")



 #5 lgin system
'''credentials=("admin", "python123")
username=input()
password=input()
if(username,password)==credentials:
   print("login successful") 
else:
   print("acceess denied")'''


#6 remove duplicates
'''names=input().split(',')
unique_names=sorted(set(names))
print(unique_names)'''

#7student marrks record
'''n=int(input())
marks_dict={}
for _ in range(n):

    name,mark=input().split()
    marks_dict[name]=int(mark)
top_student=max(marks_dict,key=marks_dict.get)
print(top_student)'''


#8 reverse the words
'''sentence = input()
words = sentence.split()
reversed_words=[word[::-1] for word in words]
output = ' '.join(reversed_words)
print(output)'''

#9 clean the list
'''numbers=input().split()
cleaned_list=[int(num) for num in numbers if int(num) !=0]
print(cleaned_list)'''

#10 alphabet frequency counter
'''text=input()
freq={}
for char in text:
    if char !=' ':
        if char in freq:
            freq[char] +=1
        else:
            freq[char]=1
print(freq)'''


