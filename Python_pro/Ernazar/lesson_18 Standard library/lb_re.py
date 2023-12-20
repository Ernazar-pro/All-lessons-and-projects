import re

soz1='temir'
soz2='tamir'
soz3='traktor'

ulgi='^t...r$'

print(re.match(ulgi,soz1))
print(re.match(ulgi,soz2))
print(re.match(ulgi,soz3))