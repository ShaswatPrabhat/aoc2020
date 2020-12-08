import re
import networkx as bubu_graph_package
import matplotlib.pyplot as noicely_plot


def solve_with_networkx():
    with open("input_real.txt", "r") as fp:
        data = fp.readlines()

    G = bubu_graph_package.DiGraph()

    for line in data:
        zuzu_entry = re.match(r"(.*) bags contain (.*)$", line)

        if zuzu_entry:
            color = zuzu_entry.group(1)
            remain = zuzu_entry.group(2)
            for child in re.findall(r"([\d]+) (.*?) bag", remain):
                G.add_edge(color, child[1], count=int(child[0]))

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    options = {
        'node_color': 'red',
        'edge_color': 'black',
        'node_size': 0.1,
        'width': 0.5,
    }
    noicely_plot.subplot(111)
    bubu_graph_package.draw_random(G, **options)
    noicely_plot.show()

    def count_bags_in(root):
        total_bags = 0
        for k, val in G[root].items():
            print('val', val, 'k', k)
            total_bags += val['count'] * count_bags_in(k) + val['count']

        return total_bags

    print(len(bubu_graph_package.ancestors(G, "shiny gold")))
    print(count_bags_in('shiny gold'))


if __name__ == '__main__':
    solve_with_networkx()
