import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
import os

plt.switch_backend('TkAgg')  # Use normal window backend

# Function to create a knowledge graph

def create_knowledge_graph_from_table(file_path):
    df = pd.read_csv(file_path)

    num_regions = df.shape[1] - 1
    outer_region_names = list(df.columns[1:])
    num_nodes = df.shape[0]

    # Define a colormap for nodes and outer regions
    node_cmap = plt.get_cmap('tab10')
    outer_cmap = plt.get_cmap('Set2')

    output_folder = input("Enter the path to save the PNG files: ")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    def plot_graph(active_node_idx=None, filename='knowledge_graph.png'):
        fig, ax = plt.subplots(figsize=(24, 8))
        ax.set_xlim(-14.0, -6.0)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')

        angles = np.linspace(0, 2 * np.pi, num_regions, endpoint=False)
        outer_positions = [(np.cos(angle) - 10.0, np.sin(angle)) for angle in angles]

        outer_region_colors = {}
        for idx, (x, y) in enumerate(outer_positions):
            color = outer_cmap(idx % 8)
            outer_region_colors[outer_region_names[idx]] = color
            ax.plot(x, y, 'o', markersize=20, color=color)

        if num_nodes == 1:
            inner_positions = [(-10.0, 0)]
        else:
            inner_angles = np.linspace(0, 2 * np.pi, num_nodes, endpoint=False)
            inner_positions = [(-10.0 + 0.5 * np.cos(a), 0.5 * np.sin(a)) for a in inner_angles]

        node_colors = {}

        for node_idx, row in df.iterrows():
            node_name = row.iloc[0]
            connections = row.iloc[1:]
            x_node, y_node = inner_positions[node_idx]
            color = node_cmap(node_idx % 10)
            node_colors[node_name] = color
            ax.plot(x_node, y_node, 'o', markersize=10, color=color)

            if active_node_idx is None or node_idx == active_node_idx:
                for region_idx, strength in enumerate(connections):
                    if strength > 0:
                        x_outer, y_outer = outer_positions[region_idx]
                        edge_cmap = plt.get_cmap('viridis')
                        edge_color = edge_cmap(strength / connections.max())
                        ax.plot([x_node, x_outer], [y_node, y_outer],
                                linewidth=strength / 2, color=edge_color, alpha=0.8)

        from matplotlib.lines import Line2D

        node_legend_elements = [Line2D([0], [0], marker='o', color='w', label=node,
                                       markerfacecolor=color, markersize=20)
                                for node, color in node_colors.items()]

        outer_legend_elements = [Line2D([0], [0], marker='o', color='w', label=region,
                                       markerfacecolor=color, markersize=20)
                                 for region, color in outer_region_colors.items()]

        first_legend = ax.legend(handles=node_legend_elements, loc='center left', bbox_to_anchor=(0.7, 0.7), fontsize=14, title="Nodes", title_fontsize=16)
        ax.add_artist(first_legend)
        second_legend = ax.legend(handles=outer_legend_elements, loc='center left', bbox_to_anchor=(0.7, 0.3), fontsize=14, title="Outer Regions", title_fontsize=16)

        plt.title("Knowledge Graph", fontsize=16)
        plt.tight_layout()
        full_path = os.path.join(output_folder, filename)
        plt.savefig(full_path, dpi=300)
        plt.close()

    # Plot individual node graphs
    for idx in range(num_nodes):
        node_name = df.iloc[idx, 0]
        filename = f'knowledge_graph_{idx+1:02d}_{node_name}.png'
        plot_graph(active_node_idx=idx, filename=filename)

    # Plot composite graph
    plot_graph(active_node_idx=None, filename=f'knowledge_graph_{num_nodes+1:02d}_composite.png')

# Run the function
if __name__ == "__main__":
    file_path = input("Enter the path to your CSV file: ")
    create_knowledge_graph_from_table(file_path)