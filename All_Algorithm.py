####################### 2장 #######################
# K번째 약수
# (1)
# n,k = map(int,input().split())
# data = []
#
# for i in range(1,n+1): # 1,2,3,4,5,6
#     if (n % i == 0):
#         data.append(i)
#
# if len(data) < k:
#     print(-1)
# else:
#     print(data[k-1])
# (2)
# n,k = map(int,input().split())
# cnt = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)


# k번째 수
# t = int(input())
# for i in range(t):
#     n,s,e,k = map(int,input().split())
#     data = list(map(int,input().split()))
#     new_data = data[s-1:e]
#     new_data.sort()
#     print("#%d %d" % (i + 1, new_data[k - 1]))


# k번째 큰 수
# (1)
# n, k = map(int,input().split())
# data = list(map(int,input().split()))
#
# new_data = []
# for i in range(len(data)):
#     for j in range(i+1,len(data)):
#         for q in range(j+1,len(data)):
#             new_data.append(data[i]+data[j]+data[q])
#
# last_data = []
# for value in new_data:
#     if value not in last_data:
#         last_data.append(value)
#
# last_data.sort(reverse=True)
# print(last_data[k-1])
# (2)
# n, k = map(int,input().split())
# data = list(map(int,input().split()))
# res = set()
#
# for i in range(n):
#     for j in range(i+1,n):
#         for m in range(j+1,n):
#             res.add(data[i]+data[j]+data[m])
#
# res = list(res)
# res.sort(reverse=True)
# print(res[k-1])


# 대표값
# n = int(input())
# data = list(map(int,input().split()))
# ave = round((sum(data) / n) + 0.5)  # 파이썬은 round_half_even 방식 채택
# min = 21470000
#
# for idx, x in enumerate(data):
#     tmp = abs(x - ave)
#     if tmp < min:
#         min = tmp
#         score = x
#         res = idx +1
#     elif tmp == min:
#         if x > score:
#             score = x
#             res = idx + 1
# print(ave, res)


# 정다면체
# n, k = map(int,input().split())
# cnt = [0] * (n+k+3)
# max = -2147000
#
# for i in range(1,n+1):
#     for j in range(1, k+1):
#         cnt[i+j] += 1
# for i in range(n+k+1):    # 최대값 찾기
#     if cnt[i] > max:
#         max = cnt[i]
# for i in range(n+k+1):
#     if cnt[i] == max:
#         print(i, end=" ")


# 자릿수의 합
# (1)
# n = int(input())
# data = list(map(int,input().split()))
#
# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x = x // 10
#     return sum
#
# max = -2147000000
# for x in data:
#     tot = digit_sum(x)
#     if tot > max:
#         max = tot
#         res = x
# print(res)

#(2)
# n = int(input())
# data = list(map(int,input().split()))
#
# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum
#
# max = -2147000000
# for x in data:
#     tot = digit_sum(x)
#     if tot > max:
#         max = tot
#         res = x
# print(res)


# 소수
# n = int(input())
# ch = [0] * (n+1)
# cnt = 0
#
# for i in range(2,n+1):
#     if ch[i] == 0:
#         cnt += 1
#         for j in range(i,n+1,i):
#             ch[j] = 1
# print(cnt)


# 뒤집은 소수
# n = int(input())
# data = list(map(int,input().split()))
#
# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10
#         res = (res * 10) + t
#         x //= 10
#     return res
#
# def isPrime(x):
#     if x == 1:
#         return False
#     for i in range(2,x//2+1):
#         if x % i == 0:
#             return False
#     else:
#         return True
#
# for x in data:
#     tmp = reverse(x)
#     if isPrime(tmp):
#         print(tmp, end=' ')


