# tienda-api-docker

API de la tienda en FastAPI. GitHub Actions ejecuta las pruebas con pytest y publica la imagen de Docker en GitHub Container Registry.

```bash
docker pull ghcr.io/zavalauriel/tienda-api-docker:latest
docker run -d --name tienda-ghcr -p 8000:8000 ghcr.io/zavalauriel/tienda-api-docker:latest
curl "http://localhost:8000/precio?precio=200&descuento=25"
```
