from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from recibo_base import my_base_recibo


my_path = './'
my_file_path = f'{my_path}recibo_sueldo.pdf'

# Create a canvas
c = canvas.Canvas(
    my_file_path,
    pagesize=landscape(A4),
)

# Move the origin up and to the left
my_recibo_info = my_base_recibo(c)
c = my_recibo_info['canvas']

# Company name --------------------------------------------------------------------------------
# Original
current_y = my_recibo_info['company_info_y'] + my_recibo_info['company_info_height'] - 0.35 * cm
c.setFont("Helvetica-Bold", 10)
c.drawString(0.2 * cm, current_y, "Artime S.A.")
c.setFont("Helvetica", 10)
current_y -= 0.5 * cm
c.drawString(0.2 * cm, current_y, "Av. Rivadavia 1234, CABA")
current_y -= 0.5 * cm
c.drawString(0.2 * cm, current_y, "CUIT: 30-12345678-9")

# Duplicate_x
duplicate_x = my_recibo_info['duplicate_x'] + 0.2 * cm
current_y = my_recibo_info['company_info_y'] + my_recibo_info['company_info_height'] - 0.35 * cm
c.setFont("Helvetica-Bold", 10)
c.drawString(duplicate_x, current_y, "Artime S.A.")
c.setFont("Helvetica", 10)
current_y -= 0.5 * cm
c.drawString(duplicate_x, current_y, "Av. Rivadavia 1234, CABA")
current_y -= 0.5 * cm
c.drawString(duplicate_x, current_y, "CUIT: 30-12345678-9")


# Show and save
c.showPage()
c.save()
