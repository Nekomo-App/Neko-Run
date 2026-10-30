# Neko Run as a tiny static web server: docker run -p 8080:80 ghcr.io/nekomo-app/neko-run
FROM nginx:1.27-alpine
LABEL org.opencontainers.image.source="https://github.com/Nekomo-App/Neko-Run" \
      org.opencontainers.image.description="Neko Run - pixel cat runner game by the Nekomo community, served by nginx" \
      org.opencontainers.image.title="Neko Run"
COPY web/ /usr/share/nginx/html/
RUN rm -f /usr/share/nginx/html/package.json
EXPOSE 80
