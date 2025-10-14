resource "aws_db_instance" "oficina_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  db_name              = "oficina_fase1"
  username             = "lameque"
  password             = var.db_password
  skip_final_snapshot  = true
  publicly_accessible  = false
  vpc_security_group_ids = [module.vpc.default_security_group_id]
}
