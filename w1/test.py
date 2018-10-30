# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

num_of_books = 30
book_cost = 24.95
bookstore_discount = 0.40
shipping_initial = 3
shipping_additional = 0.75

total_book_cost = book_cost * num_of_books

discounted_cost = total_book_cost * (1 - bookstore_discount)
shipping = shipping_initial + (shipping_additional * (num_of_books - 1))
print(discounted_cost + shipping)
