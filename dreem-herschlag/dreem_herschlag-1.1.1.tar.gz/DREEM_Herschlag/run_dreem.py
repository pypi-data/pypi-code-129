from DREEM_Herschlag.util import run_command
from DREEM_Herschlag.sanity_check import Sanity_check


class Run_dreem(object):
    def __init__(self, config) -> None:
        self.samples = config['samples']
        self.path_to_data = config['path_to_data']
        self.sample_file = 'temp/samples.csv'
        self.library_file = 'temp/library.csv'
        self.dreem_args = config['dreem_args']
        self.verbose = config['verbose']
        self.fastq_zipped = config['fastq_zipped']
        self.fasta_file = Sanity_check(config).find_fasta()

    def run(self):
        if self.verbose: print(f"Running DREEM")
        for s in self.samples:
            cmd = 'dreem'
            for fast_arg, fast_file in zip(['-fq1','-fq2'],[x + '.gz' if self.fastq_zipped else x for x in ['_R1_001.fastq', '_R2_001.fastq']]):
                cmd += ' '+fast_arg+' '+self.path_to_data+s+fast_file

            cmd += ' -fa '+self.fasta_file
            cmd += ' --sample '+s
            cmd += ' --sample_info '+self.sample_file
            cmd += ' --library_info '+self.library_file

            for key, val in self.dreem_args.items():
                if (not (type(val) == bool)) or val:
                    cmd += ' --'+ key + ' '+ (str(val) if type(val) != bool else '')

            if self.verbose: print(cmd)
            [print(out) for out in run_command(cmd)] if self.verbose else self._run_command(cmd)
        if self.verbose: print('DREEM done\n')