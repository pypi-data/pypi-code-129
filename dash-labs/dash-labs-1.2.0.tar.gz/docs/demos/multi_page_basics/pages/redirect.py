from dash_labs.plugins import register_page
from dash import html


register_page(
    __name__,
    description="Welcome to my app",
    redirect_from=["/old-home-page", "/v2"],
    extra_template_stuff="yup",
)

layout = html.Div(["Home Page", html.Img(src="/assets/birds.jpeg", height="50px")])
