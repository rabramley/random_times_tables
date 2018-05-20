import random
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


def create_pdf():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    numbers = list(range(2, 13))
    random.shuffle(numbers)

    template_vars = {
        "tables": list(range(2,13)),
        "order" : numbers
    }

    html = template.render(template_vars)

    HTML(string=html, base_url='.').write_pdf('./output/times_tables.pdf')

create_pdf()