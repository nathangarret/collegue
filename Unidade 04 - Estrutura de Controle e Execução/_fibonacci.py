def fibonnaci(x):
    previous = 1
    current = 1

    while current <= x:
        previous, current = current, previous + current # Atribuições simultânes
    return current

print(fibonnaci(13))