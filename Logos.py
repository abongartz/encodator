nothing = (0, 0, 0)
O = nothing

green = (0, 255, 0)
G = green

red = (255, 0, 0)
R = red

light_grey = (181, 181, 181)
L = grey_L

dark_grey = (135, 135, 135)
D = grey_D


# Ecran vert

full_green = [
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G
]


# 4 actions:

L_4_0 = [
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D,
L, L, D, D, L, L, D, D
]

L_4_1 = [
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D,
G, G, D, D, L, L, D, D
]

L_4_2 = [
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D,
G, G, G, G, L, L, D, D
]

L_4_3 = [
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D,
G, G, G, G, G, G, D, D
]

L_4 = [L_4_0, L_4_1, L_4_2, L_4_3, full_green]


# 5 actions:

L_5_0 = [
O, O, O, O, O, O, O, O,
O, D, L, D, L, D, O, O,
O, D, L, D, L, D, O, O,
O, D, L, D, L, D, O, O,
O, D, L, D, L, D, O, O,
O, D, L, D, L, D, O, O,
O, D, L, D, L, D, O, O,
O, O, O, O, O, O, O, O
]

L_5_1 = [
O, O, O, O, O, O, O, O,
O, G, L, D, L, D, O, O,
O, G, L, D, L, D, O, O,
O, G, L, D, L, D, O, O,
O, G, L, D, L, D, O, O,
O, G, L, D, L, D, O, O,
O, G, L, D, L, D, O, O,
O, O, O, O, O, O, O, O
]

L_5_2 = [
O, O, O, O, O, O, O, O,
O, G, G, D, L, D, O, O,
O, G, G, D, L, D, O, O,
O, G, G, D, L, D, O, O,
O, G, G, D, L, D, O, O,
O, G, G, D, L, D, O, O,
O, G, G, D, L, D, O, O,
O, O, O, O, O, O, O, O
]

L_5_3 = [
O, O, O, O, O, O, O, O,
O, G, G, G, L, D, O, O,
O, G, G, G, L, D, O, O,
O, G, G, G, L, D, O, O,
O, G, G, G, L, D, O, O,
O, G, G, G, L, D, O, O,
O, G, G, G, L, D, O, O,
O, O, O, O, O, O, O, O
]

L_5_4 = [
O, O, O, O, O, O, O, O,
O, G, G, G, G, D, O, O,
O, G, G, G, G, D, O, O,
O, G, G, G, G, D, O, O,
O, G, G, G, G, D, O, O,
O, G, G, G, G, D, O, O,
O, G, G, G, G, D, O, O,
O, O, O, O, O, O, O, O
]

L_5 = [L_5_0, L_5_1, L_5_2, L_5_3, L_5_4, full_green]


# 6 actions:

L_6_0 = [
O, O, O, O, O, O, O, O,
O, D, L, D, L, D, L, O,
O, D, L, D, L, D, L, O,
O, D, L, D, L, D, L, O,
O, D, L, D, L, D, L, O,
O, D, L, D, L, D, L, O,
O, D, L, D, L, D, L, O,
O, O, O, O, O, O, O, O
]

L_6_1 = [
O, O, O, O, O, O, O, O,
O, G, L, D, L, D, L, O,
O, G, L, D, L, D, L, O,
O, G, L, D, L, D, L, O,
O, G, L, D, L, D, L, O,
O, G, L, D, L, D, L, O,
O, G, L, D, L, D, L, O,
O, O, O, O, O, O, O, O
]

L_6_2 = [
O, O, O, O, O, O, O, O,
O, G, G, D, L, D, L, O,
O, G, G, D, L, D, L, O,
O, G, G, D, L, D, L, O,
O, G, G, D, L, D, L, O,
O, G, G, D, L, D, L, O,
O, G, G, D, L, D, L, O,
O, O, O, O, O, O, O, O
]

L_6_3 = [
O, O, O, O, O, O, O, O,
O, G, G, G, L, D, L, O,
O, G, G, G, L, D, L, O,
O, G, G, G, L, D, L, O,
O, G, G, G, L, D, L, O,
O, G, G, G, L, D, L, O,
O, G, G, G, L, D, L, O,
O, O, O, O, O, O, O, O
]

L_6_4 = [
O, O, O, O, O, O, O, O,
O, G, G, G, G, D, L, O,
O, G, G, G, G, D, L, O,
O, G, G, G, G, D, L, O,
O, G, G, G, G, D, L, O,
O, G, G, G, G, D, L, O,
O, G, G, G, G, D, L, O,
O, O, O, O, O, O, O, O
]

L_6_5 = [
O, O, O, O, O, O, O, O,
O, G, G, G, G, G, L, O,
O, G, G, G, G, G, L, O,
O, G, G, G, G, G, L, O,
O, G, G, G, G, G, L, O,
O, G, G, G, G, G, L, O,
O, G, G, G, G, G, L, O,
O, O, O, O, O, O, O, O
]

L_6 = [L_6_0, L_6_1, L_6_2, L_6_3, L_6_4, L_6_5, full_green]


# 7 actions:

L_7_0 = [
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O,
L, D, L, D, L, D, L, O
]

L_7_1 = [
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O,
G, D, L, D, L, D, L, O
]

L_7_2 = [
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O,
G, G, L, D, L, D, L, O
]

L_7_3 = [
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O,
G, G, G, D, L, D, L, O
]

L_7_4 = [
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O,
G, G, G, G, L, D, L, O
]

L_7_5 = [
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O,
G, G, G, G, G, D, L, O
]

L_7_6 = [
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O,
G, G, G, G, G, G, L, O
]

L_7 = [L_7_0, L_7_1, L_7_2, L_7_3, L_7_4, L_7_5, L_7_6, full_green]


# 8 actions:

L_8_0 = [
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D,
L, D, L, D, L, D, L, D
]

L_8_1 = [
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D,
G, D, L, D, L, D, L, D
]

L_8_2 = [
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D,
G, G, L, D, L, D, L, D
]

L_8_3 = [
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D,
G, G, G, D, L, D, L, D
]

L_8_4 = [
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D,
G, G, G, G, L, D, L, D
]

L_8_5 = [
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D,
G, G, G, G, G, D, L, D
]

L_8_6 = [
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D,
G, G, G, G, G, G, L, D
]

L_8_7 = [
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D,
G, G, G, G, G, G, G, D
]

L_8 = [L_8_0, L_8_1, L_8_2, L_8_3, L_8_4, L_8_5, L_8_6, L_8_7, full_green]

main_list = [L_4, L_5, L_6, L_7, L_8]
