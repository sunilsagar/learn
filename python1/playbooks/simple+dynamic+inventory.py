#!/bin/python
import sys
import json
import pprint
try:
   import boto3
  # print("Successfully imported boto3")
except ImportError:
   print("Please install boto3 using pip2 install boto3 or pip install boto3 and try again")
   sys.exit(1)
except Exception as e:
   print(e)
   sys.exit(2)
def get_hosts(ec2,f_value):
   f={"Name":"tag:Env", "Values":[f_value]}
   hosts=[]
   for each_in in ec2.instances.filter(Filters=[f]):
    #  print(each_in.private_ip_address)
    hosts.append(each_in.private_ip_address)
   return hosts
def main():
   ec2=boto3.resource("ec2","us-east-1")
   db_group=get_hosts(ec2,"db")
   app_group=get_hosts(ec2,"app")
   all_groups= { 'db': db_group,
                  'app': app_group
               }
   print(json.dumps(all_groups))

if __name__=="__main__":
   main()
