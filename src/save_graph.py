def save_graph(plot, directory, filename):
    
    '''
    Saves the given plot in the given directory as the given filename.

    Parameters:
    plot (pyplot figure): A pyplot plot to be saved.
    directory (string): A full path to the destination folder.
    filename (string): A name for the file being saved to, excluding file format.
    '''

    import matplotlib.pyplot as plt
    plt.savefig(directory + filename + '.png')
    plt.close(plot)

    print('Plot saved to', filename + '.png', 'in', directory)