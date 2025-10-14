provider "aws" {
  region = var.aws_region
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket = "soap-fiap-teste"
    key    = "infra-trab2/terraform.tfstate"
    region = "us-east-1"
  }
}
