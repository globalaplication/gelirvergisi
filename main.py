
cizelge = {
    150.000:25, 300.000:30, 
    600.000:35, 1200.000:40
    }

def vergial(geliri, yuzde=0):
    for test in cizelge:
        if geliri <= test :
            yuzde = cizelge[test]
            break
    if yuzde is 0:
        yuzde = 50
    return "vergi yuzdesi %{}, {} Tl vergi alinmali ".format(yuzde, 
    geliri * yuzde /100)

print (vergial(1201.000))

