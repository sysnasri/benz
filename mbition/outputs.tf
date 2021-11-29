
#############################################################################

# My domain name which is hosted on AWS Route 53 
# look at ENVIRONMENT_CNAME variable definition, in terraform TF_VAR_VARIABLE is a shell env variable \
# that you can fetch and put it as terraform variable, I used this in main.tf

#############################################################################

data "aws_route53_zone" "nasri" {
  name = "nasri.it."
}
variable "ENVIRONMENT_CNAME" {
  type        = string
  description = "This is an example input variable using env variables."
}
