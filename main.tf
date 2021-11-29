
#################################################################################

# Here I have defined a Terraform resource to create a CNAME Record \
# for ElasticBeansTalk url.
# var.ENVIRONMENT_CNAME  is an envornment variable that has set \
# through gitlab Ci on the task Deplyoment

################################################################################
resource "aws_route53_record" "benz" {
  zone_id = data.aws_route53_zone.nasri.zone_id
  name    = "benz"
  type    = "CNAME"
  ttl     = "300"
  records = [var.ENVIRONMENT_CNAME]
}
