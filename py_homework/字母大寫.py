
str1=input("請輸入一個小寫英文單字: ");

while( str1.islower() == False ):
    print("請輸入一個全小寫的單字喔~~  ");
    str1=input("請輸入一個小寫英文單字:  ");
print('你輸入的字為: '+ str1.upper()+'，這個字總共有'+str(len(str1))+'個字母');