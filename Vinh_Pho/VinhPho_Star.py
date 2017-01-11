def draw_star(num,letter):
    if letter == 0:
        for i in range(0,num):
            print "*",
        print ""
    else:
        for i in range(0,num):
            print letter,
        print ""
    
def main1():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

    length=0
    #empty=""
    for i in range(0,len(x)):
        if type(x[i]) == type(str()):
    #        print "{} - It is a string".format(x[i])
            length=len(x[i])
            fletter=x[i][0:1].lower()
            print "{} {}".format(length,fletter)
            draw_star(length,fletter)
        else:
            draw_star(x[i],0)
        
main1()