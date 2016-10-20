from Physics import force as f


def yoshida(n, h, config, x, y, px, py):

    B0 = 0.675603595979828813
    B1 = -0.175603595979828813
    D0 = 1.35120719195965763
    D1 = -1.70241438391931525

    x = config[0]
    y = config[0]
    px = config[0]
    py = config[0]

    for i in range(n):
        px[i] += B0 * h * f[i]
        x[i] += D0 * h * px[i]
        py[i] += B0 * h * f[i]
        x[i] += D0 * h * py[i]

    f.force()
    for i in range(n):
        px[i] += B0 * h * f[i]
        x[i] += D0 * h * px[i]
        py[i] += B0 * h * f[i]
        y[i] += D0 * h * py[i]

    f.force()
    for i in range(n):
        px[i] += B1 * h * f[i]
        x[i] += D0 * h * px[i]
        py[i] += B1 * h * f[i]
        y[i] += D0 * h * py[i]

    f.force()
    for i in range(n):
        px[i] += B0 * h * f[i]
        py[i] += B0 * h * f[i]

    config = [x, y, px, py]

    return config
