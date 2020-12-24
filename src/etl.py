import os

def get_vcf(chromosome, ftp, out_path):
    '''
    chromosome: list of chromosomes needed eg.
    ftp: ftp ojject from the parent func
    '''
    ### chr*
    ### TODO: clean chromosome format
    VCF_SITE = 'vol1/ftp/release/20130502'
    CHR_IDX = 1
    VCF_EXT = '.vcf.gz'
    VCF_IDX = - len(VCF_EXT)
    
    ftp.cwd(VCF_SITE)
    all_files = ftp.nlst()
    # chr* is at the 2nd index place
    # only keep .vcf.gz
    vcf_files = [i for i in all_files if (i[VCF_IDX:] == VCF_EXT)\
                 and (i.split('.')[CHR_IDX] in chromosome)]
     
    out_path = os.path.join(out_path, 'vcf')
    if not (os.path.exists(out_path)):
        os.mkdir(out_path)
    
    donwload(vcf_files, ftp, out_path)
    
    return vcf_files

def get_bam(sample, ftp, out_path):
    '''
    sample: list of samples eg. HG00096
    chromosome: list of chromosomes needed 
    ftp: ftp ojject from the parent func
    '''
    ### chrom*
    BAM_EXT = '.bam'
    BAM_IDX = -len(BAM_EXT)
    ftp.cwd('vol1/ftp/phase3/data')
#     print(ftp.nlst())
    out = []
    for sam in sample:
        BAM_SITE = '%s/alignment' % sam
        
        ftp.cwd(BAM_SITE)
        all_files = ftp.nlst()
        bam_files = [i for i in all_files if (i[BAM_IDX:] == BAM_EXT)]
        
        out_path = os.path.join(out_path, 'bam')
        if not (os.path.exists(out_path)):
            os.mkdir(out_path)
        
        donwload(bam_files, ftp, out_path)
        
        out += bam_files
        ftp.cwd('../../')
        
    return out

def get_fastq(sample, ftp, out_path):
    '''
    ### NO CRHOMOSOME FORMAT
    sample: list of samples eg. HG00096
    chromosome: list of chromosomes needed
    ftp: ftp ojject from the parent func
    '''
    FASTQ_EXT = '.fastq.gz'
    FASTQ_IDX = - len(FASTQ_EXT)
    ftp.cwd('vol1/ftp/phase3/data/')
#     print(ftp.nlst())
    out = []
    for sam in sample:
        FASTQ_SITE = '%s/sequence_read' % sam
        ftp.cwd(FASTQ_SITE)
        all_files = ftp.nlst()
        fastq_files = [i for i in all_files if (i[FASTQ_IDX:] == FASTQ_EXT)]
        
        out_path = os.path.join(out_path, 'fastq')
        if not (os.path.exists(out_path)):
            os.mkdir(out_path)
        donwload(fastq_files, ftp, out_path)
        
        out += fastq_files
        ftp.cwd('../../')
    
    return out


def get_data_list(sample, chromosome, file_format, out_path):
    '''
    file_format either be VCF/BAM/FASTQ
    '''
    SITE = 'ftp.1000genomes.ebi.ac.uk'

    ftp = FTP(SITE)
    ftp.login()
    for i in file_format:
        if 'VCF' == i:
            yield get_vcf(chromosome, ftp, out_path)
            ftp.cwd('../../../../')
            
        elif 'BAM' == i:
            ### TODO determine sample
            yield get_bam(sample, ftp, out_path)
            ftp.cwd('../../../../')

        elif 'FASTQ' == i:
            ### TODO determine sample
            yield get_fastq(sample, ftp, out_path)
            ftp.cwd('../../../../')
            
#     get_data_list(sample, chromosome, file_format, out_path)
    
    ftp.quit()
    ftp.close()


def donwload(file_lst, ftp, out_path):
    '''
    use this funcs at the lst dir
    '''
    for file in file_lst:
        write_path = os.path.join(out_path, file)
        if os.path.exists(write_path):
            print('aready exists' + file)
            continue
        print('downloading %s' % file)
        ftp.retrbinary('RETR %s' % file, open(write_path, 'wb').write)
        print('finish downloading %s' % file)
#     ftp.cwd('../../')

def get_data(**cfg):
    '''
    reads in the desired data in data-params.json 
    and uses the configuration to download all the tables
    cfg = json.load(open('data-params.json'))
    '''
    
    sample = cfg['sample']
    chrom = cfg['chromosome']
    file_type = cfg['format']
    ###########
    out_path = os.path.join('', cfg['outpath'])
    
    if not (os.path.exists(out_path)):
        os.mkdir(out_path)
        os.mkdir('data/interim')
    return get_data_list(sample, chrom, file_type, out_path)



    