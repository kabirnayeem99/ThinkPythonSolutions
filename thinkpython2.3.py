"""suppose the cover price of a book is
 $24.95 , but bookstore get 40% discount . Shipping cost
$3 for first copy, 75 cents for each additional copy. What is the total
wholesale cost for 60 copies?"""

cover_price = float(input('The cover price is:'))
discount_rate = float(input('The rate of discount is:'))
discount_rate2 = discount_rate/100
print('The discount rate is', discount_rate2)
bookstore_buying_price = cover_price / discount_rate2
print('Bookstore buy each book in' , bookstore_buying_price)
total_copies = int(input('Total copies of book is:'))
shipiing_cost_for_first_book = int(input('Shipping cost for first book:'))
copies_more_than_one = total_copies - 1
total_price = (total_copies * bookstore_buying_price) + (shipiing_cost_for_first_book + (copies_more_than_one * 0.75))
print(total_price)

"""if i leave my house at 6:32 am and run 1 mile
(8:15 per mile), then 3 miles at tempo (7:12 per mile)
and 1 mile at easy pace again, what time do I get home for breakfast?
1 mile * 8:15
3 mile * 7:12
1 mile * 8:15
the time I get outside + the time needed to run total"""

easy_pace = float(input('Per mile in easy pace:'))
tempo = float(input('Per mile in tempo:'))
easy_pace = easy_pace / 60
tempo = tempo / 60

in_ep = int(input('distance ran in easy pace:'))
in_t = int(input('distance ran in tempo:'))

time_in_ep = in_ep * easy_pace
time_in_t = in_t * tempo
total = time_in_ep + time_in_t
total = total * 60
print('Total time I ran was:', total)
total = total / 60

ib = float(input('I went outside:'))
ttr = ib + total
if ttr > 6.60:
    ttr = int(6.12 + 1 + (ttr - 6.60))
else:
    ttr = int(ttr)
print('I will return in', ttr)
