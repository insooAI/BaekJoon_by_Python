#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# # 1

# In[7]:


name = input('이름을 입력하세요 : ')
print('Hello', name)


# # 2 

# In[8]:


firstName = input('성을 입력하세요 : ')
lastName = input('이름을 입력하세요 : ')
print('Hello', firstName, lastName)


# # 3

# In[14]:


joke = 'what do you call a bear with no teeth'
answer = 'a gummy bear!'

if bool(joke) == True:
    print(answer)


# # 4

# In[15]:


number1 = int(input('숫자1을 입력하세요.'))
number2 = int(input('숫자2을 입력하세요.'))

print(f'the total is {number1 + number2}')


# # 5

# In[16]:


number1 = int(input('숫자1을 입력하세요.'))
number2 = int(input('숫자2을 입력하세요.'))
number3 = int(input('숫자3을 입력하세요.'))


print(f'the answer is {(number1 + number2) * number3}')


# # 6

# In[17]:


original = input('처음에 가지고 있었던 피자 조각의 개수는? : ')
eat = input('먹은 피자 조각의 개수는? : ')
rest = int(original) - int(eat)
print(f'남은 조각의 개수는 : {rest}')


# # 7

# In[20]:


name = input('이름을 입력하세요 : ')
age = int(input('나이를 입력하세요 : '))
print(f'next birthday you will be {age+1}')


# # 8 

# In[22]:


bill = int(input('총 가격 : '))
person = int(input('인원 수를 입력하세요 : '))
print(f'각자 내야할 돈은 {int(bill / person)}')


# # 9

# In[24]:


day = int(input('날짜 수 : '))

hours = day * 24
minutes = hours * 60
seconds = minutes * 60

print(f'{hours}시간 {minutes}분 {seconds}초 남았습니다.')


# # 10

# In[26]:


weight = int(input('몸무게를 입력해주세요 : '))
print(f'파운드로 계산한 몸무게는 다음과 같습니다. {weight * 2.204}')


# # 11

# In[31]:


number1 = int(input('100보다 큰 수를 입력하세요.'))
number2 = int(input('10보다 작은 수를 입력하세요.'))

print(f'{number1 // number2}번 들어갑니다.')


# In[ ]:




