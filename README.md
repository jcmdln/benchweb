`benchweb` compares the performance of web frameworks I might use. For fun!

# Rules

0. All benchmarks should be reasonably fair
1. Serve on port `5150`
2. Route `/` must respond with `Hello, world!`

# Using

Install `go-wrk`:

```sh
go install github.com/tsliwowicz/go-wrk@latest
```

By default, make with build and benchmark everything:

```sh
make
```

You may also benchmark a specific language:

```sh
make -C python/ bench
```

Or benchmark a specific framework:

```sh
make -C python/litestar-uvicorn bench
```

# Results

See the [results](./results/) directory.
