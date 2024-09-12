# Stage 1: Build the React application
FROM node:lts-alpine AS builder

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React application
RUN npm run build

# Stage 2: Serve the built application
FROM node:lts-alpine

# Set the environment variable for production
ENV NODE_ENV=production

# Set the working directory
WORKDIR /usr/src/app

# Copy only the build output from the previous stage
COPY --from=builder /usr/src/app/build ./build

# Install a simple HTTP server to serve the static files
RUN npm install -g serve

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["serve", "-s", "build", "-l", "3000"]