def division1(x, y):
    return x // y

def division2(x, y):
    return int(x / y)

testInput = [
    {
        'x': 15,
        'y': -4
    },
    {
        'x': 17,
        'y': 13
    },
    {
        'x': 5,
        'y': 10
    },
    {
        'x': -10,
        'y': -3
    },
    {
        'x': -8,
        'y': 2
    }
]    

for item in testInput:
    print(    
    f"x: {item['x']}, y: {item['y']}\n"
    f"Div1: {division1(**item)}\n"
    f"Div2: {division2(**item)}\n"
    )

#%%