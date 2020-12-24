def clustering(**clu_cfg):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.cluster import OPTICS
    
    csv_path = clu_cfg['cluster']['csv_path']
    num_clusters = clu_cfg['cluster']['num_clusters'] 
    plot_title = clu_cfg['cluster']['plot_title']
    plot_xlabel = clu_cfg['cluster']['plot_xlabel']
    plot_ylabel = clu_cfg['cluster']['plot_ylabel']
    plot_marker = clu_cfg['cluster']['plot_marker']
    cluster_min_samples = clu_cfg['cluster']['cluster_min_samples']
    plot_path = clu_cfg['cluster']['plot_path']
    
    
    X = pd.read_csv(csv_path, header = None, sep = " ").set_index(0).loc[:, :2]
    
    clustering = OPTICS(min_samples = cluster_min_samples).fit(X)


    X.loc[:, 'label'] = clustering.labels_
    for lab in set(clustering.labels_):
        x, y = X.loc[X.label == lab, 1], X.loc[X.label == lab, 2]
        plt.scatter(x, y, marker = plot_marker)
    
    plt.title(plot_title)
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)
    
    plt.savefig(plot_path)