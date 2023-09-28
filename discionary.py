a = {'1': 2.6,
     '2': 3.2,
     '3': 5.4,
     '4': 9.9,
     '5': 1.7
     }
a = {k: a[k] for k in sorted(a, key=a.get, reverse=False)}

print(a)