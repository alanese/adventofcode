def count_routes(network, start, end, storage={}):
    if start == end:
        return 1
    elif start not in network:
        return 0
    else:
        if (start, end) not in storage:
            storage[(start, end)] = sum([count_routes(network, next, end, storage) for next in network[start]])
        return storage[(start, end)]

with open("input-11.txt") as f:
    network = {}
    for line in f:
        line = line.split()
        network[line[0][:-1]] = line[1:]

print(count_routes(network, "you", "out", {}))

#--------------
    
storage = {}
svrfft = count_routes(network, "svr", "fft", storage)
fftdac = count_routes(network, "fft", "dac", storage)
dacout = count_routes(network, "dac", "out", storage)
svrdac = count_routes(network, "svr", "dac", storage)
dacfft = count_routes(network, "dac", "fft", storage)
fftout = count_routes(network, "fft", "out", storage)

print(svrfft*fftdac*dacout + svrdac*dacfft*fftout)