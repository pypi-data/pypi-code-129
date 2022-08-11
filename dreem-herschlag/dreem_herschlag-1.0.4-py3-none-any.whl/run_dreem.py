import subprocess

class Run_dreem(object):
    def __init__(self, config) -> None:
        self.samples = config['samples']
        self.files_per_sample = config['files_per_sample']
        self.path_to_data = config['path_to_data']
        self.sample_file = 'temp/samples.csv'
        self.dreem_args = config['dreem_args']
        self.verbose = config['verbose']

    def run_command(cmd):
        output, error_msg = None, None
        try:
            output = subprocess.check_output(
                    cmd, shell=True, stderr=subprocess.STDOUT
            ).decode("utf8")
        except subprocess.CalledProcessError as exc:
            error_msg = exc.output.decode("utf8")
        return output, error_msg

    def run(self):
        if self.verbose: print(f"Running DREEM")
        for s in self.samples:
            cmd = 'dreem'
            for fast_arg, fast_file in zip(['-fq1','-fq2','-fa'],self.files_per_sample[:3]):
                cmd += ' '+fast_arg+' '+self.path_to_data+f"{s}/"+fast_file

            cmd += ' --sample '+s
            cmd += ' --sample_info '+self.sample_file
            cmd += ' --library_info '+'temp/'+f"{s}/library.csv"

            for key, val in self.dreem_args.items():
                if (not (type(val) == bool)) or val:
                    cmd += ' --'+ key + ' '+ (str(val) if type(val) != bool else '')

            if self.verbose: print(cmd)
            [print(out) for out in self.run_command(cmd)] if self.verbose else self.run_command(cmd)
        if self.verbose: print('DREEM done\n')