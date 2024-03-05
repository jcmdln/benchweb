`benchweb` compares the performance of web frameworks I might use. For fun!

# Rules

0. All benchmarks should be reasonably fair
1. Serve on port `5150`
2. Route `/` must respond with `Hello, world!`

# Using

By default, make with build and benchmark everything:

```sh
make
```

The following example uses the default benchmarking values for Python frameworks:

```sh
make -C python/ bench DURATION=10s RATE=1000/s
```

# Results

See the [results](./results/) directory.
