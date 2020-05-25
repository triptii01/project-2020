s = "hello to everyone, hello friends"

def find_second(search_str, target_str):
       a = s.find("hello")
       b = s.find("hello", a+1)
       return b

print(find_second(s,"hello"))


x = "there are different subjects in different type of streams."

def find_2(search, target):
      return search.find(target, search.find(target) + 1)

print(find_2(x,"different"))
