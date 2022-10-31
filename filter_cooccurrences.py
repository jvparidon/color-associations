import argparse
import pandas as pd
from itertools import chain

def get_terms():
    df = pd.read_csv('data/color_dimension_nameability.csv')
    colors = list(df['color'].unique())  #['white', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'black']
    dimensions = list(df['dimension'].unique())
    dimensions = [pair.split('-') for pair in dimensions]
    dimensions = list(chain(*dimensions))
    return colors, dimensions

def get_neighbors():
    df = pd.read_csv('data/neighbors_coca_fic.tsv', sep='\t')
    color_neighbors = list(chain(df.values.tolist()[:9]))
    dim_neighbors = list(chain(df.values.tolist()[9:]))
    return color_neighbors, dim_neighbors

def get_mediators():
    with open('data/names_2plus.txt', 'r') as txtfile:
        mediators = txtfile.read().split('\n')
    return mediators

def filter_cooccurrences(fname, colors, dimensions):
    colors = set(colors)
    dimensions = set(dimensions)
    with open(fname, 'r') as infile, open(fname.replace('.txt', '.no_1st_order.txt'), 'w') as outfile, open(fname.replace('.txt', '.1st_order.txt'), 'w') as filterfile:
        for line in infile:
            words = set(line.strip('\n').split(' '))
            if (colors & words) and (dimensions & words):
                filterfile.write(line)
            else:
                outfile.write(line)
                
def filter_neighbors_strong(fname, color_neighbors, dim_neighbors):
    neighbors = set(color_neighbors + dim_neighbors)
    with open(fname, 'r') as infile, open(fname.replace('.txt', '.no_neighbors_strong.txt'), 'w') as outfile, open(fname.replace('.txt', '.neighbors_strong.txt'), 'w') as filterfile:
        for line in infile:
            words = set(line.lower().strip('\n').split(' '))
            if neighbors & words:
                filterfile.write(line)
            else:
                outfile.write(line)

def filter_neighbors_weak(fname, colors, dimensions, color_neighbors, dim_neighbors):
    dim_neighbors = set(dim_neighbors)
    color_neighbors = set(color_neighbors)
    with open(fname, 'r') as infile, open(fname.replace('.txt', '.no_neighbors_weak.txt'), 'w') as outfile, open(fname.replace('.txt', '.neighbors_weak.txt'), 'w') as filterfile:
        for line in infile:
            words = set(line.lower().strip('\n').split(' '))
            if (colors & words):
                if (dimensions & words):
                    filterfile.write(line)
                elif (dim_neighbors & words):
                    filterfile.write(line)
                else:
                    outfile.write(line)
            elif (dimensions & words) and (color_neighbors & words):
                filterfile.write(line)
            else:
                outfile.write(line)
                
def filter_mediators(fname, mediators):
    mediators = set(mediators)
    with open(fname, 'r') as infile, open(fname.replace('.txt', '.no_mediators.txt'), 'w') as outfile, open(fname.replace('.txt', '.mediators.txt'), 'w') as filterfile:
        for line in infile:
            words = set(line.lower().strip('\n').split(' '))
            if mediators & words:
                filterfile.write(line)
            else:
                outfile.write(line)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('fname')
    args = argparser.parse_args()

    colors, dimensions = get_terms()
    #filter_cooccurrences(args.fname, colors, dimensions)
    
    color_neighbors, dim_neighbors = get_neighbors()
    filter_neighbors_strong(args.fname, color_neighbors, dim_neighbors)
    filter_neighbors_weak(args.fname, colors, dimensions, color_neighbors, dim_neighbors)
    
    #mediators = get_mediators()
    #filter_mediators(args.fname, mediators)
