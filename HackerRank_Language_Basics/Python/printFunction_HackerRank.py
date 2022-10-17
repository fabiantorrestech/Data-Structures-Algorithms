#problem: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n+1):
        if i==0:
            continue
        else:
            print(i, end="")
        