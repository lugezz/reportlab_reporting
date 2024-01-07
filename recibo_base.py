from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas


def my_base_recibo(c: Canvas) -> dict:
    """ Base of payslip, it set all the lines and texts that are common to all payslips
    """
    tot_y = 21 * cm
    tot_x = 29.7 * cm
    half_of_width = tot_x / 2
    mid_margin = 0.7 * cm
    margin_between_lines = 0.2 * cm
    def_radius = 7

    resp = {
        'tot_y': tot_y,
        'tot_x': tot_x,
        'half_of_width': half_of_width,
        'mid_margin': mid_margin,
        'margin_between_lines': margin_between_lines,
    }

    # Aprox Margins
    # margin_x = 1.5 * cm
    margin_y = 1.2 * cm

    # Defining heights
    available_height = tot_y - 2 * margin_y
    company_name_height = available_height * 0.09 - margin_between_lines
    employee_info_height = available_height * 0.16 - margin_between_lines
    conceptos_height = available_height * 0.65 - margin_between_lines
    total_height = available_height * 0.1 - margin_between_lines

    c.translate(cm, cm)

    # Base Rectangles
    # Company Info --------------------------------------------------------------------------------
    gray_value = 0.93
    c.setFillColorRGB(gray_value, gray_value, gray_value)

    company_name_width = 9.65 * cm
    starting_y = tot_y - margin_y - company_name_height
    resp['company_info_y'] = starting_y
    resp['company_info_height'] = company_name_height
    resp['duplicate_x'] = half_of_width + mid_margin

    c.roundRect(0, starting_y, company_name_width, company_name_height, radius=def_radius, stroke=1, fill=1)
    c.roundRect(
        half_of_width + mid_margin,
        starting_y,
        company_name_width,
        company_name_height,
        radius=def_radius,
        stroke=1,
        fill=1
    )

    # Liquidacion Info --------------------------------------------------------------------------------
    original_x = company_name_width + 0.1 * cm
    duplicate_x = half_of_width + mid_margin + company_name_width + 0.1 * cm
    liquidacion_info_width = 3 * cm

    c.roundRect(original_x, starting_y, liquidacion_info_width, company_name_height, radius=def_radius, stroke=1, fill=0)
    c.roundRect(duplicate_x, starting_y, liquidacion_info_width, company_name_height, radius=def_radius, stroke=1, fill=0)
    # lines in the half
    c.line(
        original_x,
        starting_y + company_name_height / 2,
        original_x + liquidacion_info_width,
        starting_y + company_name_height / 2
    )
    c.line(
        duplicate_x,
        starting_y + company_name_height / 2,
        duplicate_x + liquidacion_info_width,
        starting_y + company_name_height / 2
    )

    # Employee Info --------------------------------------------------------------------------------
    starting_y -= employee_info_height + margin_between_lines
    employee_info_width = liquidacion_info_width + company_name_width + 0.1 * cm
    resp['employee_info_y'] = starting_y
    resp['employee_info_height'] = employee_info_height

    c.roundRect(0, starting_y, employee_info_width, employee_info_height, radius=def_radius, stroke=1, fill=0)
    c.roundRect(
        half_of_width + mid_margin,
        starting_y,
        employee_info_width,
        employee_info_height,
        radius=def_radius,
        stroke=1,
        fill=0
    )

    # Conceptos --------------------------------------------------------------------------------
    starting_y -= conceptos_height + margin_between_lines
    conceptos_width = employee_info_width
    resp['conceptos_y'] = starting_y
    resp['conceptos_height'] = conceptos_height

    c.roundRect(0, starting_y, conceptos_width, conceptos_height, radius=def_radius, stroke=1, fill=0)
    c.roundRect(half_of_width + mid_margin, starting_y, conceptos_width, conceptos_height, radius=def_radius, stroke=1, fill=0)

    # Linea para totales
    starting_y_totales = starting_y + conceptos_height * 0.15
    c.line(
        0,
        starting_y_totales,
        conceptos_width,
        starting_y_totales,
    )
    c.setFont("Helvetica-Bold", 10)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(0.5 * cm, starting_y_totales - 0.5 * cm, "Totales:")
    c.drawString(conceptos_width - 6 * cm, starting_y + 0.5 * cm, "Neto a Pagar:")

    c.line(
        half_of_width + mid_margin,
        starting_y_totales,
        half_of_width + mid_margin + conceptos_width,
        starting_y_totales,
    )
    c.drawString(half_of_width + mid_margin + 0.5 * cm, starting_y_totales - 0.5 * cm, "Totales:")
    c.drawString(half_of_width + mid_margin + conceptos_width - 6 * cm, starting_y + 0.5 * cm, "Neto a Pagar:")

    # Total --------------------------------------------------------------------------------
    # Original
    starting_y -= total_height + margin_between_lines + 0.3 * cm
    resp['total_y'] = starting_y

    firma_width = 5 * cm
    rect_width = total_height * 0.8

    c.roundRect(
        0,
        starting_y,
        conceptos_width,
        rect_width,
        radius=def_radius,
        stroke=1,
        fill=0
    )

    c.line(
        conceptos_width / 2,
        starting_y,
        conceptos_width / 2,
        starting_y + rect_width,
    )

    c.line(
        half_of_width / 2 - firma_width / 2 - 1 * cm,
        0,
        half_of_width / 2 + firma_width / 2 - 1 * cm,
        0,
    )
    c.setFont("Helvetica", 8)

    c.drawString(half_of_width / 2 - firma_width / 2, -0.5 * cm, "Firma del empleador")

    # Duplicate
    c.roundRect(
        half_of_width + mid_margin,
        starting_y,
        conceptos_width,
        rect_width,
        radius=def_radius,
        stroke=1,
        fill=0
    )

    c.line(
        half_of_width + mid_margin + conceptos_width / 2,
        starting_y,
        half_of_width + mid_margin + conceptos_width / 2,
        starting_y + rect_width,
    )

    c.line(
        half_of_width + mid_margin + 1 * cm,
        0,
        half_of_width + mid_margin + firma_width + 1 * cm,
        0,
    )
    c.drawString(half_of_width + mid_margin + 2 * cm, -0.5 * cm, "Firma del empleado")

    resp['canvas'] = c

    return resp
