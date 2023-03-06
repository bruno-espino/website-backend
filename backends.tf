terraform {
  backend "s3" {
    bucket = "website-state"
    key    = "website.tfstate"
    region = "us-east-1"
  }
}