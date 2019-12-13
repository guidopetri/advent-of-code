#! /usr/bin/env python3

with open('08-input.txt', 'r') as f:
    image_data = f.read().strip()

height = 6
width = 25

# sample input
# height = 2
# width = 3
# image_data = '123456789012'

image_data = [int(x) for x in image_data]

layers = [[] for x in range(len(image_data) // (height * width))]

for layer_idx, layer in enumerate(layers):
    for n in range(height * width):
        layer.append(image_data[n + (layer_idx * height * width)])
sorted_layers = sorted(layers, key=lambda x: x.count(0))

print(sorted_layers[0].count(1) * sorted_layers[0].count(2))
