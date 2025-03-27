import pandas as pd

data = {'Student': ['Anna', 'Bartek', 'Celina', 'Daniel'],
        'Matematyka': [4.5, 3.5, 5.0, 3.0],
        'Fizyka': [4.0, 4.5, 3.5, 3.0],
        'Informatyka': [5.0, 3.0, 4.5, 4.0]}
frame = pd.DataFrame(data)
frame.info()
print(frame.count())
