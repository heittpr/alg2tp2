import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_mem(df, path='datavisualization'):

    os.makedirs(path, exist_ok=True)
    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")
    figsize = (10, 10)

    df = df.sort_values(by='n')

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        bnb_df = df[(df['slv_type'] == 'bnb') & (df['size'] == size)]
        sns.lineplot(x='n', y='memory', data=bnb_df, marker='o')
        plt.title(f'Uso de memória BnB - {size}')
        plt.xlabel('n')
        plt.ylabel('Memória (KB)')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'bnb_mem_{size}.png'))
        plt.close()

        plt.figure(figsize=figsize)
        greedy_df = df[(df['slv_type'] == 'greedy') & (df['size'] == size)]
        sns.lineplot(x='n', y='memory', data=greedy_df, marker='o')
        plt.title(f'Uso de memória Greedy - {size}')
        plt.xlabel('n')
        plt.ylabel('Memória (KB)')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'greedy_mem_{size}.png'))
        plt.close()

    fptas_df = df[df['slv_type'] == 'fptas']
    epss = sorted(fptas_df['eps'].dropna().unique())

    for eps in epss:
        for size in ['small', 'large']:
            plt.figure(figsize=figsize)
            eps_df = fptas_df[(fptas_df['eps'] == eps) & (fptas_df['size'] == size)]
            sns.lineplot(x='n', y='memory', data=eps_df, marker='o')
            plt.title(f'Uso de memória FPTAS (1 - {eps}) - {size}')
            plt.xlabel('n')
            plt.ylabel('Memória (KB)')
            plt.tight_layout()
            plt.savefig(os.path.join(path, f'fptas_{eps}_mem_{size}.png'))
            plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        subset = fptas_df[fptas_df['size'] == size]
        sns.lineplot(x='n', y='memory', hue='eps', style='eps', data=subset, marker='o')
        plt.title(f'Uso de memória FPTAS - comparação ε - {size}')
        plt.xlabel('n')
        plt.ylabel('Memória (KB)')
        plt.legend(title='ε', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'fptas_eps_comparison_mem_{size}.png'))
        plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        for alg in df[df['size'] == size]['solver'].unique():
            subset = df[(df['solver'] == alg) & (df['size'] == size)]
            plt.plot(subset['n'], subset['memory'], marker='o', label=alg)
        plt.title(f'Uso de memória - todos os solvers - {size}')
        plt.xlabel('n')
        plt.ylabel('Memória (KB)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'all_mem_{size}.png'))
        plt.close()
