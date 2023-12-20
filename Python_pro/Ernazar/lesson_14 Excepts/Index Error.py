colors=['Blue','Green','Niger','Yellow','White']

try:
    color=colors[5]
except IndexError:
    print(f'colors tin ishinde {len(colors)} dana element bar')
else:
    print(color)