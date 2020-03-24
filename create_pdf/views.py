from django.shortcuts import render
from django.http import HttpResponse
from fpdf import FPDF, HTMLMixin


def index(request):
	return render(request,"index.html")

def demo(request):
    from fpdf import FPDF
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Welcome to Python!", align="C")
    pdf.output("Somefilename.pdf")
    return render(request,"index.html")

def change_fonts(request):
	pdf=FPDF()
	pdf.add_page()
	font_size=8
	for font in pdf.core_fonts:
		if any ([letter for letter in font if letter.isupper()]):
			continue
		pdf.set_font(font, size=font_size)
		txt="Font name:{} - {} pts".format(font, font_size)
		pdf.cell(0,10, txt=txt, ln=1, align="C")
		font_size+=2
	pdf.output("change_fonts.pdf")
	return render(request,"index.html")

if __name__ == '__main__':
	change_fonts()


def draw_lines(request):
    pdf = FPDF()
    pdf.add_page()
    pdf.line(10, 10, 10, 100)
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)
    pdf.line(20, 20, 100, 20)
    pdf.output('draw_lines.pdf')
    return render(request,"index.html")
    
if __name__ == '__main__':
    draw_lines()


def draw_shapes(request):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(255, 0, 0)
    pdf.ellipse(10, 10, 10, 100, 'F')
    
    pdf.set_line_width(1)
    pdf.set_fill_color(0, 255, 0)
    pdf.rect(20, 20, 100, 50)
    pdf.output('draw_shapes.pdf')
    return HttpResponse('<h1>Pdf created successfully</h1>')
    
if __name__ == '__main__':
    draw_shapes()


def add_image(request, image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=8, w=100)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)  # move 85 down
    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
    pdf.output("add_image.pdf")
    return render(request,"index.html")
if __name__ == '__main__':
    add_image('snakehead.jpg')


def multipage_simple(request):
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
    line_no = 1
    for i in range(100):
        pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
        line_no += 1
    pdf.output("multipage_simple.pdf")
    return render(request,"index.html")
    
if __name__ == '__main__':
    multipage_simple()


class CustomPDF(FPDF):
    
    def header(self):
        # Set up a logo
        #self.image('snakehead.jpg', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        
        # Add an address
        self.cell(100)
        self.cell(0, 5, 'Mike Driscoll', ln=1)
        self.cell(100)
        self.cell(0, 5, '123 American Way', ln=1)
        self.cell(100)
        self.cell(0, 5, 'Any Town, USA', ln=1)
        
        # Line break
        self.ln(20)
        
    def footer(self):
        self.set_y(-10)
        
        self.set_font('Arial', 'I', 8)
        
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')
        
def create_pdf(request):
    pdf = CustomPDF()
    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    line_no = 1
    for i in range(50):
        pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
        line_no += 1
    pdf.output('header_footer.pdf')
    return render(request,"index.html")
    
if __name__ == '__main__':
    create_pdf('header_footer.pdf')



def simple_table(request,spacing=1):
    data = [['First Name', 'Last Name', 'email', 'zip'],
            ['Mike', 'Driscoll', 'mike@somewhere.com', '55555'],
            ['John', 'Doe', 'jdoe@doe.com', '12345'],
            ['Nina', 'Ma', 'inane@where.com', '54321']
            ]
    
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
    
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)
        
    pdf.output('simple_table.pdf')
    return render(request,"index.html")
    
if __name__ == '__main__':
    simple_table()



class HTML2PDF(FPDF, HTMLMixin):
    pass
def simple_table_html(request):
    pdf = HTML2PDF()
    
    table = """<table border="0" align="center" width="50%">
    <thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
    <tbody>
    <tr><td>cell 1</td><td>cell 2</td></tr>
    <tr><td>cell 2</td><td>cell 3</td></tr>
    </tbody>
    </table>"""
    
    pdf.add_page()
    pdf.write_html(table)
    pdf.output('simple_table_html.pdf')
    return render(request,"index.html")
    
if __name__ == '__main__':
    simple_table_html()


class HTML2PDF(FPDF, HTMLMixin):
    pass
def html2pdf(request):
    html = '''<h1 align="center">PyFPDF HTML Demo</h1>
    <p>This is regular text</p>
    <p>You can also <b>bold</b>, <i>italicize</i> or <u>underline</u></p>
    '''
    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)
    pdf.output('html2pdf.pdf')
    return render(request,"index.html")
    
if __name__ == '__main__':
    html2pdf()

