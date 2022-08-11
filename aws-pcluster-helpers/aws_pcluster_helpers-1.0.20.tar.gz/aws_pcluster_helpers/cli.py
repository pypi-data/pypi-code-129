import os

import rich_click as click
from rich_click import RichCommand, RichGroup

from aws_pcluster_helpers.commands import cli_sinfo
from aws_pcluster_helpers.commands import cli_gen_nxf_slurm_config
from aws_pcluster_helpers.commands import cli_build_ami


@click.group()
def cli():
    """
    Helper functions for aws parallelcluster.
    """
    return


@cli.command()
def sinfo():
    """
    A more helpful sinfo
    """
    click.echo("Printing sinfo table")
    cli_sinfo.main()


@cli.command()
@click.option("--output", "-o", help="Output path", required=False)
@click.option("--overwrite", is_flag=True, help="Overwrite local files")
@click.option("--stdout", is_flag=True, help="Write slurm config to stdout")
def gen_nxf_slurm_config(output: str, overwrite: bool, stdout: bool):
    """
    Generate a slurm.config for nextflow that is compatible with your cluster.

    You will see a process label for each partition/node type.

    Use the configuration in your process by setting the label to match the label in the config.
    """
    click.echo("Generating NXF Slurm config")
    cli_gen_nxf_slurm_config.main(output, overwrite, stdout)


@click.option('--output', help="Path to output pcluster describe-image", required=True,
              default=os.environ.get('PCLUSTER_BUILD_AMI_FILE'))
@click.option('--region', help="Aws region to query", required=False, default=os.environ.get('AWS_DEFAULT_REGION'))
@click.option("--image-id", help="Ami build ID", required=True, default=os.environ.get('PCLUSTER_BUILD_AMI_ID'))
def build_ami(output, region, image_id):
    click.echo("PCluster image builder watcher")
    cli_build_ami.main(image_id=image_id, output_file=output, region=region)


if __name__ == "__main__":
    cli()
