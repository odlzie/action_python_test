import os
import glob

class get_input_file:
    def __init__(self, input_dir):
        self.latest_csv = self.get_latest_csv_file(input_dir)

    def get_latest_csv_file(self, input_dir):
        if os.path.isdir(input_dir):
            try:
                latest_file = max(glob.glob(os.path.join(input_dir, '*.csv')), key=os.path.getctime)
            except:
                raise ValueError('No csv file in input directory.')
        else:
            raise FileNotFoundError
        return latest_file


    def write_to_env(self):
        print(self.latest_csv)
        env_file = os.getenv('GITHUB_ENV')
        with open(env_file, "a") as myfile:
            myfile.write("my_csv={}".format(self.latest_csv))

if __name__ == "__main__":
    my_class = get_input_file('./data/input')
    my_class.write_to_env()
