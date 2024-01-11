FROM fedora:39
COPY . /benchweb
WORKDIR /benchweb
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
RUN dnf -y install make procps-ng tini tzdata
ENTRYPOINT ["/bin/tini", "--"]
CMD ["/bin/bash"]

# Go
RUN dnf -y install golang
RUN go install github.com/tsenart/vegeta@latest
ENV PATH="$PATH:/root/go/bin/"

# Python
RUN dnf -y install http-parser-devel libev-devel libuv-devel pipx python-devel
RUN pipx install pdm

# Rust
RUN dnf -y install cargo rust
