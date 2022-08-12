from pathlib import Path
import typer
from cityfront.generator import get_source, parse_openapi_spec, build_rest_api
from cityfront.generator.config import Config

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def build_api(source: Path):
    build_config = Config(
        rest_descrition_source="",
        webhook_schema_source="",
        class_overrides={},
        webhooks_output="",
        client_output="cityfront/rest",
        webhook_types_output="",
    )
    source = get_source(source)
    api_data = parse_openapi_spec(source, build_config)
    build_rest_api(api_data, build_config)


if __name__ == "__main__":
    app()
