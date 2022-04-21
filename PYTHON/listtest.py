data = []
sub = ['국어','영어','수학']
name = ['철수', '영희', '민수']

for i in range(3):
  score = []
  print('[%d번 학생 %s 점수입력하기]' % (i+1, name[i]))
  for j in range(3):
    num = int(input('%s의 %s점수 입력하시오:' % (name[i], sub[j] )))
    score.append(num)
  data.append(score)
  print()

for i in range(3):
  total = 0
  for j in range(3):
    total += data[i][j]
  print('%s의 총점:%d    평균:%.1f' % (name[i], total, total/3))
