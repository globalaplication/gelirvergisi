
cizelge = {
150.00:25, 
300.00:30, 
600.00:35, 
900.00:45
}
def vergial(geliri, yuzde=0):
    for test in cizelge:
        if geliri <= test :
            yuzde = cizelge[test]
            break
    return "vergi yuzdesi %{}, {} Tl vergi alinmali ".format(yuzde, 
    geliri * yuzde /100)

print (vergial(149.00))
