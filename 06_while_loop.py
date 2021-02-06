'''
How while loop works in python
'''

import time

counter = 1
while counter <= 10:
    time.sleep(1.5)
    print(counter)
    counter += 1

print('Good bye!!!')