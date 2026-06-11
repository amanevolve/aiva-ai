# Use the official, lightweight Nginx image
FROM nginx:alpine

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy our custom Nginx proxy configuration
COPY nginx.conf /etc/nginx/conf.d/

# Copy the Aiva interface into the Nginx web root directory
COPY index.html /usr/share/nginx/html/

# Expose port 80 to the Docker network
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
