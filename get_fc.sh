#!/bin/bash
cd /home/ubuntu/terraqi-backend-v2
conda activate base
/home/ubuntu/terraqi-backend-v2/venv/bin/python /home/ubuntu/terraqi-backend-v2/get_weatherfc.py
/home/ubuntu/terraqi-backend-v2/venv/bin/python /home/ubuntu/terraqi-backend-v2/convert_to_nc.py