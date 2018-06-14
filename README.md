# python-sync-vs-async
small example of why async is awesome for I/O stuff

You can think of this example as of some clients that requires a bunch of bytes from a remote service in chunks.
On every response client wait for data to come (sleep), run scripts to see the difference.

```
~/async_http  python sync_gen.py
Function 2 took 0.13342881202697754 seconds to finish
Function 3 took 0.13491129875183105 seconds to finish
Function 4 took 0.13185381889343262 seconds to finish
Function 5 took 0.375408411026001 seconds to finish
Function 6 took 0.13223648071289062 seconds to finish
Function 7 took 0.4342970848083496 seconds to finish
Function 8 took 0.31465673446655273 seconds to finish
Function 9 took 0.4354069232940674 seconds to finish
Function 10 took 0.49793195724487305 seconds to finish
Function 11 took 0.31534528732299805 seconds to finish
Function 12 took 0.2556459903717041 seconds to finish
Function 13 took 0.4971799850463867 seconds to finish
Function 14 took 0.31535911560058594 seconds to finish
Function 15 took 0.19452571868896484 seconds to finish
Function 16 took 0.5562665462493896 seconds to finish
Function 17 took 0.2555668354034424 seconds to finish
Function 18 took 0.19436025619506836 seconds to finish
Function 19 took 0.1949329376220703 seconds to finish
Function 20 took 0.07349371910095215 seconds to finish
Function 21 took 0.13525009155273438 seconds to finish
Function 22 took 0.19378900527954102 seconds to finish
Function 23 took 0.07050633430480957 seconds to finish
Function 24 took 0.13436245918273926 seconds to finish
Function 25 took 0.49422383308410645 seconds to finish
Function 26 took 0.19501304626464844 seconds to finish
Function 27 took 0.3756718635559082 seconds to finish
Function 28 took 0.4360160827636719 seconds to finish
Function 29 took 0.13433623313903809 seconds to finish
Function 30 took 0.13284087181091309 seconds to finish
Function 31 took 0.2550656795501709 seconds to finish
Function 32 took 0.0731515884399414 seconds to finish
Function 33 took 0.1960904598236084 seconds to finish
Function 34 took 0.07231450080871582 seconds to finish
Function 35 took 0.25351524353027344 seconds to finish
Function 36 took 0.314469575881958 seconds to finish
Function 37 took 0.4365570545196533 seconds to finish
Function 38 took 0.4947175979614258 seconds to finish
Function 39 took 0.37513208389282227 seconds to finish
Function 40 took 0.07152485847473145 seconds to finish
Function 41 took 0.315687894821167 seconds to finish
Function 42 took 0.4355466365814209 seconds to finish
Function 43 took 0.3732151985168457 seconds to finish
Function 44 took 0.13531017303466797 seconds to finish
Function 45 took 0.3752095699310303 seconds to finish
Function 46 took 0.5552749633789062 seconds to finish
Function 47 took 0.1351790428161621 seconds to finish
Function 48 took 0.3734118938446045 seconds to finish
Function 49 took 0.1920332908630371 seconds to finish
Total time: 13.182665348052979

~/async_http  python async_gen.py
Coroutine 14 took 0.10511159896850586 seconds to finish
Coroutine 15 took 0.10515332221984863 seconds to finish
Coroutine 24 took 0.1050102710723877 seconds to finish
Coroutine 33 took 0.10491037368774414 seconds to finish
Coroutine 34 took 0.10492062568664551 seconds to finish
Coroutine 39 took 0.10487484931945801 seconds to finish
Coroutine 45 took 0.10481834411621094 seconds to finish
Coroutine 5 took 0.1726381778717041 seconds to finish
Coroutine 7 took 0.17268633842468262 seconds to finish
Coroutine 12 took 0.1726822853088379 seconds to finish
Coroutine 13 took 0.17270803451538086 seconds to finish
Coroutine 22 took 0.17501449584960938 seconds to finish
Coroutine 40 took 0.17479896545410156 seconds to finish
Coroutine 47 took 0.17474651336669922 seconds to finish
Coroutine 49 took 0.17475128173828125 seconds to finish
Coroutine 2 took 0.21510815620422363 seconds to finish
Coroutine 3 took 0.2151472568511963 seconds to finish
Coroutine 6 took 0.21513676643371582 seconds to finish
Coroutine 18 took 0.2150111198425293 seconds to finish
Coroutine 32 took 0.21480584144592285 seconds to finish
Coroutine 35 took 0.2148134708404541 seconds to finish
Coroutine 36 took 0.2148447036743164 seconds to finish
Coroutine 41 took 0.21486520767211914 seconds to finish
Coroutine 46 took 0.2148454189300537 seconds to finish
Coroutine 4 took 0.29543209075927734 seconds to finish
Coroutine 38 took 0.2950417995452881 seconds to finish
Coroutine 43 took 0.2950429916381836 seconds to finish
Coroutine 16 took 0.34415507316589355 seconds to finish
Coroutine 20 took 0.3442239761352539 seconds to finish
Coroutine 37 took 0.34401893615722656 seconds to finish
Coroutine 11 took 0.41034889221191406 seconds to finish
Coroutine 17 took 0.4103872776031494 seconds to finish
Coroutine 31 took 0.41022348403930664 seconds to finish
Coroutine 44 took 0.4102191925048828 seconds to finish
Coroutine 9 took 0.4636690616607666 seconds to finish
Coroutine 23 took 0.46362781524658203 seconds to finish
Coroutine 27 took 0.4636392593383789 seconds to finish
Coroutine 28 took 0.46371984481811523 seconds to finish
Coroutine 8 took 0.5330097675323486 seconds to finish
Coroutine 19 took 0.5329856872558594 seconds to finish
Coroutine 21 took 0.533057689666748 seconds to finish
Coroutine 26 took 0.5330431461334229 seconds to finish
Coroutine 10 took 0.5977799892425537 seconds to finish
Coroutine 25 took 0.5976765155792236 seconds to finish
Coroutine 29 took 0.5977263450622559 seconds to finish
Coroutine 30 took 0.5978226661682129 seconds to finish
Coroutine 42 took 0.597785472869873 seconds to finish
Coroutine 48 took 0.5978381633758545 seconds to finish
Total time: 0.5989062786102295
```
time will differ from run to run as the time spent to wait for data is semi-random for every chunk
