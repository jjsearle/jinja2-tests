import os
import sys
from jinja2 import Environment, FileSystemLoader


class Template:
    def __init__(self, template_file=None,
                 output_directory=os.path.dirname(os.path.realpath(__file__))):
        self.template_file = template_file
        self.output_directory = output_directory
        self.output_filename = self.template_file.replace('.j2', '')

    def render(self):
        try:
            file_loader = FileSystemLoader(self.output_directory)
            env = Environment(loader=file_loader)
            t = env.get_template(self.template_file)
            print(f"Loaded template ({self.template_file})")
        except Exception as ex:
            print(f"ERROR: Failed to load template ({self.template_file})")
            print(f"{ex}")
            sys.exit(1)
        try:
            output = t.render(env=os.environ)
            f = open(f"{self.output_directory}/{self.output_filename}", "w+")
            f.write(output)
            f.close()
            print(f"Rendered template ({self.template_file})" +
                  " to {self.output_directory}/{self.output_filename}")
        except Exception as ex:
            print(f"ERROR: Failed to render template ({self.template_file})" +
                  " to {self.output_directory}/{self.output_filename}")
            print(f"{ex}")
            sys.exit(1)


standard_templates = ["test1.conf.j2", "test2.conf.j2"]

for template in standard_templates:
    t = Template(template_file=template)
    t.render()
