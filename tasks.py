#1
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if n == 0:
#        return 0
#     else: 
#      return fibo(n-1) + fibo(n-2)
    
# n = int(input())
# print(fibo(n))


#2 
# def power(num,cnt = 1,res = 0):
#          if cnt == num + 1:
#              return res
#          res += pow(cnt,2)
#          return power(num,cnt+1,res)
# m = int(input())
# print(power(m))
#3
# def revrse(a,sum = 0)

#4
# def power(n):
#     if n == 0:
#         return 1
#     else:
#         return 2 * power(n - 1)

# n = int(input())
# print(power(n))

#3
def reverse_n(n,rev=0):
         if n == 0:
             return rev
         rev = rev * 10 + n % 10
         return reverse_n(n // 10,rev)
     
n = int(input())
print(reverse_n(n))

