favorite_language=" python "
a_1="1"
print(1,favorite_language,a_1)
print(2,favorite_language.rstrip(),a_1)#rstrip()删除 string 字符串末尾的指定字符，
###默认为空白符，包括空格、换行符、回车符、制表符
print(3,favorite_language.rstrip('n '))
print(4,favorite_language,a_1)
favorite_language=favorite_language.rstrip()
print(5,favorite_language,a_1)
favorite_language=" python "
print("\n",favorite_language,a_1,"\n",favorite_language.rstrip(),a_1,"\n",
      favorite_language.lstrip(),a_1,"\n",favorite_language.strip(),a_1)
#lstrip()左边
#strip()两边
