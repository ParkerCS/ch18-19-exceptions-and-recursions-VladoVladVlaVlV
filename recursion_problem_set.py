'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''


# 1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.
def solver(k, s):
    while s >= 0:
        if s == 0:
            print(k)
        k += k * (0.2 / 12)
        s -= 1
        return solver(k, s)


solver(10000, 6)


# 2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.
def solver2(k, s):
    while s >= 0:
        if s == 0:
            print(k)
        k += k * (0.2 / 12)
        k -= 100  # I assume you add the value after apr gets calculated
        s -= 1
        return solver2(k, s)


solver2(10000, 36)


# 3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.
def solver3(k):
    try:
        while k > 0:
            k += k * (0.2 / 12)
            k -= 100  # I assume you add the value after apr gets calculated
            return solver3(k)
    except:
        print("You will never repay your debt")


solver3(10000)





# 4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on.  Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.
def pyramid(n,m):
    if n>=0:
        m += n
        n -= 1
        pyramid(n, m)
        if n==0:
            print(m)


pyramid(4,0)