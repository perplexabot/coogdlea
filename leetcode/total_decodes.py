"""Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count
the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
"""
import pytest

def total_decodes(msg):
    from string import ascii_lowercase

    msg = str(msg)
    if len(msg) in [0, 1]:
        return len(msg)

    decode_dict = {str(ind+1): char for ind, char in enumerate(ascii_lowercase)}
    decode_list = []

    # returns {decoded_part:encoded_part}
    def decode_front(msg):
        partial_decode = {}
        chars = [msg[0]] if int(msg[:2]) > 26 else [msg[0], msg[:2]]
        for char in chars:
            partial_decode[decode_dict[char]] = msg[len(char):]
        return partial_decode

    partial_dict = decode_front(msg)
    while partial_dict:
        to_remove = []
        to_add = {}
        for key in partial_dict:
            if not partial_dict[key]:
                decode_list.append(key)
            else:
                temp_dict = decode_front(partial_dict[key])
                for temp_key in temp_dict:
                    new_decode = key + temp_key
                    to_add[new_decode] = temp_dict[temp_key]
            to_remove.append(key)

        partial_dict.update(to_add)
        for key in to_remove:
            del partial_dict[key]

    return len(decode_list)

@pytest.mark.parametrize('msg, expected', [('111', 3),
                                           ('1', 1),
                                           ('12', 2),
                                           ('33', 1),
                                           ('1134', 3)])
def test_func(msg, expected):
    assert total_decodes(msg) == expected
