#!/usr/bin/env ruby
# A script that accepts one argument and passes it to a regular expression,
# matching method
# The regular expression that matches the given cases

puts ARGV[0].scan(/hbt{2,5}n/).join
