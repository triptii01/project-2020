s='<a href="https://www.wikipedia.com">wiki</a>'
t='<a href="http://www.google.com"'
u='<a href="http://www.googleweree.com"'
v='<a href="http://www.googlasdasd.com"'

def link(l) :
	x = (l.find('"'))
	print(x)
	y = l.find('"', x+1)
	print(y)
	print(l[x+1:y])

link(s)
link(t)
link(u)
link(v)


