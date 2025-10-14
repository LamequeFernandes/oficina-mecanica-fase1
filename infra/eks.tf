module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "21.3.2"        # ✅ Adicione esta linha
  cluster_name    = "oficina-cluster"
  cluster_version = "1.30"
  subnets         = module.vpc.private_subnets
  vpc_id          = module.vpc.vpc_id

  eks_managed_node_groups = {
    default = {
      desired_capacity = 2
      max_capacity     = 4
      min_capacity     = 1

      instance_types = ["t3.micro"]
    }
  }

  tags = {
    Environment = "dev"
    Project     = "Oficina"
  }
}
