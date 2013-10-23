from jinja2.exceptions import TemplateNotFound, TemplateError
from webapp2_extras import jinja2
import webapp2

DEFAULT_PATH = "index.html"
NOT_FOUND_TEMPLATE = "404.html"
INTERNAL_ERROR_TEMPLATE = "500.html"


class PageHandler(webapp2.RequestHandler):
  def get(self, path):
    if path is None or len(path) == 0:
      path = DEFAULT_PATH
    self.render_template(path)

  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(app=self.app)

  def render_template(self, template_name, **template_args):
    try:
      html = self.jinja2.render_template(template_name,
                                         path=template_name,
                                         **template_args)
    except TemplateNotFound:
      self.response.status = 404
      html = self.jinja2.render_template(NOT_FOUND_TEMPLATE,
                                         path=template_name,
                                         **template_args)
    except TemplateError:
      self.response.status = 500
      html = self.jinja2.render_template(INTERNAL_ERROR_TEMPLATE,
                                         path=template_name,
                                         **template_args)

    self.response.write(html)