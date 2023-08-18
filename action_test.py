import pandas as pd
import os
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

class data_format:
    def __init__(self, input_file):
        self.df_input = self.get_input_data(input_file)

    def get_input_data(self, input_file):
        if os.path.isfile(input_file):
            df_input = pd.read_csv(input_file)
            logger.info('input file read')
        else:
            logger.error('input file not exist')
            raise
        return df_input

    def get_output_data(self):
        df = self.df_input.groupby(['Country'], as_index=False).agg({'Number of employees': sum})
        logger.info('output generated')
        return df

    def write_output_data(self):
        df = self.get_output_data()
        print(df.head(10))
        df.to_csv('./data/output/test.csv', index=False)

if __name__ == '__main__':
    # df = pd.read_csv('./data/input/organizations-100.csv')
    # print(df.head(10))
    # #print('testsss')

    my_class = data_format('./data/input/organizations-100.csv')
    my_class.write_output_data()
