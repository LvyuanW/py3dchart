from py3dchart import chart3d

# isinstance
chart1 = chart3d()

# set a[] as the data
# set b[] as the label
a = [5, 3, 1]
b = ['q', 'w', 'e']

# text font-size
chart1.fontSize(12)

# chart location:
# (x1,y1) is of the left top;
# (x2,y2) is of the right bottom.
# the orignal point(0,0) is on the left top coner of canvas
chart1.x1(50), chart1.y1(50)
chart1.x2(300), chart1.y2(300)

# draw pie chart
chart1.drawPie(a, b)

