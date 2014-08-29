def func1(parte)
    i = 0
    while i<=parte
        i+=1
    end
end
total = 10000000
concurrency = ARGV[0].to_i
list_threads = []
for x in 0..concurrency
    list_threads.push(Thread.new{func1(total/concurrency)})
end
for x in list_threads
    x.join
end
