import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_sumv(df, path='datavisualization'):
    os.makedirs(path, exist_ok=True)

    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")
    sns.set_context("poster")

    figsize = (12, 12)
    line_width = 3
    font_size = 24

    fptas_df = df[(df['slv_type'] == 'fptas') & (df['eps'] == 0.25) & (df['size'] == 'small')]
    fptas_df = fptas_df.sort_values(by='sumv')

    plt.figure(figsize=figsize)
    sns.lineplot(x='sumv', y='time', data=fptas_df, marker='o', linewidth=line_width)
    plt.yscale('log')
    plt.title('Tempo de execução FPTAS (ε = 0.25) pela soma dos valores (small)', fontsize=font_size)
    plt.xlabel('Soma dos valores dos itens (sumv)', fontsize=font_size)
    plt.ylabel('Tempo de execução (μs)', fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.tight_layout()
    plt.savefig(os.path.join(path, 'fptas_eps_025_time_vs_sumv_small.png'))
    plt.close()
