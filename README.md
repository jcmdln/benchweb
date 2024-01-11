`benchweb` compares the performance of web frameworks I might use. For fun!

# Rules

0. All benchmarks should be reasonably fair
1. Serve on port `5150`
2. Route `/` must respond with `Hello, world!`

# Using

```sh
# Prepare every framework
make build

# Clear terminal
clear

# Benchmark frameworks
make bench
```

The following example uses the default benchmarking values:

```sh
make bench DURATION=10s RATE=1000/s
```

You may also run `make` from each subdirectory to collect benchmarks for a
specific language or individual frameworks.

# Results 2024/1/10

```
$ make bench
make[1]: Entering directory '/home/john/Projects/jcmdln/benchweb/go'
make[2]: Entering directory '/home/john/Projects/jcmdln/benchweb/go/fiber'
Requests      [total, rate]            10000, 1000.17
Duration      [total, attack, wait]    9.999504279s, 9.998335571s, 1.168708ms
Latencies     [mean, 50, 95, 99, max]  494.61µs, 161.184µs, 1.270499ms, 1.623909ms, 7.82572ms
Bytes In      [total, mean]            130000, 13.00
Bytes Out     [total, mean]            0, 0.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:10000
Error Set:
make[2]: Leaving directory '/home/john/Projects/jcmdln/benchweb/go/fiber'
make[2]: Entering directory '/home/john/Projects/jcmdln/benchweb/go/net-http'
Requests      [total, rate]            10000, 1000.11
Duration      [total, attack, wait]    9.999774263s, 9.998899431s, 874.832µs
Latencies     [mean, 50, 95, 99, max]  528.46µs, 153.486µs, 1.327011ms, 1.725306ms, 6.618315ms
Bytes In      [total, mean]            140000, 14.00
Bytes Out     [total, mean]            0, 0.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:10000
Error Set:
make[2]: Leaving directory '/home/john/Projects/jcmdln/benchweb/go/net-http'
make[1]: Leaving directory '/home/john/Projects/jcmdln/benchweb/go'
make[1]: Entering directory '/home/john/Projects/jcmdln/benchweb/python'
make[2]: Entering directory '/home/john/Projects/jcmdln/benchweb/python/blacksheep'
Requests      [total, rate]            10000, 1000.05
Duration      [total, attack, wait]    10.00212863s, 9.999476994s, 2.651636ms
Latencies     [mean, 50, 95, 99, max]  1.283217ms, 240.575µs, 3.208882ms, 4.0099ms, 7.329348ms
Bytes In      [total, mean]            130000, 13.00
Bytes Out     [total, mean]            0, 0.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:10000
Error Set:
make[2]: Leaving directory '/home/john/Projects/jcmdln/benchweb/python/blacksheep'
make[2]: Entering directory '/home/john/Projects/jcmdln/benchweb/python/fastapi'
Requests      [total, rate]            10000, 999.81
Duration      [total, attack, wait]    10.078052786s, 10.001866644s, 76.186142ms
Latencies     [mean, 50, 95, 99, max]  51.341452ms, 402.676µs, 190.204457ms, 350.98123ms, 486.932351ms
Bytes In      [total, mean]            150000, 15.00
Bytes Out     [total, mean]            0, 0.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:10000
Error Set:
make[2]: Leaving directory '/home/john/Projects/jcmdln/benchweb/python/fastapi'
make[1]: Leaving directory '/home/john/Projects/jcmdln/benchweb/python'
```
