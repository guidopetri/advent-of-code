#! /usr/bin/env python3

with open('08-input.txt', 'r') as f:
    image_data = f.read().strip()

height = 6
width = 25

# sample input
# height = 2
# width = 2
# image_data = '0222112222120000'

image_data = [int(x) for x in image_data]

layers = [[] for x in range(len(image_data) // (height * width))]

for layer_idx, layer in enumerate(layers):
    for n in range(height * width):
        layer.append(image_data[n + (layer_idx * height * width)])

final_img = [3 for x in range(height * width)]

for idx, n in enumerate(final_img):
    for layer in layers:
        if layer[idx] != 2 and n == 3:
            final_img[idx] = layer[idx]
            break

print('\n'.join([''.join(['x' if final_img[x + width * y] else '.'
                          for x in range(width)])
                 for y in range(height)]))
