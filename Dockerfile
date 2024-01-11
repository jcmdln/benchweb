FROM fedora:39
COPY . /benchweb
WORKDIR /benchweb

RUN dnf -y install make

# Go
RUN dnf -y install golang
RUN go install github.com/tsenart/vegeta@latest

# Python
RUN dnf -y install http-parser-devel libuv-devel pipx python-devel
RUN pipx install pdm
