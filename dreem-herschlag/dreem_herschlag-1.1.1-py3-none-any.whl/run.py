from email.policy import default
import click
from click_option_group import optgroup
import yaml
from DREEM_Herschlag.sanity_check import Sanity_check
from DREEM_Herschlag.run_dreem import Run_dreem
import os

from DREEM_Herschlag.get_info import echo_attributes_samples, echo_attributes_library
from DREEM_Herschlag.templates import TemplateGenerator
from DREEM_Herschlag.util import generate_mh_only_folder

@click.command()
@optgroup.group("main arguments")
@optgroup.option("-c", "--config", type=click.Path(exists=True),
                 help="reference sequences in fasta format")

@optgroup.option("--samples_info", is_flag=True, help="Print the mandatory and optional columns for samples.csv")
@optgroup.option("--library_info", is_flag=True, help="Print the mandatory and optional columns for library.csv")
@optgroup.option("--generate_templates", default=None, help="Path to generate templates for samples.csv (in_vivo and in_vitro) and library.csv")

def main(**args):
    """
    DREEM processes DMS next generation sequencing data to produce mutational
    profiles that relate to DMS modification rates written by Silvi Rouskin and the
    Rouskin lab (https://www.rouskinlab.com/)
    """
    run(args)

def read_config(args):
    with open(args['config'], 'r') as f:
        config = yaml.safe_load(f)
    assert config['samples'], "No samples found in config file"
    assert config['path_to_data'], "No path_to_data found in config file"
    assert config['dreem_args'], "No dreem_args found in config file"
    assert config['verbose'] != None, "No verbose found in config file"
    assert config['mut_hist_only_folder'] != None, "No mut_hist_only_folder found in config file"
    assert config['fastq_zipped'] != None, "No fastq_zipped found in config file"
    return config

def make_dirs():
    for repo in ['temp', 'output','log','input']:
        if not os.path.exists(repo):
            os.makedirs(repo)

def run(args):
    if args['samples_info']:
        echo_attributes_samples()
    if args['library_info']:
        echo_attributes_library()
    if args['generate_templates'] != None:
        temp = TemplateGenerator(args['generate_templates']).run()
    if args['samples_info'] or args['library_info'] or args['generate_templates'] != None:
        exit()
    else:
        config = read_config(args)
        make_dirs()
        Sanity_check(config).run()
        Run_dreem(config).run()
        if config['mut_hist_only_folder']:
            generate_mh_only_folder(config['samples'])




if __name__ == "__main__":
    main()
