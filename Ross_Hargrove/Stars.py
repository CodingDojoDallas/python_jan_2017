x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars (x):
    # Loop that iterates through the list
    for num in x:
        # Conditional that prints for a number
        if type(num) is int:
            print "*"*num
        # Conditional that prints for a string
        else:
            print num[0].lower()*len(num)


draw_stars(x)