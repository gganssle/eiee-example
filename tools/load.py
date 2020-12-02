import pandas as pd 


class s3_load_csv(object):
  def __init__(self):
    pass 


  def load(self, bucket, path):
    data_location = f's3://{bucket}/{path}'

    df = pd.read_csv(data_location)

    return df

