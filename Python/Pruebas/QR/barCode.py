import barcode
from barcode.writer import ImageWriter
data = "TSwxMDUwLDEsMjItMDEtMjAyMCwwMToyMjo1NC4="
data1 = str(data)
a = barcode.get_barcode_class('code128')
b = a(data, writer = ImageWriter())
c = b.save('barcode')