# 주사위 게임
# n = int(input())
#
# res = 0
# for i in range(n):
#     tmp = input().split()
#     tmp.sort()
#     a,b,c = map(int, tmp)
#     if a == b and b == c:
#         money = 10000 + a * 1000
#     elif a == b or a == c:
#         money = 1000 + a  * 100
#     elif b == c:
#         money = 1000 + b * 100
#     else:
#         money = c * 100
#     if money > res:
#         res = money
# print(res)
#
#
# 점수계산
# n = int(input())
# a = list(map(int,input().split()))
# sum = 0
# count = 0
#
# for i in data:
#     if i == 1:
#        count += 1
#        sum += count
#     else:
#         count = 0
# print(sum)



####################### 3장 #######################
# 회문 문자열 검사
# (1)
# n = int(input())
#
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size//2):
#         if s[j] != s[-(j+1)]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))
# (2)
# if s == s[::-1]:
#     print("#%d YES" % (i + 1))
# else:
#     print("#%d NO" % (i + 1))


# 숫자만 추출
# s = input()
#
# res = 0
# for i in s:
#     if i.isdecimal():
#         res = res * 10 + int(i)
#
# cnt = 0
# for i in range(1,res+1):
#     if res % i == 0:
#         cnt += 1
# print(cnt)


# 카드 역배치
# (1)
# data = []
# for i in range(0,21):
#     data.append(i)
#
# for i in range(10):
#     a,b = map(int,input().split())
#     data[a:b+1] = data[b:a-1:-1]
#
# for i in range(1,21):
#     print(data[i],end=' ')

# (2)
# a = list(range(21))
# for _ in range(10):
#     s, e = map(int,input().split())
#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i] = a[e-i], a[s+i]
# a.pop(0)  # 0번 인덱스 제거
# for x in a:
#     print(x,end=" ")


# 두 리스트 합치기
# n = int(input())
# a = list(map(int,input().split()))
# m = int(input())
# b = list(map(int,input().split()))
#
# p1=p2=0
# c = []
# while p1 < n and p2 < m:
#     if a[p1] <= b[p2]:
#         c.append(a[p1])
#         p1 += 1
#     else:
#         c.append(b[p2])
#         p2 += 1
# if p1 < n:
#     c += a[p1:]
# if p2 < m:
#     c += b[p2:]
# for x in c:
#     print(x,end=' ')


# 수들의 합
# n,m = map(int,input().split())
# a = list(map(int,input().split()))
# lt = 0
# rt = 1
# tot = a[0]
# cnt = 0
#
# while True:
#     if tot < m:
#         if rt < n:
#             tot += a[rt]
#             rt += 1
#         else:
#             break
#     elif tot == m:
#         cnt += 1
#         tot -= a[lt]
#         lt += 1
#     else:
#         tot -= a[lt]
#         lt += 1
# print(cnt)


# 격자판 최대합
# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# largest = -2147000000
#
# for i in range(n):
#     sum1 = sum2 = 0
#     for j in range(n):
#         sum1 += a[i][j]
#         sum2 += a[j][i]
#     if sum1 > largest:
#         largest = sum1
#     if sum2 > largest:
#         largest = sum2
#
# sum1=sum2 =0
# for i in range(n):
#     sum1 += a[i][i]
#     sum2 += a[i][n-i-1]
# if sum1 > largest:
#     largest = sum1
# if sum2 > largest:
#     largest = sum2
#
# print(largest)


# 사과나무(다이아몬드)
# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# res = 0
# s = e = n//2
#
# for i in range(n):
#     for j in range(s, e+1):
#         res += a[i][j]
#     if i < n//2:
#         s -= 1
#         e += 1
#     else:
#         s += 1
#         e -= 1
# print(res)


# 곳감(모래시계)
# n = int(input())
# data = [list(map(int,input().split())) for _ in range(n)]
# m = int(input()) # 명령개수
#
# for i in range(m):
#     h, t, k = map(int,input().split())
#     if t == 0:
#         for _ in range(k):
#             data[h-1].append(data[h-1].pop(0))
#     else:
#         for _ in range(k):
#             data[h-1].insert(0, data[h-1].pop())
#
# res = 0
# s = 0
# e = n-1
# for i in range(n):
#     for j in range(s, e+1):
#         res += data[i][j]
#     if i < n//2:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
# print(res)

