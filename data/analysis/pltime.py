import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_time(df, path='datavisualization'):
    """
    Serão gerados 14 gráficos:
    - Para cada algoritmo (bnb, greedy, fptas para cada ε, e comparação geral),
      um gráfico para testcases 'small' e outro para 'large'.
    """

    os.makedirs(path, exist_ok=True)
    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")
    figsize = (10, 10)

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        bnb_df = df[(df['slv_type'] == 'bnb') & (df['size'] == size)].sort_values(by='n')
        sns.lineplot(x='n', y='time', data=bnb_df, marker='o')
        plt.title(f'Tempo de execução BnB - {size}')
        plt.xlabel('n')
        plt.ylabel('Tempo de execução (ms)')
        plt.savefig(os.path.join(path, f'bnb_time_{size}.png'))
        plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        greedy_df = df[(df['slv_type'] == 'greedy') & (df['size'] == size)].sort_values(by='n')
        sns.lineplot(x='n', y='time', data=greedy_df, marker='o')
        plt.title(f'Tempo de execução Greedy - {size}')
        plt.xlabel('n')
        plt.ylabel('Tempo de execução (ms)')
        plt.savefig(os.path.join(path, f'greedy_time_{size}.png'))
        plt.close()

    fptas_df = df[df['slv_type'] == 'fptas']
    epss = fptas_df['eps'].unique()

    for eps in epss:
        for size in ['small', 'large']:
            plt.figure(figsize=figsize)
            eps_df = fptas_df[(fptas_df['eps'] == eps) & (fptas_df['size'] == size)].sort_values(by='n')
            sns.lineplot(x='n', y='time', data=eps_df, marker='o')
            plt.title(f'Tempo de execução FPTAS (1 - {eps})-aproximativo - {size}')
            plt.xlabel('n')
            plt.ylabel('Tempo de execução (ms)')
            plt.savefig(os.path.join(path, f'fptas_{eps}_time_{size}.png'))
            plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        subset = fptas_df[fptas_df['size'] == size].sort_values(by='n')
        sns.lineplot(x='n', y='time', hue='eps', style='eps', data=subset, marker='o')
        plt.title(f'Tempo de execução FPTAS - {size}')
        plt.xlabel('n')
        plt.ylabel('Tempo de execução (ms)')
        plt.legend(title='ε')
        plt.savefig(os.path.join(path, f'fptas_comparison_{size}.png'))
        plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        for alg in df[df['size'] == size]['solver'].unique():
            subset = df[(df['solver'] == alg) & (df['size'] == size)].sort_values(by='n')
            plt.plot(subset['n'], subset['time'], marker='o', label=alg)
        plt.legend(bbox_to_anchor=(1.05, 1))
        plt.yscale('log')
        plt.title(f'Tempo de execução de todos os solvers - {size}')
        plt.xlabel('n')
        plt.ylabel('Tempo de execução (ms)')
        plt.savefig(os.path.join(path, f'all_{size}.png'), bbox_inches='tight')
        plt.close()
