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


# In[2]:


#Create roles to give learning and histing access to data
role = get_execution_role()
region = boto3.Session().region_name
sess = sagemaker.Session()


# In[3]:


# S3 bucket where the original data is downloaded and stored.
downloaded_data_bucket = f"mlspace-data-981080730561"
downloaded_data_prefix = "global/datasets/TRBChallengeData"


# In[4]:


get_ipython().run_cell_magic('time', '', '\n# Load the dataset\ns3 = boto3.client("s3")\ns3.download_file(downloaded_data_bucket, f"{downloaded_data_prefix}/2023-11-03-12-37-20.bag", "2023-11-03-12-37-20.bag")\n\nwith rosbag.Bag(\'2023-11-03-12-37-20.bag\', \'r\') as bag:\n    # Iterate through the messages in the bag\n    for topic, msg, t in bag.read_messages():\n        # Process or print information about the message\n        print(f"Topic: {topic}, Timestamp: {t.to_sec()}")\n        # ... do something with the message content (msg)\n')


# In[ ]:


s3 = s3fs.S3FileSystem()
s3_address = 's3://mlspace-data-981080730561/global/datasets/TRBChallengeData/2023-11-03-12-37-20.bag'

chunk_size=786432

bag = bagreader(s3.open(s3_address))
# Now you can iterate through the messages in the bag

for topic, msg, t in bag.read_messages():
    # Process each message as needed
    print(f"Topic: {topic}, Timestamp: {t}, Message: {msg}")

# Close the bag file
bag.close()


# In[ ]:


counter=0
# Open the bag file
with rosbag.Bag('2023-11-03-12-37-20.bag', 'r') as bag:
    # Iterate through the messages in the bag
    for topic, msg, t in bag.read_messages():
        counter+=1
        # Process or print information about the message
        if counter>=10:
            print(f"Topic: {topic}, Message: {msg}, Timestamp: {t.to_sec()}")
            print('*******************************************')
        elif counter>=15:
            break
        # ... do something with the message content (msg)
bag.close()


# In[ ]:




