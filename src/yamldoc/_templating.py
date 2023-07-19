from jinja2 import Environment, PackageLoader, select_autoescape

ENV: Environment = Environment(
    loader=PackageLoader("yamldoc"),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True,
)
