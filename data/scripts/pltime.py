import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_time(df, path='datavisualization'):

    os.makedirs(path, exist_ok=True)

    # Visual padrão grande
    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")
    sns.set_context("poster")

    figsize = (12, 12)
    line_width = 3
    font_size = 24

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        bnb_df = df[(df['slv_type'] == 'bnb') & (df['size'] == size)].sort_values(by='n')
        sns.lineplot(x='n', y='time', data=bnb_df, marker='o', linewidth=line_width)
        plt.title(f'Tempo de execução BnB - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Tempo de execução (ms)', fontsize=font_size)
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'bnb_time_{size}.png'))
        plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        greedy_df = df[(df['slv_type'] == 'greedy') & (df['size'] == size)].sort_values(by='n')
        sns.lineplot(x='n', y='time', data=greedy_df, marker='o', linewidth=line_width)
        plt.title(f'Tempo de execução Greedy - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Tempo de execução (ms)', fontsize=font_size)
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'greedy_time_{size}.png'))
        plt.close()

    fptas_df = df[df['slv_type'] == 'fptas']
    epss = fptas_df['eps'].unique()

    for eps in epss:
        for size in ['small', 'large']:
            plt.figure(figsize=figsize)
            eps_df = fptas_df[(fptas_df['eps'] == eps) & (fptas_df['size'] == size)].sort_values(by='n')
            sns.lineplot(x='n', y='time', data=eps_df, marker='o', linewidth=line_width)
            plt.title(f'Tempo de execução FPTAS (1 - {eps})-aproximativo - {size}', fontsize=font_size)
            plt.xlabel('n', fontsize=font_size)
            plt.ylabel('Tempo de execução (ms)', fontsize=font_size)
            plt.xticks(fontsize=font_size)
            plt.yticks(fontsize=font_size)
            plt.tight_layout()
            plt.savefig(os.path.join(path, f'fptas_{eps}_time_{size}.png'))
            plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        subset = fptas_df[fptas_df['size'] == size].sort_values(by='n')
        sns.lineplot(x='n', y='time', hue='eps', style='eps', data=subset, marker='o', linewidth=line_width)
        plt.title(f'Tempo de execução FPTAS - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Tempo de execução (ms)', fontsize=font_size)
        plt.legend(title='ε', fontsize=font_size - 4, title_fontsize=font_size - 2, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'fptas_comparison_{size}.png'))
        plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        for alg in df[df['size'] == size]['solver'].unique():
            subset = df[(df['solver'] == alg) & (df['size'] == size)].sort_values(by='n')
            plt.plot(subset['n'], subset['time'], marker='o', label=alg, linewidth=line_width)
        plt.title(f'Tempo de execução de todos os solvers - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Tempo de execução (ms)', fontsize=font_size)
        plt.legend(fontsize=font_size - 4, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.yscale('log')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'all_{size}.png'))
        plt.close()

