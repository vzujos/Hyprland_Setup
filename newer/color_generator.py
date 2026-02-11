from colorsys import hls_to_rgb


def calculate_deltas(c1, c2):
    h1, s1, l1 = c1
    h2, s2, l2 = c2

    Dh = h2 - h1
    if Dh > 180: Dh -= 360
    elif Dh < -180: Dh += 360
    Ds = s2 - s1
    Dl = l2 - l1
    return Dh, Ds, Dl


def gen_palette_hsl(base_color, deltas):
    palette = [base_color]
    h1, s1, l1 = base_color
    for delta in deltas:
        h_i = (h1 + delta[0]) % 360  # Asegurarse de que el tono esté en el rango [0, 360]
        s_i = max(0, min(100, s1 + delta[1])) # Limitar la saturación entre 0 y 100
        l_i = max(0, min(100, l1 + delta[2])) # Limitar la luminosidad entre 0 y 100
        palette.append((h_i, s_i, l_i))
    return palette


def hsl_to_rgb(color):
    h, s, l = color
    rgb_01 = hls_to_rgb(h/360, l/100, s/100)
    rgb = tuple([int(i*255) for i in rgb_01])
    return rgb


def gen_css(palette, names):
    css = ""
    for i, color in enumerate(palette):
        css += f"@define-color color-{names[i]} rgb{hsl_to_rgb(color)};\n"
    return css


def gen_conf(palette, names):
    conf = ""
    for i, color in enumerate(palette):
        r, g, b = hsl_to_rgb(color)
        conf += f"$color-{names[i]} = rgb({r},{g},{b})\n"
    return conf


c1 = (356, 89, 22) # forte
c2 = (0, 28, 12) # background
c3 = (19, 50, 28) # secundario
c4 = (6, 100, 83) # claro
c5 = (6, 58, 86) # font
names = ("forte", "backg", "secun", "activ", "font")

deltas = tuple(calculate_deltas(c1, ci) for ci in [c2, c3, c4, c5])

base_color = (170, 89, 22) # 170, 356

palette = gen_palette_hsl(base_color, deltas)

with open("palette.css", "w") as f:
    f.write(gen_css(palette, names))

with open("hypr/myColors_2.conf", "w") as f:
    f.write(gen_conf(palette, names))


def prueba(palette):
    css = ":root {\n"
    for i, color in enumerate(palette):
        css += f"color: hsl{color};\n"
    css += "\n"
    for i, color in enumerate(palette):
        css += f"color: rgb{hsl_to_rgb(color)};\n"
    css += "}"
    with open("prueba.css", "w") as f:
        f.write(css)

#prueba(palette)