#!/usr/bin/env python
import sys

def decomp(text, start=0, times=1):
    """
    Iterate over and decompress the compressed string.
    This approach makes use of nested Python iterators, which is a very clean way
    of expressing expansion of nested iterated items.
    Args:
        text: The entire string to decompress.  It's unobvious, but nice
          to have the whole string plus an index; this allows any error
          detection code to report the absolute index of a problematic
          character.
        start: The starting index within 'text'.  We decompress from
          'start' up through the matching close-brace or end-of-string.
        times: The number of times to repeat decompression.
    """
    # Repeat iteration over our sub-chunk N times.
    for _ in range(times):
        i = start
        # Until we hit the end of the string, or end of our chunk...
        while i < len(text) and text[i] != ']':
            # Emit letters as themselves.
            if text[i].islower():
                yield text[i]
                i += 1
            # If it's not a letter, it must be digit(s). Convert to integer.
            else:
                sub_times = 0
                while text[i].isdigit():
                    sub_times = sub_times * 10 + int(text[i])
                    i += 1
                i += 1  # Skip past open-bracket
                # Start an iterator over the sub-chunk.
                for item in decomp(text, i, sub_times):
                    # Iterator generates many characters, and then at the very end,
                    # it generates an integer. Provide characters up to our caller,
                    # and use the integer to advance our index 'i' to end-of-chunk.
                    if isinstance(item, str):
                        yield item
                    else:
                        i = item
                # Advance 'i' to the next letter, or skip the close-bracket, whichever.
                i += 1
    # Don't emit the trailing integer if we are doing the outermost call.
    if start > 0:
        yield i

def decompress(text):
    """
    A wrapper around decomp() to initiate decompression and write output directly to stdout.
    """
    for letter in decomp(text):
        sys.stdout.write(letter)
    sys.stdout.write('\n')

if __name__ == '__main__':
    decompress(sys.argv[1])
