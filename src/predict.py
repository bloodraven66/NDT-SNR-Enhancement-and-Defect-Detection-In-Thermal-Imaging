from utils import load_data



if __name__ == '__main__':
    load_data = Load_data()
    cell_data = Load_data(name='data.mat', mat_key='data', file_path='../../NDTPhase2/data/')
    print(cell_data.shape)
