# src/cli.py
import click
import yaml
from flask import current_app
from app import app  # ensure app is loaded with all blueprints

@app.cli.command('export-openapi')
def export_openapi():
    """Export the OpenAPI spec to docs/openapi.yaml"""
    with app.app_context():
        spec = app.blueprints['api'].api.__schema__
        with open('docs/openapi.yaml', 'w') as f:
            yaml.dump(spec, f)
        click.echo("✅ OpenAPI spec exported to docs/openapi.yaml")