# 봉우리
# n = int(input())
# data = [list(map(int,input().split())) for _ in range(n)]
# data.insert(0, [0]*n)
# data.append([0]*n)
# for x in data:
#     x.insert(0,0)
#     x.append(0)
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# cnt = 0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if all(data[i][j] > data[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt += 1
# print(cnt)


# 스토쿠 검사
# def check(data):
#     for i in range(9):
#         ch1 = [0] * 10
#         ch2 = [0] * 10
#         for j in range(9):
#             ch1[data[i][j]] = 1
#             ch2[data[j][i]] = 1
#         if sum(ch1) != 9 or sum(ch2) != 9:
#             return False
#
#     for i in range(3):
#         for j in range(3):
#             ch3 = [0] * 10
#             for k in range(3):
#                 for s in range(3):
#                     ch3[data[i*3+k][j*3+s]]=1
#             if sum(ch3) != 9:
#                 return False
#     return True
#
# data = [list(map(int,input().split())) for _ in range(9)]
# if check(data):
#     print("YES")
# else:
#     print("NO")


# 격자판 회문수
# def check (data):
#     cnt = 0
#     # 행 검사
#     for i in range(7):
#         for j in range(3):
#             if data[i][j] == data[i][j+4] and data[i][j+1] == data[i][j+3]:
#                 cnt += 1
#     # 열 검사
#     for i in range(7):
#         for j in range(3):
#             if data[j][i] == data[j + 4][i] and data[j + 1][i] == data[j+3][i]:
#                 cnt += 1
#
#     return cnt
#
#
# data = [list(map(int,input().split())) for _ in range(7)]
# print(check(data))


####################### 4장 #######################
# 이분검색
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
# lt = 0
# rt = n-1
#
# while lt <= rt:  # 같아질 수도 있음
#     mid = (lt + rt) // 2
#     if m == data[mid]:
#         print(mid+1)
#         break
#     elif m < data[mid]:
#         rt = mid - 1
#     else:
#         lt = mid + 1


# 랜선자르기(결정알고리즘)
# k, n = map(int,input().split())
# Line = []
# res = 0
# largest = 0
# for i in range(k):
#     tmp = int(input())
#     Line.append(tmp)
#     largest = max(largest, tmp)
#
# lt = 1
# rt = largest
#
# def Count(len):
#     cnt = 0
#     for x in Line:
#         cnt += (x//len)
#     return cnt
#
# while lt <= rt:
#     mid = (lt + rt) // 2
#     if Count(mid) >= n:
#         res = mid
#         lt = mid + 1
#     else:
#         rt = mid - 1
#
# print(res)


# 뮤직비디오(결정알고리즘)
# n, m = map(int,input().split())
# data = list(map(int,input().split()))
# max_value = max(data)
# lt = 1
# rt = sum(data)
# res = 0
#
# def Count(capacity):  # dvd 몇 장을 써야하는지 카운트
#     cnt = 1
#     sum = 0
#     for x in data:
#         if sum + x <= capacity:
#             sum += x
#         else:
#             cnt += 1
#             sum = x
#     return cnt
#
# while lt <= rt:
#     mid = (lt+rt) // 2
#     if mid >= max_value and Count(mid) <= m:
#         res = mid
#         rt = mid - 1
#     else:
#         lt = mid + 1
# print(res)


