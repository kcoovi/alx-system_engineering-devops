#!/usr/bin/env ruby
# A script that accepts one argument and passes it to a regular expression,
# matching method
# The regular expression will match the given cases

puts ARGV[0].scan(/hbt*n/).join
