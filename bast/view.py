from jinja2 import Environment, FileSystemLoader, TemplateNotFound, PackageLoader, select_autoescape
import os


class TemplateRendering:
    def render_template(self, template_name, kwargs):
        # template_dir = []
        # if self.settings.get('template_path', ''):
        #     template_dir.append(self.settings["template_path"])
        template_dir = os.environ['TEMPLATE_FOLDER']

        # app_name = app.config['APP_NAME']
        app_name = os.environ['APP_NAME']
        # env = Environment(loader=PackageLoader('bast', 'public'), autoescape=select_autoescape(['html']))
        env = Environment(loader=FileSystemLoader(template_dir))
        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        content = template.render(kwargs)
        return content
