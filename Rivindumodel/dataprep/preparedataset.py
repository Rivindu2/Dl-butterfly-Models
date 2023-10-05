import os
import pandas as pd
import shutil


# this code will arrange the train dataset to 75 folders and each image will be added to the folder basd on their label

dataset_path = '/Users/rivindu/Desktop/datasetfor-butterfly/train'
csv_path = '/Users/rivindu/Desktop/datasetfor-butterfly/Training_set.csv'
output_path = '/Users/rivindu/Desktop/DL-A1/Dl-butterfly-Models/Rivindumodel/datset'

if not os.path.exists(output_path):
    os.makedirs(output_path)


df = pd.read_csv(csv_path)


unique_labels = df['label'].unique()#identify all unuqie 75 classes
for label in unique_labels:
    label_folder = os.path.join(output_path, label)
    os.makedirs(label_folder, exist_ok=True)
    image_filenames = df[df['label'] == label]['filename'].tolist()
    

    for filename in image_filenames:
        src_path = os.path.join(dataset_path, filename)
        dst_path = os.path.join(label_folder, filename)
        shutil.copy(src_path, dst_path)
        
print("Done check dir")