# 마구간 정하기(결정알고리즘)
# n,m = map(int,input().split())
# data = [int(input()) for _ in range(n)]
# data.sort()
#
# lt = 1
# rt = data[n-1]
#
# def Count(len):
#     cnt = 1
#     ep = data[0]
#     for i in range(1,n):
#         if data[i] - ep >= len:
#             cnt += 1
#             ep = data[i]
#     return cnt
#
# while lt <= rt:
#     mid = (lt+rt) // 2
#     if Count(mid) >= m:
#         res = mid
#         lt = mid + 1
#     else:
#         rt = mid - 1
# print(res)


# 회의실 배정(그리디)
# n = int(input())
# data = []  # data [1,4][2,3][3,5][4,6],[5,7]
# for i in range(n):
#     s,e = map(int,input().split())
#     data.append((s,e))
#
# data = sorted(data, key=lambda x:(x[1],x[0]))
#
# et = 0
# cnt = 0
#
# for s,e in data:
#     if s >= et:
#         et = e
#         cnt += 1
# print(cnt)


# 씨름 선수(그리디)
# n = int(input())
#
# data = []
# for i in range(n):
#     h,w = map(int,input().split())
#     data.append((h,w))
# data.sort(reverse=True)
#
# largest = 0
# cnt = 0
#
# for h, w in data:
#     if w > largest:
#         largest = w
#         cnt += 1
# print(cnt)


# 창고 정리
# n = int(input())
# data = list(map(int,input().split()))
# m = int(input())
#
# data.sort()
#
# for _ in range(m):
#     data[0] += 1
#     data[-1] -= 1
#     data.sort()
#
# print(data[-1]-data[0])


# 침몰하는 타이타닉(그리디)
# (1)
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
#
# cnt = 0
#
# while data:
#     if len(data) == 1:
#         cnt += 1
#         break
#     if data[0] + data[-1] > m:
#         data.pop()
#         cnt += 1
#     else:
#         data.pop(0)
#         data.pop()
#         cnt += 1
# print(cnt)

#(2)
# from collections import deque  # 데크를 사용, 인덱스가 바뀌지 않아 더 효율적
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
# data = deque(data)
# cnt = 0
#
# while data:
#     if len(data) == 1:
#         cnt += 1
#         break
#     if data[0] + data[-1] > m:
#         data.pop()
#         cnt += 1
#     else:
#         data.popleft()
#         data.pop()
#         cnt += 1
# print(cnt)


# 증가수열 만들기(그리디)
# n = int(input())
# a = list(map(int, input().split()))
# lt = 0
# rt = n-1
# last = 0
# res = ""
# tmp = []
# while lt <= rt:
#     if a[lt] > last:
#         tmp.append((a[lt], 'L'))
#     if a[rt] > last:
#         tmp.append((a[rt], 'R'))
#     tmp.sort()
#     if len(tmp)==0:
#         break
#     else:
#         res = res + tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1] == 'L':
#             lt = lt+1
#         else:
#             rt = rt-1
#     tmp.clear()
#
# print(len(res))
# print(res)


# 역수열(그리디)
# n = int(input())
# a = list(map(int,input().split()))
# seq = [0] * n
#
# for i in range(n):
#     for j in range(n):
#         if a[i] == 0 and seq[j] == 0:
#             seq[j] = i + 1
#             break
#         elif seq[j] == 0:
#             a[i] -= 1
#
# for x in seq:
#     print(x, end=" ")


####################### 5장 #######################
# 가장 큰 수
# num, m = map(int,input().split())
# num = list(map(int,str(num)))
# stack = []
#
# for x in num:
#     while stack and m > 0 and stack[-1]<x:
#         stack.pop()
#         m -=1
#     stack.append(x)
#
# if m != 0:
#     stack = stack[:-m]
# res = ''.join(map(str,stack))
# print(res)


# 쇠막대기
# s = input()
# stack = []
# cnt = 0
# for i in range(len(s))
#     if s[i] == '(':
#         stack.append(s[i])
#     else:
#         stack.pop()
#         if s[i-1] == '(':
#             cnt += len(stack)
#         else:
#             cnt += 1
# print(cnt)

