from jinja2 import Environment, FileSystemLoader, TemplateNotFound, PackageLoader, select_autoescape
import os


def script(js_file):
    if 'http' in js_file:
        return '<script type="text/javascript" src="' + js_file + '"></script'
    static_folder = os.environ['STATIC_FILES']
    return '<script type="text/javascript" src="' + str(static_folder) + '/' + js_file + '"></script>'


def css(css_file):
    if 'http' in css_file:
        return '<link rel="stylesheet" href="' + css_file + '">'
    static_folder = os.environ['STATIC_FILES']
    return '<link rel="stylesheet" href="' + str(static_folder) + '/' + css_file + '">'


class TemplateRendering:

    def render_template(self, template_name, kwargs):
        template_dir = os.environ['TEMPLATE_FOLDER']

        env = Environment(loader=FileSystemLoader(template_dir))

        env.globals['css'] = css
        env.globals['script'] = script

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        content = template.render(kwargs)
        return content
