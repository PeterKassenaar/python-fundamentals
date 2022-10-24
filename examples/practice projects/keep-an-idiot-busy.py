# P. 194: Sample project: 'how to keep an idiot busy for hours', from 'Automate the boring stuff with Python', Seigwart.
# using the pyinputplus module.
# This module must be installed separately. See also https://pypi.org/project/PyInputPlus/.
# using 'pip install pyinputplus'

import pyinputplus as pyip

while True:
    prompt = 'Do you want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt=prompt)
    if(response == 'no'):
        break
print('Thank you, have a nice day')
