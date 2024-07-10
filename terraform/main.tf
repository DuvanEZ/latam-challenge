# Provider configuration for Google Cloud Platform
provider "google" {
  credentials = file("../stalwart-yen-428319-q9-xxxxxxxx.json")  # Ruta al archivo JSON de la cuenta de servicio
  project     = var.project_id  # ID del proyecto para el proyecto de Google Cloud
  region      = var.region  # Región donde se crearán los recursos
}

# Recurso de instancia de Google Compute Engine
resource "google_compute_instance" "default" {
  name         = "docker-instance"  # Nombre de la instancia
  machine_type = "e2-medium"  # Tipo de máquina para la instancia
  zone         = "us-central1-a"  # Zona donde se creará la instancia

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"  # Imagen para el disco de arranque
    }
  }

  network_interface {
    network = "default"  # Red para la instancia
    access_config {}  # Usar configuración de acceso predeterminada
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo docker run -d -p 8080:80 de_challenge_completed # Ejecutar el contenedor Docker
  EOF
}