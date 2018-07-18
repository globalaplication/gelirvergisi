
cizelge = {
    150000:25, 300000:30, 
    600000:35, 1200000:40
    }
def ondalik(tl, test=""):
    for en, nokta in enumerate(tl[::-1], 1):
        if en%3 is 0:
            test = test + nokta + str(".")
        else:
            test = test + nokta
    if test.endswith(".") is True:
        return test[::-1][1:]
    return test[::-1]
def vergial(geliri, yuzde=0):
    geliri = geliri.replace(".","")
    geliri = float(geliri)
    for test in cizelge:
        if geliri <= test :
            yuzde = cizelge[test]
            break
    if yuzde is 0:
        yuzde = 50
    return "vergi yuzdesi %{}, {} Tl vergi alinmali ".format(yuzde, 
    ondalik(str(geliri * yuzde /100)
    [0:-2]))

print (vergial("1.200.000"))



