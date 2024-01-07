from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


my_path = '/home/lugezz/Downloads/'
my_file_path = f'{my_path}report.pdf'
image_path = f'{my_path}download.png'

# Create a canvas
c = canvas.Canvas(
    my_file_path,
    pagesize=A4
)

# Move the origin up and to the left
c.translate(cm, cm)

# Fill some color and font
c.setFillColorRGB(0, 0, 255)
c.setFont("Helvetica", 30)

# Write some text
c.drawString(100, 750, "Hello Artime!")

# Draw some lines
c.line(100, 700, 500, 700)
c.line(100, 650, 500, 650)

# Last line with different color and width
c.setLineWidth(10)
c.setStrokeColorRGB(1, 0, 0)
c.line(100, 600, 500, 600)

# Draw a rectangle
# Arguments are: x1, y1, x2, y2, fill (1) or not (0)
# x1 and y1 are the bottom left corner
# x2 and y2 are the top right corner
c.setFillColorRGB(0, 100, 100)
c.rect(100, 100, 400, 400, fill=1)

# Write some text rotated inside the rectangle
c.rotate(45)
c.setFillColorRGB(255, 255, 255)
c.setFont("Helvetica", 80)
# Calculate adjusted coordinates for the rotated text inside the rectangle
text_x = 300  # Adjusted X-coordinate
text_y = 00  # Adjusted Y-coordinate
c.drawString(text_x, text_y, "Que tul!")
c.rotate(-45)

# Draw the image, and rotate it
c.rotate(-15)
c.drawImage(image_path, -0.8 * cm, 9 * cm, width=1.5 * cm, height=1.5 * cm)
c.rotate(15)

# Show and save
c.showPage()
c.save()
