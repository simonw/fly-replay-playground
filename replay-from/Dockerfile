# Start from the latest Golang base image
FROM golang:latest

# Add Maintainer Info
LABEL maintainer="Your Name <youremail@example.com>"

# Set the Current Working Directory inside the container
WORKDIR /app

# Here we write the Go file
RUN echo 'package main' > main.go
RUN echo '' >> main.go
RUN echo 'import ("net/http")' >> main.go
RUN echo '' >> main.go
RUN echo 'func main() {' >> main.go
RUN echo '	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {' >> main.go
RUN echo '		w.Header().Add("fly-replay", "app=replay-to")' >> main.go
RUN echo '		w.WriteHeader(http.StatusOK)' >> main.go
RUN echo '		w.Write([]byte(""))' >> main.go
RUN echo '	})' >> main.go
RUN echo '	http.ListenAndServe(":8080", nil)' >> main.go
RUN echo '}' >> main.go

# Build the Go app with GO111MODULE off
RUN GO111MODULE=off go build -o main .

# Expose port 8080 to the Docker host, so we can access it
# from the outside
EXPOSE 8080

# Command to run the executable
CMD ["./main"]
