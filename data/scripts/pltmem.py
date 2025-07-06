import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_mem(df, path='datavisualization'):

    os.makedirs(path, exist_ok=True)

    # Configuração visual para fontes grandes
    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")
    sns.set_context("poster")  # maior contexto visual

    figsize = (12, 12)
    line_width = 3
    font_size = 24  # Fonte bem maior

    df = df.sort_values(by='n')

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        bnb_df = df[(df['slv_type'] == 'bnb') & (df['size'] == size)]
        sns.lineplot(x='n', y='memory', data=bnb_df, marker='o', linewidth=line_width)
        plt.title(f'Uso de memória BnB - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Memória (KB)', fontsize=font_size)
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'bnb_mem_{size}.png'))
        plt.close()

        plt.figure(figsize=figsize)
        greedy_df = df[(df['slv_type'] == 'greedy') & (df['size'] == size)]
        sns.lineplot(x='n', y='memory', data=greedy_df, marker='o', linewidth=line_width)
        plt.title(f'Uso de memória Greedy - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Memória (KB)', fontsize=font_size)
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'greedy_mem_{size}.png'))
        plt.close()

    fptas_df = df[df['slv_type'] == 'fptas']
    epss = sorted(fptas_df['eps'].dropna().unique())

    for eps in epss:
        for size in ['small', 'large']:
            plt.figure(figsize=figsize)
            eps_df = fptas_df[(fptas_df['eps'] == eps) & (fptas_df['size'] == size)]
            sns.lineplot(x='n', y='memory', data=eps_df, marker='o', linewidth=line_width)
            plt.title(f'Uso de memória FPTAS (1 - {eps}) - {size}', fontsize=font_size)
            plt.xlabel('n', fontsize=font_size)
            plt.ylabel('Memória (KB)', fontsize=font_size)
            plt.xticks(fontsize=font_size)
            plt.yticks(fontsize=font_size)
            plt.tight_layout()
            plt.savefig(os.path.join(path, f'fptas_{eps}_mem_{size}.png'))
            plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        subset = fptas_df[fptas_df['size'] == size]
        sns.lineplot(x='n', y='memory', hue='eps', style='eps', data=subset, marker='o', linewidth=line_width)
        plt.title(f'Uso de memória FPTAS - comparação ε - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Memória (KB)', fontsize=font_size)
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.legend(title='ε', fontsize=font_size - 4, title_fontsize=font_size - 2, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'fptas_eps_comparison_mem_{size}.png'))
        plt.close()

    for size in ['small', 'large']:
        plt.figure(figsize=figsize)
        for alg in df[df['size'] == size]['solver'].unique():
            subset = df[(df['solver'] == alg) & (df['size'] == size)]
            plt.plot(subset['n'], subset['memory'], marker='o', label=alg, linewidth=line_width)
        plt.title(f'Uso de memória - todos os solvers - {size}', fontsize=font_size)
        plt.xlabel('n', fontsize=font_size)
        plt.ylabel('Memória (KB)', fontsize=font_size)
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.legend(fontsize=font_size - 4, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'all_mem_{size}.png'))
        plt.close()

