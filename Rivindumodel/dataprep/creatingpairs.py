import csv
import os
import pandas as pd
import random
import shutil

# this file will create positiv and negative pairs 
# meaning it will create pairs of images that belong in the same class (positive pairs)
# and create pais of images that dont belong in the same class (negative pai r)


#load image labels
labels = pd.read_csv("/Users/rivindu/Desktop/datasetfor-butterfly/Training_set.csv")
#get image list in traiing dir
image_dir = "/Users/rivindu/Desktop/datasetfor-butterfly/train"
image_list = os.listdir(image_dir)

#dictonary to map labels to image filess
label_dict = {row['filename']: row['label'] for index, row in labels.iterrows()}

#create +ive & -ive pairs
def create_pairs(image_list, label_dict):
    pairs = []
    labels = []
    for image_file in image_list:
        print(image_file)
        current_label = label_dict.get(image_file)
        if current_label is not None:
            positive_image = random.choice([f for f in image_list if label_dict.get(f) == current_label])#get random image from current class for positive image
            negative_image = random.choice([f for f in image_list if label_dict.get(f) != current_label])#get another random image that is not from urrent class for negative image
            
            pairs.append((image_file, positive_image))
            labels.append(1)
            pairs.append((image_file, negative_image))
            labels.append(0)
    return pairs,labels

pairs, labels = create_pairs(image_list, label_dict)

#store pairs in local directory and information of pairs
positive_pairs_dir = "/Users/rivindu/Desktop/DL-A1/Dl-butterfly-Models/Rivindumodel/dataprep/datapairs/positive_pairs"
negative_pairs_dir = "/Users/rivindu/Desktop/DL-A1/Dl-butterfly-Models/Rivindumodel/dataprep/datapairs/negative_pairs"
pair_info_file = "/Users/rivindu/Desktop/DL-A1/Dl-butterfly-Models/Rivindumodel/dataprep/datapairs/pair_info.csv"


#create diretories if first time
os.makedirs(positive_pairs_dir, exist_ok=True)
os.makedirs(negative_pairs_dir, exist_ok=True)

# write data to the directories 
with open(pair_info_file, 'w', newline='') as csvfile:
    pair_info_writer = csv.writer(csvfile)
    pair_info_writer.writerow(["Image1", "Image2", "Label"])
    for i, (image1, image2) in enumerate(pairs):
        label = labels[i]
        print("label",label)

        if label == 1:
            pair_dir = positive_pairs_dir
        else:
            pair_dir = negative_pairs_dir

        image1_dst = os.path.join(pair_dir, f"pair_{i}_1.jpg")
        image2_dst = os.path.join(pair_dir, f"pair_{i}_2.jpg")
        
        shutil.copy(os.path.join(image_dir, image1), image1_dst)
        shutil.copy(os.path.join(image_dir, image2), image2_dst)
        
        pair_info_writer.writerow([image1_dst, image2_dst, label])



print("created pairs")