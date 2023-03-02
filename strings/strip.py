# Real data sets are often messy, with whitespace, extra spaces and tabs, etc
# To enable proper use, they must be cleaned up

# We have a list of lines from a poem, with the list elements contain a lot of extra whitespace which needs to be removed:

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for element in love_maybe_lines:
    cleaned_element = element.strip()
    love_maybe_lines_stripped.append(cleaned_element)

print(love_maybe_lines_stripped)

# now we can safely join the list elements together:
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

# strip() works like split(), and can take any character as the parameter:

featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '

# To remove several unnecessary characters at once, we can chain several strip() method:

featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!').strip())
# => 'rob thomas'
# this will be difficult to see in the terminal, but it works
