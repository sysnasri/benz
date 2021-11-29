#############################################################################

# As I am using terraform in CI/CD, so it is a must to have remote state file. 
# I have created an s3 bucket for remote state for my project 

#############################################################################

terraform {
  backend "s3" {
    bucket         = "terraform-state-nasri-projects"
    key            = "terraform-state-key"
    region         = "us-east-1"
    dynamodb_table = "terraform-nasri-project-state"

  }
  required_providers {

    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.67.0"

    }
  }
}
