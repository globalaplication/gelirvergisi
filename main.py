
cizelge = {
    150000:25, 300000:30, 
    600000:35, 1200000:40
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

print (vergial(600000))
