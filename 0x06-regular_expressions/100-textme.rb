#!/usr/bin/env ruby
logfile="text_messages.log"

# open and read the log file line by line
File.open(logfile).each do |line|

# use regex to extract sender, receiver and flags
data = line.match(/\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/)

# print the extracted details
puts "#{data[:sender]},#{data[:receiver]},#{data[:flags]}" if data
end