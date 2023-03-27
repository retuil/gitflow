for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= (not (y <= z))) or w) == 0:
                    print(f'{x}   {y}   {z}   {w}')
