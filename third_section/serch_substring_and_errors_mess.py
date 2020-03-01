def test_substring(full_string, substring):
    if substring not in full_string:
        print(f'expected \'{substring}\' to be substring of \'{full_string}\'')
