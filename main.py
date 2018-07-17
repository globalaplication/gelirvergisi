cizelge = {150.00:25, 
300.00:30, 
600.00:35, 900.00:45}
def vergial(geliri, yuzde = 0):
    for test in cizelge:
        if  test <= geliri:
            yuzde = cizelge[test]
    return geliri * yuzde / 100

print ("gelirinden {} Tl vergi alinmali ".format( vergial(200) ))
