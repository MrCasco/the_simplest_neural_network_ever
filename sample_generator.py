import random
import json

"""
Meanings:

* Taking this example [1, 0, 1, 0] each index means the following:
    0: left-top corner
    1: right-top corner
    2: bottom-left corner
    3: bottom-right corner
* Each element inside the 4-length array corresponds to one cell in the grid flowing in clockwise direction

* The answers are binary-coded numbers, meaning:
    [1, 1, 1, 1] = 15 in decimal number
    [1, 1, 0, 0] = 12 in decimal
    [1, 0, 1, 0] = 10    ""
    [0, 0, 1, 1] = 3     ""
    and so on...
"""

options = [
    {'input':[1.0, 1.0, 1.0, 1.0] ,'answer':15.0},
    {'input':[0.0, 0.0, 0.0, 0.0] ,'answer':0.0},
    {'input':[1.0, 0.0, 0.0, 1.0] ,'answer':9.0},
    {'input':[0.0, 1.0, 1.0, 0.0] ,'answer':6.0},
    {'input':[1.0, 1.0, 0.0, 0.0] ,'answer':12.0},
    {'input':[0.0, 0.0, 1.0, 1.0] ,'answer':3.0},
    {'input':[0.0, 1.0, 0.0, 1.0] ,'answer':5.0},
    {'input':[1.0, 0.0, 1.0, 0.0] ,'answer':10.0},
]

def generate_samples():
    res = []
    for i in range(10000):
        ix = random.randint(0, 7)
        res.append(options[ix])
    return res

def test(samples):
    count = {key: 0 for key in [0.0, 3.0, 5.0, 6.0, 9.0, 10.0, 12.0, 15.0]}
    for sample in samples:
        key = sample['answer']
        count[key] += 1
    print(count)

def write_samples_to_txt():
    samples = generate_samples()
    json_object = json.dumps(samples, indent=2)

    with open("samples.json", "w") as outfile:
        outfile.write(json_object)

write_samples_to_txt()
