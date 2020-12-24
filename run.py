#!/usr/bin/env python
import sys
sys.path.insert(0, 'src') # add library code to path

from etl import get_data
from pca import process_data
from pipeline import merge_vcf, filter_vcf
from cluster import clustering

import os
import json
import shutil

import shlex
import subprocess as sp


DATA_PARAMS = 'config/data-params.json'
TEST_PARAMS = 'config/test-params.json'

PIPELINE_PARAMS = 'config/pipeline.json'

PROCESS_PARAMS = 'config/process-params.json'

ENV_PARAMS = 'config/env.json'

def load_params(fp):
    with open(fp) as fh:
        param = json.load(fh)
    return param

def load_docker(docker_name):
    pre = 'launch-scipy-ml.sh -i'
    cmd = pre + ' ' + docker_name
    sp.call(shlex.split(cmd))
    return 'loading docker successfually'


def main(targets):
    if not os.path.exists('data'):
        os.mkdir('data')
        
    if not os.path.exists('out'):
        os.mkdir('out')
        
    if not os.path.exists('data/interim'):
        os.mkdir('data/interim')
    
    env_cfg = load_params(ENV_PARAMS)
    
    # starting the docker-image
#     load_docker(env_cfg['docker-image'])
    
    # make the clean target
    if 'clean' in targets:
        if 'interim' in targets:
            shutil.rmtree('data/interim', ignore_errors=True)
        if 'raw' in targets:
            shutil.rmtree('data/raw', ignore_errors=True)
        if 'test' in targets:
            shutil.rmtree('data/test', ignore_errors=True)
            
    #==================== get data chunk ====================
    # get data from ftp server if not in testing mode and the files not exist locally; load process para  
    if ('data' in targets) and ('test' not in targets):
        data_cfg = load_params(DATA_PARAMS)
        get_data(**data_cfg)
        
        pro_cfg = load_params(PROCESS_PARAMS)
        
    #==================== ingest data chunk ====================    
    # after loading raw data, execute data ingesting (fastq2bam/bam2vcf/merge-vcf/filter-vcf)
    if 'ingest' in targets:
        data_pipeline_cfg = load_params(PIPELINE_PARAMS)
        filter_vcf(**data_pipeline_cfg)
        merge_vcf(**data_pipeline_cfg)
    
    
    #==================== testing chunk 1 ====================
    # get data in test folder if in testing mode by changing file path in process config
    if 'data-test' in targets:
        test_cfg = load_params(TEST_PARAMS)
        
        pro_cfg = load_params(PROCESS_PARAMS)
        pro_cfg["pca_pruning"]['--vcf'] = test_cfg['filepath']
        pro_cfg["pca_conduct"]['--vcf'] = test_cfg['filepath']
        
        # in testing mode: specify the output path matches with what in env config
        pro_cfg["cluster"]['plot_path'] = env_cfg['output-paths']
    
    #==================== process chunk ====================
    if 'process' in targets:
        process_data(**pro_cfg)
        clustering(**pro_cfg)
        
    #==================== testing chunk 2 ====================
    if 'test-project' in targets:
        re = 'data-test process'
        main(re)
    # cleaning and analysis
    return


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
