variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for resources"
  type        = string
  default     = "oficina-fase2"
}

variable "database_name" {
  description = "Database name"
  type        = string
  default     = "oficina_fase1"
}

variable "db_username" {
  description = "Database username"
  type        = string
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

variable "sql_script_path" {
  description = "Path to the SQL script for initializing the database schema"
  type        = string
  default     = "../scripts/create_db_oficina.sql"  # Adjust if needed
}