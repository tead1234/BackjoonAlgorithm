import ycnbc

data = ycnbc.News()

# get trending news
trending_ = data.trending() # return DataFrame

# get latest news
latest_ = data.latest() # return DataFrame

# get news by category
economy_ = data.economy() # return DataFrame

print(economy_)
# etc.