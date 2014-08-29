echo "bench append list 10000000"
time python append_list.py ; sleep 4; time ruby append_list.rb
echo "bench while incremental to 10000000"
time python while_incremental.py ; sleep 4; time ruby while_incremental.rb
