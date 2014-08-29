ruby-vs-python-performance
==========================

Test ruby vs python2 / 3

launch benchmark (bash)

echo append_list.py
time python append_list.py; sleep 10
echo append_list.rb
time ruby append_list.rb; sleep 10
echo for_range.py
time python for_range.py; sleep 10
echo for_range.rb
time ruby for_range.rb; sleep 10

echo generate_incremental_list.py
time python generate_incremental_list.py; sleep 10
echo generate_incremental_list.rb
time ruby generate_incremental_list.rb; sleep 10

echo while_incremental.py
time python while_incremental.py; sleep 10
echo while_incremental.rb
time ruby while_incremental.rb; sleep 10 

echo process_no_concurrency.py 1
time python process_no_concurrency.py 1; sleep 10
echo process_no_concurrency.py 2
time python process_no_concurrency.py 2; sleep 10
echo process_no_concurrency.py 3
time python process_no_concurrency.py 3; sleep 10
echo process_no_concurrency.py 4
time python process_no_concurrency.py 4; sleep 10
echo process_no_concurrency.py 10
time python process_no_concurrency.py 10; sleep 10
echo process_no_concurrency.py 100
time python process_no_concurrency.py 100; sleep 10

echo process_no_concurrency.rb 1
time ruby process_no_concurrency.rb 1; sleep 10
echo process_no_concurrency.rb 2
time ruby process_no_concurrency.rb 2; sleep 10
echo process_no_concurrency.rb 3
time ruby process_no_concurrency.rb 3; sleep 10
echo process_no_concurrency.rb 4
time ruby process_no_concurrency.rb 4; sleep 10
echo process_no_concurrency.rb 10
time ruby process_no_concurrency.rb 10; sleep 10
echo process_no_concurrency.rb 100
time ruby process_no_concurrency.rb 100; sleep 10

echo threads_no_concurrency.py 1
time python threads_no_concurrency.py 1; sleep 10
echo threads_no_concurrency.py 2
time python threads_no_concurrency.py 2; sleep 10
echo threads_no_concurrency.py 3
time python threads_no_concurrency.py 3; sleep 10
echo threads_no_concurrency.py 4
time python threads_no_concurrency.py 4; sleep 10
echo threads_no_concurrency.py 10
time python threads_no_concurrency.py 10; sleep 10
echo threads_no_concurrency.py 100
time python threads_no_concurrency.py 100; sleep 10

echo threads_no_concurrency.rb 1
time ruby threads_no_concurrency.rb 1; sleep 10
echo threads_no_concurrency.rb 2
time ruby threads_no_concurrency.rb 2; sleep 10
echo threads_no_concurrency.rb 3
time ruby threads_no_concurrency.rb 3; sleep 10
echo threads_no_concurrency.rb 4
time ruby threads_no_concurrency.rb 4; sleep 10
echo threads_no_concurrency.rb 10
time ruby threads_no_concurrency.rb 10; sleep 10
echo threads_no_concurrency.rb 100
time ruby threads_no_concurrency.rb 100; sleep 10
