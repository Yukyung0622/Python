#특정 글자수 변환
oneLine = 'this is one line string'
print('t 글자수 : ',oneLine.count('t'))

#접두어 문자 비교 판단
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

#문자열 교체
print(oneLine.replace('this', 'that'))

#문자열 분리(split) : 문단 -> 문장
multiLine = """this is
multi line
string"""
sent = multiLine.split('\n')
print('문장 : ', sent)

#문자열 분리(split)2 : 문단 -> 단어
words = oneLine.split(' ') # split(sep ='') :default

#문자열 결합(join) : 단어 -> 문장
sent2 = ',' .join(words) #'구분자'.join(string)
print(sent2) #this, is, one, line, string