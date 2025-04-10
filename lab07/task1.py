import pandas as pd

dane_studentow = pd.DataFrame({
    'Student': ['Anna', 'Bartek', 'Celina', 'Dawid', 'Ewa', 'Filip', 'Gosia', 'Hubert'],
    'Matematyka': [85, 90, 78, 92, 88, 76, 94, 85],
    'Fizyka': [76, 88, 90, 75, 82, 84, 91, 76],
    'Informatyka': [92, 85, 88, 95, 80, 75, 89, 92]
})
print(dane_studentow["Matematyka"].mean())
print(dane_studentow["Matematyka"].median())
print(dane_studentow["Matematyka"].mode().to_list())