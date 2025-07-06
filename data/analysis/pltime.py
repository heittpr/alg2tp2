import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_time(df, path='datavisualization'):
    """
    serao gerados 7 graficos,
    graficos individuais para os algoritmos
    2 graficos comparativos para eps e todos
    """

    os.makedirs(path,exist_ok=True)
    plt.style.use('seaborn')
    sns.set_palette("husl")
    figsize=(10,10)

    plt.figure(figsize=figsize)
    bnb_df = df[df['slv_type'] == 'bnb']
    sns.scatterplot(x='n', y='time', data=bnb_df)
    plt.title('Tempo de execução por número de itens - Branch-and-bound')
    plt.xlabel('n')
    plt.ylabel('Tempo de execução (ms)')
    plt.savefig(os.path.join(path, 'bnb_time.png'))
    plt.close()

    greedy_df=df[df['slv_type']=='greedy']
    sns.scatterplot(x='n', y='time', data=greedy_df)
    plt.title('Tempo de execução por número de itens - Algoritmo 2-aproximativo')
    plt.xlabel('n')
    plt.ylabel('Tempo de execução (ms)')
    plt.savefig(os.path.join(path, 'greedy_time.png'))
    plt.close()

    fptas_df=df[df['slv_type']=='fptas']
    epss=fptas_df['eps'].unique()

    for eps in epss:
        plt.figure(figsize=figsize)
        eps_df=fptas_df[fptas_df['eps']==eps]
        sns.scatterplot(x='n',y='time',data=eps_df)
        plt.title(f'Tempo de execução por número de itens - FPTAS ε={eps}')
        plt.xlabel('n')
        plt.ylabel('Tempo de execução (ms)')
        plt.savefig(os.path.join(path, f'fptas_{eps}_time.png'))
        plt.close()
       
    plt.figure(figsize=figsize)
    sns.scatterplot(x='n', y='time', hue='eps', style='eps', data=fptas_df)
    plt.title('Tempo de execução por número de itens - Diferentes valores de ε em FPTAS')
    plt.xlabel('n')
    plt.ylabel('Tempo de execução (ms)')
    plt.legend(title='ε')
    plt.savefig(os.path.join(path, 'fptas_comparison.png'))
    plt.close()

    for alg in df['solver'].unique():
        subset = df[df['solver'] == alg]
        plt.scatter(subset['n'], subset['time'], label=alg)
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.yscale('log')
    plt.title('Tempo de execução por número de itens - Todos os solvers')
    plt.savefig(f'{path}/all.png')
    plt.close()
