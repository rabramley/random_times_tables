from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


def create_pdf():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    template_vars = {
        "tables": [4, 6, 8, 9],
        "order" : range(1, 13)
    }

    html = template.render(template_vars)

    HTML(string=html, base_url='.').write_pdf('/output/times_tables.pdf')

create_pdf()