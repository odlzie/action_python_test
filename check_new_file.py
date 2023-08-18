import os
import glob

class get_input_file:
    def __init__(self, input_dir):
        self.latest_csv = self.get_latest_csv_file(input_dir)

    def get_latest_csv_file(self, input_dir):
        if os.path.isdir(input_dir):
            latest_file = max(glob.glob(os.path.join(input_dir, '*.csv')), key=os.path.getctime)

            if latest_file is None:
                raise ValueError('no csv file in input dir')
        else:
            raise FileNotFoundError

    def write_to_env(self):
        env_file = os.getenv('GITHUB_ENV')
        with open(env_file, "a") as f:
            f.write("my_csv={}".format(self.latest_csv))

        print(os.getenv('GITHUB_ENV'))

if __name__ == "__main__":
    # my_class = get_input_file('./data/input')
    # my_class.write_to_env()

    env_file = os.getenv('GITHUB_ENV')
    with open(env_file, "a") as myfile:
        myfile.write("MY_VAR={}".format(12))