from django import template
import re

register = template.Library()

@register.filter(name='convert_to_latex')
def convert_to_latex(text):
    if re.search(r"\\\w+", text):
        return f"${text}$"
    else:
        text = text.replace("минус", "-")
        text = text.replace("умножить на", r" * ")
        text = text.replace("умножить", r" * ")
        text = text.replace("плюс", "+")
        text = text.replace("разделить", "/")
        text = text.replace("в степени", "^")
        text = text.replace(",", ".")
        text = text.replace("sin", r"\mathrm{sin}")
        text = text.replace("cos", r"\mathrm{cos}")
        text = text.replace("tan", r"\mathrm{tan}")
        text = text.replace("ctg", r"\mathrm{ctg}")
        text = text.replace("левая круглая скобка", "(")
        text = text.replace("правая круглая скобка", ")")
        text = re.sub(r"\\left\|(.*?)\\right\|", r"\\left|\\text{\1}\\right|", text)

        parts = re.split(r"([+\-*\/^()=<>]+|[0-9]+(?:[.][0-9]+)?)", text) 
        result = ""
        for part in parts:
            part = part.strip()
            if not part:
                continue

            if re.match(r"^[+\-*\/^()=<>]+|[0-9]+(?:[.][0-9]+)?$", part): 
                result += part  
            else:
                result += r"\text{" + part + r"}" 

        return f"${result}$"
