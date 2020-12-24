def pca_pruning(**proc_cfg):
    import shlex
    import subprocess as sp
    
    lines = ''
    for k, v in proc_cfg['pca_pruning'].items():
        line = k + ' ' + v
        lines += line + ' '
    cmd = 'plink2 ' + lines
    #####
    cmd_lst = shlex.split(cmd)
    proc = sp.call(cmd_lst)
    #####
    return proc

def pca_conduct(**proc_cfg):
    import shlex
    import subprocess as sp

    lines = ''
    for k, v in proc_cfg['pca_conduct'].items():
        line = k + ' ' + v
        lines += line + ' '
    cmd = 'plink2 ' + lines
    #####
    cmd_lst = shlex.split(cmd)
    proc = sp.call(cmd_lst)
    #####
    return proc

def plot_pca(**proc_cfg):
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    # will make it generic as development
    
    val_path = proc_cfg['plot']['val_path']
    vec_path = proc_cfg['plot']['vec_path']
    
    csv_path = proc_cfg['plot']['csv_path']
    plot_path = proc_cfg['plot']['plot_path']
    
    plot_title = proc_cfg['plot']['plot_title']
    plot_xlabel = proc_cfg['plot']['plot_xlabel']
    plot_ylabel = proc_cfg['plot']['plot_ylabel']
    plot_marker = proc_cfg['plot']['plot_marker']
    plot_color = proc_cfg['plot']['plot_color']
    
    vec = pd.read_csv(vec_path, header = None, sep = " ")
    val = pd.read_csv(val_path, header = None, sep = " ")
    vec = vec.loc[:, 1:].set_index(1)
    
    vec.to_csv(csv_path, header = None, sep = " ")
    
    plt.scatter(x = vec.loc[:, 2],
                y = vec.loc[:, 3], 
                color = plot_color, 
                marker = plot_marker)
    
    plt.title(plot_title)
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)
    
    plt.savefig(plot_path)
    
def process_data(**proc_cfg):
    pca_pruning(**proc_cfg);
    pca_conduct(**proc_cfg);
    # will need to take in/out path
    plot_pca(**proc_cfg);