all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def generate_li(object):
	return ('<li>'+object["label"]+'</li>')

def filter_colors(object):
	if (object["sexy"]==True):
		return object["label"]
result =list(filter(filter_colors, all_colors))

result =list(map(generate_li, result))
print(result)