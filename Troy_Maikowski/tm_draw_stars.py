a = [4,6,1,3,5,7,25]
b = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


#part I and part II
def draw_stars(arr):
    for num in arr:
        if type(num) is int:
            print "*"*num
        elif type(num) is str:
            print num[0].lower() * len(num)
        
draw_stars(a)
draw_stars(b)