import shlex
import subprocess as sp

def merge_vcf(**cfg):
    lines = ''
    for k, v in cfg['bcftools'].items():
        if isinstance(v, list):
            line = k + ' ' + ' '.join(v)
        elif k == 'concat':
            line = k + ' ' + ' '.join(
                [v.replace('*', 'chr' + str(l)) for l in range(1, 23)]
            ) 
        else:
            line = k + ' ' + v
        lines += line + ' '
    cmd = "bcftools " + lines
    print(cmd)
    cmd_lst = shlex.split(cmd)
    proc = sp.call(cmd_lst)



def filter_vcf(**cfg):
    lines = ''
    for k, v in cfg['plink2'].items():
        if isinstance(v, list):
            line = k + ' ' + ' '.join(v)
        else:
            line = k + ' ' + v
        lines += line + ' '
    
    for idx in range(1, 23):
        s = 'chr' + str(idx)
        cmd = ("plink2 " + lines).replace('*', s)
#         print(cmd)
        cmd_lst = shlex.split(cmd)
        proc = sp.call(cmd_lst)



    

####### helper method for fastq2vcf ######
def fastq2bam(**cfg):
    cmd = cfg['fastq2bam']
    cmd_lst = shlex.split(cmd)
    proc = sp.Popen(cmd_lst, stdout=sp.PIPE, stderr=sp.PIPE)
        
        
def bam2vcf(**cfg):
    cmd = cfg['bam2vcf']
    cmd_lst = shlex.split(cmd)
    proc = sp.Popen(cmd_lst, stdout=sp.PIPE, stderr=sp.PIPE)
############ end of helper method ########

def fastq2vcf(**cfg):
    fastq2bam(**cfg)
    bam2vcf(**cfg)
    