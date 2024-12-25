# Результаты тестирования с помощью wrk

- Отдача статического документа напрямую через nginx

  wrk -c 100 -d 10s -t 4 http://localhost:80/static/js/index.js   
Running 10s test @ http://localhost:80/static/js/index.js
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    29.37ms   61.21ms 964.97ms   97.66%
    Req/Sec     1.16k   102.60     1.77k    87.50%
  46102 requests in 10.03s, 20.97MB read
Requests/sec:   4596.84
Transfer/sec:      2.09MB
---
- Отдача статического документа напрямую через gunicorn

  wrk -c 100 -d 10s -t 4 http://localhost:8081/static/js/index.js
Running 10s test @ http://localhost:8081/static/js/index.js
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   148.21ms  156.15ms   1.93s    96.42%
    Req/Sec   182.42     48.43   430.00     80.95%
  7282 requests in 10.05s, 31.97MB read
  Socket errors: connect 0, read 0, write 0, timeout 26
  Non-2xx or 3xx responses: 7282
Requests/sec:    724.86
Transfer/sec:      3.18MB
---
- Отдача динамического документа напрямую через gunicorn

  wrk -c 100 -d 10s -t 4 http://localhost:8081/       
Running 10s test @ http://localhost:8081/
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us     nan%
    Req/Sec     0.00      0.00     0.00    100.00%
  6 requests in 10.04s, 2.32MB read
  Socket errors: connect 0, read 0, write 0, timeout 6
Requests/sec:      0.60
Transfer/sec:    236.48KB
---
- Отдача динамического документа через проксирование запроса с nginx на gunicorn

    wrk -c 100 -d 10s -t 4 http://localhost:80/  
Running 10s test @ http://localhost/
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.43s   432.33ms   1.97s    60.00%
    Req/Sec     2.23      3.01    10.00     90.32%
  32 requests in 10.10s, 6.05MB read
  Socket errors: connect 0, read 0, write 0, timeout 22
  Non-2xx or 3xx responses: 32
Requests/sec:      3.17
Transfer/sec:    613.27KB
---
- Отдача динамического документа через проксирование запроса с nginx на gunicorn, при кэшировние ответа на nginx (proxy cache)

    wrk -c 100 -d 10s -t 4 http://localhost:80/       
Running 10s test @ http://localhost:80/
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    68.32ms  201.14ms   1.99s    92.65%
    Req/Sec     1.14k   375.84     2.89k    78.45%
  2976 requests in 10.02s, 1.31GB read
  Socket errors: connect 0, read 0, write 0, timeout 27
Requests/sec:   4101.23
Transfer/sec:    153.51MB
---
## Вывод

При отдаче статических документов nginx превосходит gunicorn по скорости примерно в 5 раз.
При отдаче динамики без кэшрования nginx не дает преимущества, но при включенном кэшировании ускоряет отдачу страниц в 18 раз.
