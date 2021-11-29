# Continous Integeration And Deployment 

CI and CD is a must in modern application architecture and by far most appropriate aproach is implementing DevOps culture in your organization. Basically DevOps engineers or mindset is used to automate every manual task as much as possible as most of the time mistakes happen by human erorr, so If automation is in place then we will see less error in our environment. 

# DevOps Roadmap

One of the popular approach to achive maximum automation in place is using DevOps methodologies.
Here in this repo I have setup a continous deployment of a simple python application into aws ElasticBeanstalk.
Automation part includes Gitlab-ci, Docker, ElasticBeansTalk , Terraform and Route53. 

These are the most important files in the repository that Iam going to explain each by one. 

1. Gitlab and Gitlab-ci.yml
2. Docker and Dockerfile
3. ElasticBeansTalk and Dockerrun.aws.json 
4. Terraform and main.tf 
5. python and app.py



## Gitlab-ci.yml

It is used as main CI/CD definition file which consists of 5 tasks to create aws services, dockerize application, deployment and finally a cname record in Route53 and then big bang. 

## Dockerfile

From Docker standardization and using python image for python application and then pushing the image into my dockerhub which is nasri. 

## Dockerrun.aws.json 

Using Elasticbeanstalk to deploy images on AWS needs task definition it's pretty stright forward by reading the file you can grasp it. it is am easy json format.  
if you are working on local environment you need to install eb cli and set aws credentials. 

## Terraform 

With Terraform, it is easy to add or remove resources on AWS, it is used to create a cname record for ElasticBeansTalk endpoint to my personal domain , benz.nasri.it

## Python application

The application uses some external api to get some resources such as name , email , avatar and renders an html file regarding this porpuse. 





