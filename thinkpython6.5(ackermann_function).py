"""
Copyright Kabir Nayeem <kabirnayeem.99@gmail.com>
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

In computability theory, the Ackermann function, named after Wilhelm Ackermann, is one of the simplest and earliest-discovered examples of a total computable function that is not primitive recursive. All primitive recursive functions are total and computable, but the Ackermann function illustrates that not all total computable functions are primitive recursive. 
"""

def A(m, n):
	if m == 0:
		n + 1
		a = n + 1
		print(a)
		return (a)
	elif n == 0:
		print(A(m - 1, 1))
		return A(m - 1, 1)
	a = A((m-1), A(m, n - 1))
	print(a)
	return a

m = int(input())
n = int(input())
A(m, n)
"""there is something wrong with this code, it has a runtime error when m is bigger than n"""
