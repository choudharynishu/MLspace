#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Packages to access AWS S3 bucket
import os
import boto3
import s3fs
from io import BytesIO

import sagemaker
from sagemaker import get_execution_role

#Packages to read the .bag files
import rosbag
import bagpy
from bagpy import bagreader

#Create roles to give learning and histing access to data
role = get_execution_role()
region = boto3.Session().region_name
sess = sagemaker.Session()


# S3 bucket where the original data is downloaded and stored.
downloaded_data_bucket = f"mlspace-data-981080730561"
downloaded_data_prefix = "global/datasets/TRBChallengeData"

#Load the dataset
s3 = boto3.client('s3')
s3.download_file(downloaded_data_bucket,f"{downloaded_data_prefix}/2023-11-03-12-37-20.bag","2023-11-03-12-37-20.bag")

with rosbag.Bag('2023-11-03-12-37-20.bag', 'r') as bag:
    # Iterate through the messages in the bag
    for topic, msg, t in bag.read_messages():
        # Process or print information about the message
            print(f"Topic: {topic}, Message: {msg}, Timestamp: {t.to_sec()}")
        # ... do something with the message content (msg)
bag.close()





