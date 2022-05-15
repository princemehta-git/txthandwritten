import pywhatkit as pwt

r = '''
1) l1:l2:l3 = 8:12:16 = 2:3:4
since, diameter is constant so let take respective resistance as 2x,3x,4x
so, 1/equivalent resistance = 1/2x + 1/3x + 1/4x
equivalent resistance = 12x/13
voltage  = 78*12x/13 = 72x
since voltage is same in parallel comb.
so, current in the 1st branch = 72x/2x = 36amp
2nd branch = 72x/3x = 24amp
3rd branch = 72x/4x = 18amp

2) 1/equivalent resistance = 1/4 + 1/4  + 1/4
equivalent resistance = 4/3 
since voltage is same as in parallel connection
therefore, I1  = v/r1
so, I1 = I2 = I3 = 16/4 = 4amp.

'''
pwt.text_to_handwriting(r,'sample.png',[10,10,10])