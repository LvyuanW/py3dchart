for install package: pip install py3dchart
import: from py3dchart import chart3d

isinstance: chart1 = chart3d()

set a[] as the data: a = [5, 3, 1]
set b[] as the label: b = ['q', 'w', 'e']

set text font-size: chart1.fontSize(12)

set chart location:

(x1,y1) is of the left top: chart1.x1(50), chart1.y1(50)
(x2,y2) is of the right bottom: chart1.x2(300), chart1.y2(300)

and the orignal point(0,0) is on the left top coner of canvas

draw pie chart: chart1.drawPie(a, b)
